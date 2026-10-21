#!/usr/bin/env python3
"""Save selected public GitHub files at one explicit commit, without execution."""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from http.client import HTTPException
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import HTTPRedirectHandler, Request, build_opener


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise HTTPError(req.full_url, code, "redirect refused", headers, fp)


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def source_path(value):
    if not value or "\\" in value or any(
        part in ("", ".", "..") for part in value.split("/")
    ) or any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise argparse.ArgumentTypeError("paths must be relative repository file paths")
    return value


def arguments(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="public owner/repository")
    parser.add_argument("--commit", required=True, help="full 40-character commit SHA")
    parser.add_argument("--path", action="append", type=source_path, required=True)
    parser.add_argument("--out", type=Path, required=True, help="new snapshot directory")
    parser.add_argument("--max-bytes", type=int, default=4 * 1024 * 1024,
                        help="maximum bytes per file (default: 4 MiB)")
    parser.add_argument("--timeout", type=float, default=25,
                        help="network timeout per request in seconds")
    args = parser.parse_args(argv)
    if not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("--repo must be owner/repository")
    if args.repo.split("/")[1] in (".", ".."):
        parser.error("invalid repository name")
    if not re.fullmatch(r"[0-9a-fA-F]{40}", args.commit):
        parser.error("--commit must be a full 40-character hexadecimal SHA")
    if len(set(args.path)) != len(args.path):
        parser.error("duplicate --path")
    if args.max_bytes < 1 or not (0 < args.timeout <= 300):
        parser.error("--max-bytes must be positive; --timeout must be in (0, 300]")
    args.commit = args.commit.lower()
    return args


def save_manifest(destination, manifest):
    # Only the fresh snapshot's own manifest is replaced, never a source file.
    temporary = destination / ".manifest.tmp"
    with temporary.open("x", encoding="utf-8") as stream:
        json.dump(manifest, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    temporary.replace(destination / "manifest.json")


def run(args):
    destination = args.out.absolute()
    destination.mkdir(mode=0o700)  # Existing destinations, including symlinks, refuse.
    sources = destination / "sources"
    sources.mkdir(mode=0o700)
    manifest = {
        "repository": args.repo,
        "commit": args.commit,
        "started_at": timestamp(),
        "status": "in_progress",
        "requested_paths": args.path,
        "files": [],
        "note": "Hashes identify downloaded bytes, not independently verified Git blobs. "
                "Source selection, reading, licensing and usefulness remain caller decisions.",
    }
    save_manifest(destination, manifest)
    opener = build_opener(NoRedirect())
    for path in args.path:
        url = ("https://raw.githubusercontent.com/" + args.repo + "/" + args.commit
               + "/" + quote(path, safe="/"))
        record = {"path": path, "url": url, "requested_at": timestamp()}
        try:
            request = Request(url, headers={"User-Agent": "CodexResearchSnapshot/1",
                                            "Accept-Encoding": "identity"})
            with opener.open(request, timeout=args.timeout) as response:
                record["http_status"] = response.status
                if response.status != 200:
                    raise ValueError("expected HTTP 200")
                if response.headers.get("Content-Encoding", "identity").lower() != "identity":
                    raise ValueError("unexpected content encoding")
                length = response.headers.get("Content-Length")
                expected = int(length) if length is not None else None
                if expected is not None and not (0 <= expected <= args.max_bytes):
                    raise ValueError("invalid or oversized Content-Length")
                data = response.read(args.max_bytes + 1)
                if len(data) > args.max_bytes:
                    raise ValueError("file exceeds --max-bytes")
                if expected is not None and len(data) != expected:
                    raise ValueError("incomplete response body")
            target = sources / path
            target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(data)
            record.update(status="saved", bytes=len(data),
                          sha256=hashlib.sha256(data).hexdigest(), saved_at=timestamp())
        except (OSError, URLError, ValueError, HTTPException, KeyboardInterrupt) as error:
            interrupted = isinstance(error, KeyboardInterrupt)
            if isinstance(error, HTTPError):
                record.update(http_status=error.code, error="HTTP request refused or unavailable")
                error.close()
            elif isinstance(error, ValueError):
                record["error"] = str(error)
            else:
                record["error"] = type(error).__name__
            record["status"] = "interrupted" if interrupted else "failed"
            manifest["files"].append(record)
            manifest["status"] = "interrupted" if interrupted else "partial" if any(
                item["status"] == "saved" for item in manifest["files"]
            ) else "failed"
            manifest["finished_at"] = timestamp()
            save_manifest(destination, manifest)
            print(json.dumps({"status": manifest["status"], "manifest": str(destination / "manifest.json"),
                              "failed_path": path, "error": record["error"]}), file=sys.stderr)
            return 130 if interrupted else 1  # No retries or later requests after failure.
        manifest["files"].append(record)
        save_manifest(destination, manifest)
    manifest.update(status="complete", finished_at=timestamp())
    save_manifest(destination, manifest)
    print(json.dumps({"status": "complete", "files": len(manifest["files"]),
                      "bytes": sum(item["bytes"] for item in manifest["files"]),
                      "manifest": str(destination / "manifest.json")}))
    return 0


def main(argv=None):
    args = arguments(argv)
    try:
        return run(args)
    except KeyboardInterrupt:
        print("snapshot interrupted; inspect the destination manifest", file=sys.stderr)
        return 130
    except OSError as error:
        print("snapshot refused: " + type(error).__name__, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
