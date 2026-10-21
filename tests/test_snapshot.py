"""Offline contract tests for the optional public-source snapshot helper."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("snapshot", ROOT / "research/scripts/snapshot_github.py")
snapshot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(snapshot)
SHA = "a" * 40


class Response(io.BytesIO):
    status = 200

    def __init__(self, body=b"example\n", headers=None, status=200):
        super().__init__(body)
        self.headers = headers or {}
        self.status = status


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.destination = Path(self.temp.name) / "snapshot"

    def args(self, *extra, paths=("src/example.py",)):
        argv = ["--repo", "example/project", "--commit", SHA, "--out", str(self.destination)]
        for path in paths:
            argv += ["--path", path]
        return snapshot.arguments(argv + list(extra))

    def execute(self, responses, *extra, paths=("src/example.py",)):
        with patch.object(snapshot, "build_opener") as factory:
            factory.return_value.open.side_effect = responses
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                code = snapshot.run(self.args(*extra, paths=paths))
            return code, factory.return_value.open.call_args_list

    def manifest(self):
        return json.loads((self.destination / "manifest.json").read_text())

    def test_success_preserves_bytes_hash_revision_and_quoted_url(self):
        body = b"\x00original\xff\n"
        code, calls = self.execute([Response(body, {"Content-Length": str(len(body))})], paths=("dir/file name.txt",))
        self.assertEqual(code, 0)
        self.assertEqual((self.destination / "sources/dir/file name.txt").read_bytes(), body)
        manifest = self.manifest()
        self.assertEqual(manifest["status"], "complete")
        self.assertEqual(manifest["commit"], SHA)
        self.assertEqual(manifest["files"][0]["sha256"], hashlib.sha256(body).hexdigest())
        self.assertEqual(calls[0].args[0].full_url, f"https://raw.githubusercontent.com/example/project/{SHA}/dir/file%20name.txt")

    def test_partial_failure_preserves_first_file_and_stops(self):
        code, calls = self.execute([Response(b"kept"), URLError("unavailable"), Response(b"never")], paths=("a", "b", "c"))
        self.assertEqual(code, 1)
        self.assertEqual(len(calls), 2)
        self.assertEqual((self.destination / "sources/a").read_bytes(), b"kept")
        self.assertEqual(self.manifest()["status"], "partial")
        self.assertEqual([f["status"] for f in self.manifest()["files"]], ["saved", "failed"])
        self.assertFalse((self.destination / "sources/c").exists())

    def test_first_failure_records_failed_state(self):
        error = HTTPError("https://example.org", 404, "missing", {}, io.BytesIO(b"error body"))
        self.addCleanup(error.close)
        code, calls = self.execute([error])
        self.assertEqual((code, len(calls)), (1, 1))
        self.assertEqual(self.manifest()["status"], "failed")
        self.assertEqual(self.manifest()["files"][0]["http_status"], 404)
        self.assertTrue(error.closed)

    def test_interrupt_records_state_and_stops(self):
        code, calls = self.execute([KeyboardInterrupt(), Response()])
        self.assertEqual((code, len(calls)), (130, 1))
        self.assertEqual(self.manifest()["status"], "interrupted")

    def test_invalid_responses_never_save_source_bytes(self):
        cases = [
            Response(b"12345", {"Content-Length": "5"}),
            Response(b"12345"),
            Response(b"1", {"Content-Length": "2"}),
            Response(b"1", {"Content-Length": "-1"}),
            Response(b"1", {"Content-Length": "not-a-number"}),
            Response(b"1", {"Content-Encoding": "gzip"}),
            Response(b"1", status=206),
        ]
        for index, response in enumerate(cases):
            with self.subTest(index=index):
                self.destination = Path(self.temp.name) / str(index)
                code, calls = self.execute([response], "--max-bytes", "4")
                self.assertEqual((code, len(calls)), (1, 1))
                self.assertEqual(self.manifest()["status"], "failed")
                self.assertFalse((self.destination / "sources/src/example.py").exists())

    def test_existing_destination_refuses_before_network_and_preserves_bytes(self):
        self.destination.mkdir()
        existing = self.destination / "important"
        existing.write_bytes(b"preserve me")
        with patch.object(snapshot, "build_opener") as opener:
            with self.assertRaises(FileExistsError):
                snapshot.run(self.args())
            opener.assert_not_called()
        self.assertEqual(existing.read_bytes(), b"preserve me")

    def test_symlink_destination_refuses(self):
        target = Path(self.temp.name) / "target"
        target.mkdir()
        self.destination.symlink_to(target, target_is_directory=True)
        with self.assertRaises(FileExistsError):
            snapshot.run(self.args())
        self.assertEqual(list(target.iterdir()), [])

    def test_conflicting_nested_paths_record_failure_without_overwrite(self):
        code, calls = self.execute([Response(b"kept"), Response(b"not saved")], paths=("a", "a/b"))
        self.assertEqual((code, len(calls)), (1, 2))
        self.assertEqual((self.destination / "sources/a").read_bytes(), b"kept")
        self.assertEqual(self.manifest()["status"], "partial")

    def test_redirect_is_refused(self):
        request = snapshot.Request("https://raw.githubusercontent.com/example/project/file")
        body = io.BytesIO(b"redirect")
        with self.assertRaises(HTTPError) as caught:
            snapshot.NoRedirect().redirect_request(request, body, 302, "moved", {}, "https://example.org")
        self.assertEqual(caught.exception.code, 302)
        self.assertEqual(caught.exception.url, request.full_url)
        caught.exception.close()

    def test_unsafe_source_paths_are_rejected(self):
        for value in ("", "/abs", "../a", "a/../b", "a//b", "./a", "a/", "a\\b", "a\x00b", "a\x7fb", "a\nb"):
            with self.subTest(value=repr(value)):
                with self.assertRaises(snapshot.argparse.ArgumentTypeError):
                    snapshot.source_path(value)

    def test_invalid_cli_values_reject_before_creating_output(self):
        for extra in (["--repo", "a/../b"], ["--repo", "a/.."], ["--commit", "main"], ["--commit", "g" * 40], ["--max-bytes", "0"], ["--timeout", "0"], ["--timeout", "301"], ["--timeout", "nan"], ["--path", "src/example.py"]):
            with self.subTest(extra=extra), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    self.args(*extra)
                self.assertEqual(error.exception.code, 2)
        self.assertFalse(self.destination.exists())


if __name__ == "__main__":
    unittest.main()
