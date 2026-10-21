No. Use GitHub’s [releases Atom feed](https://github.com/python-pillow/Pillow/releases.atom) for convenience, but use PyPI for package availability and separate advisory sources for security.

A concrete counterexample, checked October 21, 2026: [Pillow 13.0.0](https://github.com/python-pillow/Pillow/releases/tag/13.0.0) was released October 16; [GHSA-654x-cwwv-5j9c](https://github.com/python-pillow/Pillow/security/advisories/GHSA-654x-cwwv-5j9c), published October 19, lists affected versions 11.2.1–13.0.0 and no patched version. It concerns Arrow export with `PILLOW_ALIGNMENT > 1`. An advisory can therefore require attention without a new release. These are publisher reports, not a locally reproduced vulnerability.

A practical design:

- **Releases:** Read `https://pypi.org/simple/pillow/` with `Accept: application/vnd.pypi.simple.v1+json`. Track stable versions with at least one non-yanked file, plus subsequent withdrawals. PyPI [recommends this index API](https://docs.pypi.org/api/index-api/); its project JSON `releases` key is [deprecated](https://docs.pypi.org/api/json/). Package availability does not establish compatibility with your Python or platform.
- **Advisories:** Poll the repository’s published advisories and [global package advisories](https://docs.github.com/en/rest/security-advisories/global-advisories), following pagination. Repository records can precede global review; global records can originate outside the repository. Global queries default to reviewed advisories, excluding malware. Preserve affected ranges, patch information, IDs, revisions and withdrawals. Alert on changes, even when the release version stays constant.
- **Coverage:** Optionally query `POST https://api.osv.dev/v1/query` with `{"package":{"ecosystem":"PyPI","name":"Pillow"},"version":"YOUR_DEPLOYED_VERSION"}`, following `next_page_token`. This is a read-only query. OSV [imports GitHub and PyPI advisory data](https://google.github.io/osv.dev/data/), so overlap is not independent corroboration. Neither service guarantees every disclosure or immediate indexing. An empty result is not a clean bill of health. Pillow’s [security guidance](https://pillow.readthedocs.io/en/stable/handbook/security.html) also calls out bundled C libraries: a Pillow-only package query cannot establish their safety.

For the daily watcher, retain a local last-successful snapshot per source. Report new versions, changed/yanked versions and new/revised/withdrawn advisories, grouping aliases such as CVE and GHSA while retaining provenance. Print locally; do not auto-upgrade. Use timeouts, conditional requests where supported, and bounded backoff respecting `Retry-After`. A failed source must produce an error and retain its old snapshot, never imply “no changes.” A daily check also needs a visible last-success time; a sleeping computer cannot provide continuous coverage.

**Manual pilot:** Save this as `pillow_watch.py` and run using an existing Python 3. It needs no third-party packages. It deliberately accepts only Pillow’s ordinary numeric stable versions; unexpected future version conventions need review. No scheduler is created. Run once daily manually, retaining the baseline; later automation would be separate work.

```python
import json, re, urllib.request

def fetch(url, accept):
    req = urllib.request.Request(url, headers={
        "Accept": accept, "User-Agent": "local-pillow-watch/1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r), r.headers.get("Link", "")

def pages(url):
    out = []
    while url:
        data, links = fetch(url, "application/vnd.github+json")
        if not isinstance(data, list):
            raise ValueError("Expected advisory list")
        out.extend(data)
        nxt = re.search(r'<([^>]+)>;\s*rel="next"', links)
        url = nxt.group(1) if nxt else None
    return {a["ghsa_id"]: a for a in out}

def releases(index):
    versions = {}
    for f in index["files"]:
        m = re.match(r"(?i)^pillow-(\d+(?:\.\d+)+)(?:-|\.tar\.gz$|\.zip$)",
                     f["filename"])
        if m:
            v = m.group(1)
            versions[v] = versions.get(v, False) or not f["yanked"]
    if not versions:
        raise ValueError("No recognized stable release files")
    available = [v for v, ok in versions.items() if ok]
    return {"latest": max(available, key=lambda v: tuple(map(int, v.split('.')))),
            "available": versions}

def main():
    index, _ = fetch("https://pypi.org/simple/pillow/",
                     "application/vnd.pypi.simple.v1+json")
    snapshot = {"releases": releases(index),
        "repository": pages("https://api.github.com/repos/python-pillow/"
                            "Pillow/security-advisories?per_page=100"),
        "global_reviewed": pages("https://api.github.com/advisories?"
                            "ecosystem=pip&affects=Pillow&per_page=100")}
    print(json.dumps(snapshot, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
```

```sh
# First successful run establishes the baseline.
python3 pillow_watch.py > candidate.json && mv candidate.json baseline.json
# On later days, inspect differences. diff exit 1 means differences, not failure.
python3 pillow_watch.py > candidate.json && diff -u baseline.json candidate.json
# After review, explicitly replace baseline.json with candidate.json.
```

This pilot compares raw advisory records, so cosmetic revisions can also appear. It is a coverage and change-detection trial, not the finished alerting service. Locally, stable/prerelease/yank filtering and pagination passed synthetic checks. Live Python requests failed DNS resolution; browser access retrieved original documentation and advisory pages, but not the Atom/API responses. End-to-end operation remains unverified.
