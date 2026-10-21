Use **EPA AirData’s public daily-download tool**. I retrieved measured records without an account or key for Chicago’s ComEd site, **17-031-0076**. Its complete returned CSVs were **113,895 bytes (2023)** and **96,622 bytes (2024)**, both below 1 MiB. These are direct retrieval observations, not a completed neighborhood comparison. [EPA tool](https://www.epa.gov/outdoor-air-quality-data/download-daily-data)

Open-Meteo supplies CAMS atmospheric-model output, including a roughly 45-km global product covering Chicago. Even with historical coverage, that does not meet “measured at regulatory sites.” [Data sources](https://open-meteo.com/en/docs/air-quality-api#data-sources)

OpenAQ’s current API requires a key. Its public AWS archive is a legitimate account-free alternative, with unsigned access and daily location files, but Chicago station identity, regulatory provenance and both-year completeness still need verification. EPA avoids that extra mapping step. [API authentication](https://docs.openaq.org/using-the-api/api-key), [archive access](https://docs.openaq.org/aws/quick-start)

**Acquisition plan**

1. Define the geography first. Cook County and the Chicago metropolitan area include suburbs; neither means the city or a particular neighborhood. Use EPA’s monitor map and site metadata to select the actual sites, recording coordinates, addresses and selection rationale. [Monitor map](https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors)
2. In the public tool choose PM2.5 → 2023 → Illinois → one site → Get Data. Download the generated CSV within its ten-minute lifetime; repeat for 2024 and each selected site. The compact example reproduces the request programmatically using only Python’s standard library.
3. Apply the size guard to every response, including the query response. Save original bytes, retrieval date, exact query, byte count and SHA-256 hash. Reject HTML/error responses masquerading as CSV. For any oversized site-year, stop; a smaller export from the new AirData app would need separate verification.
4. Preserve the returned schema and filter explicitly: `Source=AQS`, concentration units `ug/m3 LC`, and parameter `88101` for the approved reference/equivalent-method PM2.5 series. The tool also returns `88502`; do not silently mix it into that series. Keep POC, the instrument identifier, and Method Code. [EPA parameter categories](https://aqs.epa.gov/aqsweb/airdata/download_files.html)

**Is the comparison defensible?** Yes, as a descriptive comparison of measurements at the selected sites, conditional on method and sampling checks. It does not establish neighborhood-wide exposure or why concentrations changed.

The ComEd response demonstrates the trap: 2023 contains 384 rows and 2024 contains 326, but each has only **60 rows for parameter 88101, POC 1, method 545**. The remaining rows belong to a different stream. A daily archive need not contain a measurement on every calendar day.

Compare consistent site/instrument/method streams; investigate replacements and EPA’s T640 correction advisory before joining data. Report valid sampled days and seasonal coverage against the operating schedule, retain missing dates, and disclose 2024’s leap day. Use concentrations rather than AQI. Report site-specific distributions and seasonal summaries; show sensitivity to unequal coverage. Keep smoke episodes in the primary description of what was measured; any event-exclusion analysis requires verified event flags. [Monitor identifiers and sampling](https://www.epa.gov/outdoor-air-quality-data/about-airdata-reports), [correction advisory](https://aqs.epa.gov/aqsweb/airdata/Data_Advisory_PM25_88101_Pregen_Files.pdf)

EPA says its legacy tools retire December 18, 2026; migrate this acquisition to the new app before then. That replacement workflow was not tested here. [Transition notice](https://www.epa.gov/outdoor-air-quality-data/legacy-airdata-tools-and-reports)

Compact example, tested request structure; run once per site/year. The abbreviated record below is an actual returned row.

```python
import urllib.request as U, urllib.parse as P, re, csv, io, hashlib
limit = 1_048_576
def get(url):
    with U.urlopen(url, timeout=40) as r:
        b = r.read(limit)
    if len(b) >= limit: raise ValueError("Response reaches 1 MiB")
    return b
base = "https://www3.epa.gov/cgi-bin/broker"
query = base + "?" + P.urlencode({
    "_service":"data", "_debug":"0",
    "_program":"dataprog.ad_data_daily_airnow_method.sas",
    "poll":"88101','88502", "year":"2023", "state":"17",
    "cbsa":"-1", "county":"-1", "site":"170310076"})
html = get(query).decode()
url = re.search(r'href="([^"]+)"', html).group(1)
data = get(url)
rows = list(csv.DictReader(io.StringIO(data.decode())))
assert rows and "Daily Mean PM2.5 Concentration" in rows[0]
print(len(data), hashlib.sha256(data).hexdigest())
# Save data and the query/hash metadata locally after validation.
```

```csv
Date,Source,Site ID,POC,Daily Mean PM2.5 Concentration,Units,AQS Parameter Code,Method Code
01/06/2023,AQS,170310076,1,10.5,ug/m3 LC,88101,545
```

