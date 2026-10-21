"""Release integrity checks, independent of model wording or behavioral scores."""
import hashlib
import json
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_frozen_artifact_identities(self):
        for filename in ("evaluation/manifest.json", "evaluation/v2/manifest.json"):
            manifest = json.loads((ROOT / filename).read_text())
            for name, expected in manifest["files"].items():
                with self.subTest(manifest=filename, name=name):
                    self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), expected)

    def test_relative_document_links_resolve(self):
        for document in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                path = target.split("#", 1)[0]
                with self.subTest(document=str(document.relative_to(ROOT)), target=target):
                    self.assertTrue((document.parent / path).exists())

    def test_banner_is_valid_svg_without_external_resources(self):
        for svg in (ROOT / "assets").glob("*.svg"):
            tree = ET.parse(svg)
            self.assertEqual(tree.getroot().tag, "{http://www.w3.org/2000/svg}svg")
            ids = [e.attrib["id"] for e in tree.iter() if "id" in e.attrib]
            self.assertEqual(len(ids), len(set(ids)))
            for element in tree.iter():
                self.assertNotIn(element.tag.rsplit("}", 1)[-1], ("script", "foreignObject"))
                for key, value in element.attrib.items():
                    if key.rsplit("}", 1)[-1] in ("href", "src"):
                        self.assertTrue(value.startswith("#"))

    def test_source_files_contain_no_symlinks_or_local_home_paths(self):
        for folder in (ROOT / "research", ROOT / "docs", ROOT / "evaluation"):
            for path in folder.rglob("*"):
                # Python may create bytecode while running this very suite.
                # Generated caches are excluded from Git and release archives.
                if "__pycache__" in path.parts:
                    continue
                with self.subTest(path=str(path.relative_to(ROOT))):
                    self.assertFalse(path.is_symlink())
                    if path.is_file():
                        self.assertNotIn(b"/Users/", path.read_bytes())


if __name__ == "__main__":
    unittest.main()
