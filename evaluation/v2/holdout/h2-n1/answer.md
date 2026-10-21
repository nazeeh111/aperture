A GitHub releases Atom feed is useful, but insufficient. It follows release announcements, while security advisories are separate records and can change independently. A finite feed also cannot serve as a complete history after a long outage.

Use two public, anonymous sources:

- **Published packages:** [PyPI’s JSON index](https://pypi.org/simple/pillow/), requested with `Accept: application/vnd.pypi.simple.v1+json`. Select a stable version, then check its files at `https://pypi.org/pypi/Pillow/VERSION/json`; exclude versions whose files are all yanked. PyPI recommends the index instead of the deprecated project JSON `releases` field. See [index documentation](https://docs.pypi.org/api/index-api/) and [JSON documentation](https://docs.pypi.org/api/json/).
- **Advisories:** [GitHub’s public advisory endpoint](https://api.github.com/advisories?ecosystem=pip&affects=pillow&per_page=100). Follow pagination and compare complete records so edits and withdrawals also produce alerts. It supports anonymous public requests, package filtering, affected ranges and patched versions. Its default reviewed coverage can lag a maintainer’s announcement; periodically inspect [Pillow’s own advisories](https://github.com/python-pillow/Pillow/security/advisories). See [API documentation](https://docs.github.com/en/rest/security-advisories/global-advisories).

Keep the Atom feed as an optional human-readable supplement: [Pillow release feed](https://github.com/python-pillow/Pillow/releases.atom).

The following **one-shot pilot** uses Python 3’s standard library. Save it as `watch_pillow.py`, then run `python3 watch_pillow.py` from a dedicated writable directory. It creates only local state. First run reports the current baseline; a second unchanged run should say “No change.” It reports package-wide advisories; compare their affected ranges with the version actually deployed before deciding whether action is needed. No automatic upgrades.

The version filter deliberately supports Pillow’s ordinary three-number final releases, not general Python version ordering. If Pillow changes its version scheme, revise that filter using a proper PEP 440 parser already available locally.

```python
import hashlib, json, os, re, sys
from pathlib import Path
from urllib.request import Request, urlopen

state = Path("pillow-watch-state.json")
def get(url, accept="application/json"):
    req = Request(url, headers={"Accept": accept,
                                "User-Agent": "local-pillow-watch"})
    with urlopen(req, timeout=30) as response:
        return json.load(response), response.headers

try:
    index, _ = get("https://pypi.org/simple/pillow/",
                  "application/vnd.pypi.simple.v1+json")
    versions = sorted(
        (v for v in index["versions"]
         if re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", v)),
        key=lambda v: tuple(map(int, v.split("."))), reverse=True)
    latest = None
    for v in versions:
        release, _ = get(f"https://pypi.org/pypi/Pillow/{v}/json")
        if any(not f["yanked"] for f in release["urls"]):
            latest = v
            break
    if latest is None:
        raise ValueError("No supported stable, non-yanked release")
    advisories = {}
    url = ("https://api.github.com/advisories"
           "?ecosystem=pip&affects=pillow&per_page=100")
    while url:
        records, headers = get(url, "application/vnd.github+json")
        if not isinstance(records, list):
            raise ValueError("Unexpected advisory response")
        for a in records:
            digest = hashlib.sha256(
                json.dumps(a, sort_keys=True).encode()).hexdigest()
            advisories[a["ghsa_id"]] = {
                "digest": digest, "url": a["html_url"],
                "withdrawn": a["withdrawn_at"]}
        next_link = re.search(r'<([^>]+)>; rel="next"',
                              headers.get("Link", ""))
        url = next_link.group(1) if next_link else None
    current = {"latest": latest, "advisories": advisories}
    old = json.loads(state.read_text()) if state.exists() else {}
    if current != old:
        print(json.dumps(current, indent=2))
    else:
        print("No change")
    temp = state.with_suffix(".tmp")
    temp.write_text(json.dumps(current, sort_keys=True))
    os.replace(temp, state)
except Exception as error:
    print(f"CHECK FAILED; prior state retained: {error}", file=sys.stderr)
    sys.exit(1)
```

For daily operation, later connect this one-shot command to an existing local scheduler, retain stdout/stderr and exit status, and expose the last successful check time. Surface failures separately from “no change”; respect rate-limit/backoff headers and retry transient failures within a bounded window. A sleeping/offline computer and delayed advisory publication limit timeliness. No scheduler or subscription was created.

**Verification:** Python 3 is present and the pilot passes a syntax check. All four direct endpoint probes failed DNS resolution in this execution environment, so live responses and two-run behavior remain unverified. Official documentation was accessible through web lookup; the web fetch of the Atom feed returned a cache-miss error.
