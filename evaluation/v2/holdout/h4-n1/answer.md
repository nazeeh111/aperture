Use **Crossref as the main metadata and integrity source, OpenAlex as a supplementary discovery source, and OSTI plus DataCite to find material a journal DOI search misses**. Keep a local ledger and run it monthly with standard-library Python or curl; no account, installation or paid service is needed.

As checked on October 21, 2026, OpenAlex’s current documentation permits basic anonymous queries. A key is required for cursor paging beyond its first page; basic paging has a 10,000-result ceiling. Use narrow date windows, record returned counts and stop with an explicit incomplete-search warning if limits prevent completion. Older claims that every request requires a key are stale. [OpenAlex authentication](https://help.openalex.org/api/authentication/)

1. **Discover broadly.** Search separate phrases: “direct air capture,” “direct atmospheric carbon capture,” and atmospheric CO2 removal paired with sorbent, solvent, electrochemical, regeneration or contactor. Screen out flue-gas capture and unrelated acronym matches. Search titles/abstracts, then follow relevant references and research groups. Add [OSTI](https://www.osti.gov/api/v1/docs) for DOE-funded reports and other research outputs, and [DataCite](https://support.datacite.org/docs/api) for repository datasets, software and preprints. Record source-specific coverage; these additions reduce gaps without promising exhaustive coverage.

2. **Separate new evidence from newly indexed evidence.** Store publication date, first-seen date and source update date separately. Each monthly run overlaps the previous checkpoint by seven days and advances it only after all pages succeed. Crossref’s `from-index-date` includes third-party changes, whereas publication-date filtering alone misses updates to old papers. Reconcile the full query periodically for late indexing and changed search terms. [Crossref synchronization](https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/)

3. **Group versions without deleting provenance.** Normalize DOI case and remove DOI URL prefixes. Merge identical identifiers; link preprint, accepted manuscript and published versions using explicit relations. Crossref supplies preprint/version relations; DataCite supplies `IsVersionOf`, `IsNewVersionOf` and related links. Keep each version’s identifiers and dates under one evidence-family entry. Title/author similarity only nominates a manual match: datasets and supplements remain distinct supporting objects. [Crossref relations](https://www.crossref.org/documentation/schema-library/markup-guide-metadata-segments/relationships/), [DataCite versioning](https://support.datacite.org/docs/versioning)

4. **Recheck every retained family monthly, including old work.** Inspect Crossref `update-to` and query notices with `filter=updates:DOI`; follow notices and publisher/Crossmark status pages. Deduplicate notices by target, notice DOI and type while retaining publisher/Retraction Watch provenance. Crossref integrates Retraction Watch, but corrections and expressions of concern are less comprehensive than retractions. Missing metadata means “no notice found in checked sources,” never “clean.” Preserve retracted entries with prominent warnings; explain how corrections affect earlier digest conclusions. [Update filters](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/), [Retraction Watch coverage](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/)

5. **Write an evidence digest.** For each selected family give the finding, experimental versus modeled evidence, capture conditions, energy and cost assumptions, uncertainty, accessible source links and status-check date. Include sections for changed conclusions and unresolved matches, plus query windows, source counts and failures.

Use small metadata pages and a streaming byte cap of **1,048,575 bytes per response file**; abort and reduce page size if exceeded. Avoid bulk snapshots and PDFs.

**Verification limit:** documentation was inspected; live API requests were unavailable here because shell DNS failed. The following is reproducible documentation-backed syntax, not a successfully executed harvest.

Compact example, adapting Crossref’s documented update schema (illustrative DOI, not a DAC correction):
```xml
<updates>
  <update type="correction" date="2012-05-12">10.5555/12345681</update>
</updates>
```

Example GETs, with no key:
```text
https://api.crossref.org/works?query=direct%20air%20capture&filter=from-index-date:2026-10-01,until-index-date:2026-10-21&rows=5
https://api.crossref.org/works?filter=updates:10.1016/j.joule.2018.05.006&rows=5
```
