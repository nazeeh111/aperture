Use EPA AirData’s public **Download Daily Data** form. It needs no account or key in the workflow I tested: PM2.5 → 2024 → Illinois → site **170310001** → Get Data produced a CSV link. This verifies the public query route, not the CSV’s contents or this site’s suitability for the nonprofit’s neighborhood. [EPA form](https://www.epa.gov/outdoor-air-quality-data/download-daily-data)

OpenAQ’s current API requires an account-issued key; its retired v1/v2 endpoints are not a workaround. Open-Meteo supplies CAMS atmospheric model output, including a roughly 45 km global grid, rather than regulatory monitor observations. Neither suggested API fits this measured-data request under the stated authority. [OpenAQ access](https://docs.openaq.org/using-the-api/quick-start), [retired versions](https://docs.openaq.org/about/about), [Open-Meteo sources](https://open-meteo.com/en/docs/air-quality-api)

A defensible comparison is **descriptive change at the same monitoring sites**, subject to adequate coverage and comparable methods. It cannot establish neighborhood-wide exposure, a policy effect or regulatory attainment from two years alone.

Reproducible acquisition plan:

1. Define the neighborhood boundary and site-selection rule before viewing results. Start with Illinois/Cook County candidates, then verify addresses, coordinates, monitoring objectives, regulatory classification and methods. Cook County and the Chicago metropolitan area extend beyond Chicago neighborhoods. Record site IDs and choose sites operating in both years.
2. In the EPA form, select PM2.5, 2023, Illinois (or IL–Cook), and **one site**. Repeat for 2024 and every selected site. Record all form choices and retrieval dates. EPA’s generated CSV link expires after ten minutes, so reproduce the query rather than preserving that link as the sole acquisition instruction.
3. Copy each fresh CSV link and download with a strict cap, for example:
   `curl --fail --location --max-filesize 1048575 --output site-year.csv 'FRESH_CSV_URL'`
   Retain only successful downloads smaller than 1 MiB; discard partial failed transfers. This enforces the limit even if a response’s size is unknown. Start with site-year requests; if one exceeds the cap, stop and use a verified smaller date-filtered export route before proceeding. Do not download national archives: EPA lists the 2023/2024 daily 88101 ZIPs at approximately 9.7/8.2 MB. [Archive sizes](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
4. Inspect the returned schema and source labels. Restrict to regulatory-method PM2.5 (88101, FRM/FEM: federal reference/equivalent methods), or explicitly document any alternative. Check the public PM2.5 export’s actual parameter coverage rather than assuming every row is 88101.
5. Keep one comparable daily mean per selected monitor/day. Audit duplicate standards, sampling durations and event variants; never average all duplicate rows. Preserve monitor occurrence IDs and method changes. Use local-standard calendar days and consistent units. Include exceptional-event measurements for the primary “what was measured” comparison; optionally report an explicitly labeled exclusion sensitivity analysis. [EPA field definitions](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html)
6. Report valid-day counts, monthly coverage, sampling schedule and missingness by site/year. Do not fill gaps with zero. Compare site-specific distributions and means with seasonal coverage checks; show matched-calendar-day sensitivity where available, handling February 29 separately. Avoid pooling changing site mixtures.

Documented schema example, **not an observed Chicago row**:

```text
State Code | County Code | Site Num | Parameter Code | POC
Sample Duration | Pollutant Standard | Date Local
Units of Measure | Event Type | Observation Count
Observation Percent | Arithmetic Mean | Method Code | Method Name
```

These are EPA national daily-file fields; the public form’s CSV may differ. Full CSV retrieval was unavailable here, so no measured values, coverage results or year-to-year conclusion are claimed.