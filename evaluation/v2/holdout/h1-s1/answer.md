Use **EPA AirData’s public daily monitor query**, with one site and year per export. It needs no account or API key. This is a feasible acquisition route, but I could not verify delivery of both years: the 2023 query generated a CSV link; the 2024 site selector returned a backend error. No measurement files were downloaded.

OpenAQ’s current API requires an account-issued key. Open-Meteo supplies CAMS model output, so its Chicago values do not answer a question about measurements at regulatory sites. EPA’s separate AQS API also requires a key. [OpenAQ authentication](https://docs.openaq.org/using-the-api/api-key), [Open-Meteo data sources](https://open-meteo.com/en/docs/air-quality-api), [EPA access methods](https://www.epa.gov/outdoor-air-quality-data/what-best-way-access-outdoor-air-monitoring-data).

Reproducible acquisition plan:

1. Open [Download Daily Data](https://www.epa.gov/outdoor-air-quality-data/download-daily-data). Choose PM2.5 → 2023 → Illinois → one Monitor Site → Get Data. I tested `170310001` (`17-031-0001`); this produced “Download CSV (spreadsheet),” valid for ten minutes. Regenerate the link each run. Repeat for 2024, waiting for each selector to finish loading. Record the filters and any errors.
2. Define the study boundary before selecting sites. Cook County includes places outside Chicago; the Chicago metropolitan area includes other counties and states. Use EPA’s [monitor map](https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors) to select regulatory sites within the intended geography, then intersect the two years’ site lists. Verify monitoring purpose, instruments and operating dates rather than assuming every PM2.5 sensor is regulatory.
3. Copy each generated CSV URL into a size-limited downloader. Reject declared sizes ≥1,048,576 bytes; for unknown lengths, stream at most 1,048,575 bytes and reject a response that has not ended. Save only complete, parseable CSVs below that ceiling. Keep each site-year separate; do not fetch the national ZIPs and split afterward. EPA lists 2023/2024 national 88101 ZIPs at roughly 9.7/8.2 MB, already too large. [Download inventory](https://aqs.epa.gov/aqsweb/airdata/download_files.html).
4. Archive original bytes, retrieval UTC, query selections, byte count, SHA-256 hash, header, row count and available last-change dates. Validate dates, units and site identity. If the simplified export omits instrument/method or event information, resolve that metadata before treating the comparison as controlled. EPA now links a [replacement AirData app](https://rconnect-public.epa.gov/AirData/); its export was not verified here.

**The comparison is defensible as a description of measured conditions at the selected sites**, conditional on these checks. Compare daily mean concentrations in µg/m³, with consistent local-day definitions, instruments, sample durations and event treatment. Preserve missing days as missing; report valid-day counts and seasonal coverage separately for each year. A monitor sampling every third day cannot supply daily observations between samples. Use the same sites and comparable seasonal coverage; a two-year difference alone does not establish a long-term trend or neighborhood-wide exposure.

A consequential trap: EPA recommends excluding original T640/T640X method codes **236/238**, using corrected **736/738** and updated **636/638** where applicable. Do not count both versions. [EPA advisory, posted August 26, 2024](https://aqs.epa.gov/aqsweb/airdata/Data_Advisory_PM25_88101_Pregen_Files.pdf).

Real documented schema example, selected fields from EPA’s daily-summary format, **not a retrieved measurement or a confirmed header for the simplified export**:

```text
State Code,County Code,Site Num,Parameter Code,POC,Sample Duration,
Pollutant Standard,Date Local,Units of Measure,Event Type,
Observation Count,Observation Percent,Arithmetic Mean,Method Code,Method Name
```

`POC` distinguishes instruments at one site. EPA documents multiple rows per monitor-day for durations, standards and exceptional events: select a consistent series before summarizing, rather than averaging duplicate representations. [Official schema, §5.1–5.2](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html).
