Use a local monthly ledger combining Crossref, small anonymous OpenAlex searches, and direct preprint/repository checks. Make each digest item a **study with linked versions and status**, rather than a DOI entry. This is feasible without accounts; exhaustive discovery or correction coverage is not guaranteed.

1. **Discover broadly.** Maintain separate searches for “direct air capture”, “direct atmospheric CO2 capture”, and ambient-air carbon capture with sorbent, electrochemical, humidity and process terms. Screen out flue-gas-only work. Use Crossref for registered publications; OpenAlex for additional locations and citation leads. Add arXiv and DataCite/repository searches for preprints, datasets and software. Follow references from a few relevant reviews and check their publishers’ recent contents to find vocabulary missed by keywords. [Crossref public access](https://www.crossref.org/documentation/retrieve-metadata/rest-api), [DataCite queries](https://support.datacite.org/docs/api-queries).

2. **Run two monthly passes.** First, discover newly published work with a rolling 90-day overlap for late indexing. Second, refresh every previously included study, regardless of publication year. For Crossref incremental metadata, use `from-index-date` through the run cutoff, overlapping the previous checkpoint by seven days; it includes changes from Crossref and outside sources. Save publication date, first-seen date and last-checked date separately. Advance the checkpoint only after all pages succeed; periodically rerun a broader historical search. [Date semantics](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/).

3. **Keep keyless access bounded.** OpenAlex currently documents anonymous basic queries, but cursor paging beyond its first page requires a key. Use ordinary pages and narrower monthly/topic partitions; record any truncation. Do not silently claim completeness when a limit or access error occurs. Cache results, retry 429 responses with backoff, and stop at the free anonymous limit. Use small metadata pages, abort a response before 1 MiB, and reduce page size if oversized. Avoid bulk datasets and PDFs. [Current authentication rules](https://help.openalex.org/api/authentication/).

4. **Resolve versions conservatively.** Normalize DOI URLs/case, retain arXiv base ID plus version, and use explicit Crossref relations or DataCite `IsVersionOf/HasVersion` links to group records. Title, author and year similarity should generate a human-review candidate, never an automatic merge. Keep distinct experiments separate. Prefer the journal version for citation while retaining the preprint and its revision history. [Version relationships](https://support.datacite.org/docs/connecting-versions-with-related-identifiers).

5. **Check integrity independently of keywords.** For every retained Crossref DOI, fetch its record and query `/works?filter=updates:DOI&rows=20`, paging as necessary. Inspect update relationships, notice type, date and source; follow the publisher/Crossmark notice before interpreting it. A correction titled simply “Correction” can escape topical searches. Crossref incorporates Retraction Watch, including a `source` marker; corrections and expressions of concern have less complete coverage than retractions. Missing metadata means “no notice found as of [date]”, not “verified clean”. Recheck non-Crossref works on their repository/publisher pages. [Integrity data and limitations](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/).

6. **Produce an evidence digest.** Start with corrections/retractions affecting earlier digests, then new studies, then changed versions. Give each study one short finding, evidence type, key limitation, version/status, links and check date. Preserve exclusions and unresolved duplicate candidates.

A reproducible real example is [Open DAC 2023](https://arxiv.org/abs/2311.00341): its landing page lists v1 and v2, plus a DataCite-issued DOI. These are one work’s versions, not two discoveries. The following is a local schema projection, not a claimed API response:

```json
{
  "study_id": "arxiv:2311.00341",
  "title": "The Open DAC 2023 Dataset and Challenges for Sorbent Discovery in Direct Air Capture",
  "doi": "10.48550/arXiv.2311.00341",
  "versions": [
    {"id": "2311.00341v1", "date": "2023-11-01"},
    {"id": "2311.00341v2", "date": "2023-11-27"}
  ],
  "status": "not assessed",
  "source": "https://arxiv.org/abs/2311.00341"
}
```

Verification limit: the landing page and official documentation were readable; both API test requests failed through this environment. The workflow is recommended, not an executed monthly harvest.
