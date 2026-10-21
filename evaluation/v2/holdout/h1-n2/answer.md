Use EPA AirData’s **Download Daily Data** form for measured monitor data. A descriptive 2023–2024 comparison is feasible without an account or API key, provided the same suitable monitors and comparable daily measurements exist in both years. It would describe those sites, not every Chicago neighborhood.

OpenAQ’s current programmatic route requires an account and API key. Open-Meteo’s Chicago air-quality series comes from CAMS global model forecasts, approximately 45 km resolution; it is unsuitable as a substitute for regulatory-site measurements. [OpenAQ requirements](https://docs.openaq.org/about/terms), [Open-Meteo sources](https://open-meteo.com/en/docs/air-quality-api)

**Acquisition plan**

1. Open [EPA Download Daily Data](https://www.epa.gov/outdoor-air-quality-data/download-daily-data). Select PM2.5 → 2023 → county “IL - Cook” → one site → Get Data. Repeat for 2024 and each selected site. Use Cook County for discovery, then check site coordinates and addresses against Chicago boundaries and the nonprofit’s actual neighborhood; the Chicago metropolitan option includes areas outside the city.
2. I executed the 2023 selection for site **170310022** and received a CSV download link, valid for ten minutes. This verifies the form’s export-generation path, not the file contents or 2024 completeness. Regenerate links rather than treating the temporary URL as a permanent API.
3. Copy each generated CSV link into the size-capped downloader below. It stores only responses smaller than 1 MiB. Query one site/year at a time; do not download the nationwide archives, listed around 9.7 MB for 2023 and 8.2 MB for 2024. If a site export exceeds the limit, stop and seek a smaller supported export rather than downloading and splitting it afterward. [EPA file inventory](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
4. Preserve original CSVs and a manifest containing selections, retrieval time, source URL, bytes and SHA-256. Check the returned headers, date range, units, site identity and pollutant. Restrict the study to parameter **88101**, EPA’s reference/equivalent-method PM2.5 category, and verify regulatory classification and monitor history through EPA’s monitor map or the reporting agency. Do not assume every PM2.5 selection is eligible.

**Make the comparison defensible**

Preselect sites operating in both years. Resolve colocated instruments using POC, the code distinguishing instruments at one site; check method changes. Use one consistent daily concentration series in µg/m³ and EPA’s local-standard-day boundary. Avoid counting duplicate summaries for different standards, durations or event treatments. These distinctions are documented in [EPA’s daily schema](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html).

For each site/year report observed days, expected sampling schedule, quarterly coverage, missingness, mean, median and daily distribution. Do not fill missing days with zero. Compare common seasonal coverage; show a matched-calendar-day sensitivity analysis and handle February 29 separately. Keep exceptional-event measurements in the primary description of measured air, with a separately labeled exclusion sensitivity analysis where flags support it. Do not silently remove smoke peaks.

Report site-specific differences before any equal-site aggregate. Two years cannot establish a long-term trend or identify causes. Annual compliance determinations need their own regulatory rules.

**Verification limits:** no CSV was downloaded or analyzed. The shell could not resolve EPA’s host; the web reader could not access the generated session link. EPA also links a PM2.5 data advisory whose PDF timed out; inspect it before accepting final results. Acquisition is feasible through the verified form, while complete data delivery and a numerical comparison remain unverified.

Compact example: genuine EPA daily-summary field subset, not an invented observation or a claim about the form’s exact export headers:

```text
State Code, County Code, Site Num, Parameter Code, POC,
Sample Duration, Pollutant Standard, Date Local, Units of Measure,
Event Type, Observation Count, Observation Percent, Arithmetic Mean,
Method Code, Method Name
```

Size-capped acquisition example (Python standard library; paste a fresh export URL):

```python
import urllib.request, pathlib, hashlib
url = input("Fresh EPA CSV URL: ")
with urllib.request.urlopen(url, timeout=60) as r:
    data = r.read(1048576)
if len(data) >= 1048576:
    raise ValueError("Limit reached; nothing saved. Narrow the query.")
if b"<html" in data[:1000].lower():
    raise ValueError("HTML response, not a validated CSV.")
pathlib.Path("site-year.csv").write_bytes(data)
print(len(data), hashlib.sha256(data).hexdigest())
```

