A GitHub releases Atom feed is useful, but **it is not enough**. Release announcements and security advisories are separate records. Pillow’s [release procedure](https://github.com/python-pillow/Pillow/blob/main/RELEASING.md) explicitly includes publishing GitHub security advisories for security fixes. A release feed cannot establish that a project’s installed version has no known vulnerabilities.

Use two public, account-free inputs:

- **Stable releases:** [PyPI’s Pillow JSON endpoint](https://pypi.org/pypi/Pillow/json). Select the greatest numeric `major.minor.patch` version with at least one non-yanked file, excluding prereleases and empty releases. This deliberately uses Pillow’s current version shape rather than claiming to implement every Python version format. The [PyPI API documentation](https://docs.pypi.org/api/json/) describes release and file metadata.
- **Security advisories:** [GitHub’s reviewed Pillow advisories](https://api.github.com/advisories?ecosystem=pip&affects=Pillow&type=reviewed&per_page=100). This package-wide query also catches advisories outside the upstream repository. Follow every `Link: rel="next"` page. The [API documentation](https://docs.github.com/en/rest/security-advisories/global-advisories) confirms public unauthenticated access, package filtering, update fields and pagination. Optionally also watch [upstream repository advisories](https://api.github.com/repos/python-pillow/Pillow/security-advisories?per_page=100), deduplicating by GHSA ID, to complement the reviewed database.

For a practical daily watcher, keep a local JSON baseline containing the stable release, advisory IDs and content hashes, plus each source’s last successful check. Alert locally when a release changes or an advisory is added, edited or withdrawn. Show advisory links and affected/fixed versions for human review; do not equate every Pillow advisory with exposure in this project. Record the actual installed or locked version separately. Bundled native libraries and other dependencies need additional coverage.

On first run, display the current release and existing advisories for review before accepting a baseline. Fetch and validate complete results before replacing state atomically. An HTTP error, malformed response, timeout or incomplete pagination must produce a visible failure and preserve the prior baseline. Report stale checks explicitly; silence must not mean “safe.” Use bounded retries on a later attempt and respect `Retry-After` and rate-limit headers. GitHub documents [60 unauthenticated requests per hour per originating IP](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api), shared with other users behind that IP.

Pilot below: save as `pillow_snapshot.py` and run with an existing Python 3 interpreter. It makes read-only public requests and prints a complete snapshot; it neither installs anything nor schedules a job. Run it manually on successive days and compare successful snapshots. It intentionally prints the full advisory baseline on every run; persistent deduplication, local notifications and scheduling are the next implementation step, not features claimed here. An existing scheduler could later invoke it daily, with a missed-run check after sleep or shutdown.

**Verification:** the script compiled and passed mocked checks for numeric ordering, prerelease/yanked/empty exclusion, two-page advisory retrieval, withdrawn metadata and failure propagation. Live terminal requests failed DNS resolution for all tested hosts. The web reader accessed PyPI and official documentation but could not fetch the Atom or repository-advisory endpoint. No current release/advisory count or end-to-end network success is claimed. No installs, jobs, subscriptions, accounts, credentials or remote writes were performed.

```python
# Python 3; standard library only. Run: python3 pillow_snapshot.py
import json, re, sys
from urllib.request import Request, urlopen

def get(url):
    req = Request(url, headers={
        "User-Agent": "local-pillow-watcher",
        "Accept": "application/json"})
    with urlopen(req, timeout=25) as response:
        return json.load(response), response.headers.get("Link", "")

def stable(releases):
    versions = [
        (tuple(map(int, v.split("."))), v)
        for v, files in releases.items()
        if re.fullmatch(r"\d+\.\d+\.\d+", v)
        and any(not f.get("yanked", False) for f in files)
    ]
    return max(versions)[1]

def snapshot():
    package, _ = get("https://pypi.org/pypi/Pillow/json")
    advisories, url = {}, (
        "https://api.github.com/advisories"
        "?ecosystem=pip&affects=Pillow&type=reviewed&per_page=100")
    while url:
        page, links = get(url)
        for a in page:
            advisories[a["ghsa_id"]] = {
                k: a.get(k) for k in (
                    "updated_at", "withdrawn_at", "summary", "html_url")}
        match = re.search(r'<([^>]+)>; rel="next"', links)
        url = match.group(1) if match else None
    return {"latest_stable": stable(package["releases"]),
            "advisories": advisories}

if __name__ == "__main__":
    try:
        print(json.dumps(snapshot(), indent=2, sort_keys=True))
    except Exception as error:
        print("WATCH FAILED: " + str(error), file=sys.stderr)
        sys.exit(1)
```
