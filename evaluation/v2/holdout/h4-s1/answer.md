Use **Crossref as the backbone, OpenAlex as optional enrichment, and publisher pages as the final status check**. A monthly DOI search alone cannot meet the goal: old papers receive new corrections, and different DOIs can represent one study.

Crossref needs no account or key. Current OpenAlex documentation permits basic keyless queries but requires a key for cursor paging beyond its first page. Older announcements describe different limits; therefore, do not make OpenAlex completeness a dependency. Its API could not be tested here. [Crossref access](https://www.crossref.org/documentation/retrieve-metadata/rest-api/), [current OpenAlex authentication](https://help.openalex.org/api/authentication/).

1. **Keep a local study ledger.** Store study ID, every DOI/repository ID, title/authors, version, first-seen and publication dates, sources, status checks and unresolved matches. Keep a separate notice table pointing to affected studies. One digest entry per study, with links to its versions.

2. **Discover monthly, using overlapping windows.** Start with “direct air capture”, “direct atmospheric carbon capture”, and “CO2 capture from ambient air”; screen out flue-gas capture. Query Crossref using `from-index-date` and `until-index-date`, initially covering the previous month plus seven days. Index dates include external metadata changes; publication dates do not. Follow pagination, save the last completed window, and retry unfinished windows before advancing it. Label newly discovered older work separately. [Date semantics](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/).

   Add a small **OSTI** search for DOE-funded technical reports and research outputs that a journal-centric search can miss. Follow useful references and repository links from selected papers. This adds a different publication channel, not another supposedly independent vote for the same result. [OSTI API scope](https://www.osti.gov/api/v1/docs).

3. **Resolve versions conservatively.** Normalize DOI prefixes/case; exact DOI matches merge automatically. Follow Crossref `is-preprint-of` and other explicit version relations. Use similar titles plus authors only to flag manual review: do not automatically merge experiments with similar titles. Preserve distinct version IDs and changes; prefer the corrected journal version for citation without hiding the preprint. Missing relations remain unresolved. [Crossref preprint relations](https://www.crossref.org/documentation/schema-library/markup-guide-record-types/posted-content-includes-preprints/).

4. **Monitor the entire ledger, not just new search hits.** Each month retrieve every tracked Crossref DOI and search `/works?filter=updates:DOI`; inspect `relation`, `update-to`, notice type/source, and linked notices. Check publisher/Crossmark pages before discussing an item. Include corrections, retractions, expressions of concern and reinstatements as status changes, never duplicate “new studies”. Crossref incorporates Retraction Watch, but that is shared provenance, not independent corroboration; corrections and concerns are less comprehensive than retractions. Absence of a notice means “none found in checked sources”, not “verified clean”. [Update filters](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/), [coverage limits](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/).

5. **Publish a local draft for the meeting.** Separate new studies, new versions and status changes. Summarize mechanism, tested conditions, findings, limitations and relevance. Record failed queries and coverage gaps. Use existing Python standard-library HTTP/JSON support; request small metadata pages, reject responses reaching 1,048,576 bytes, and split oversized requests. Skip bulk datasets and PDFs unless their size is safely bounded. No installs or accounts are needed.

A real test fixture is below: the publisher’s correction changes a plotted estimate, demonstrating why notices affect evidence rather than merely bibliography. It is historical, not this month’s discovery. [Original correction, published 18 April 2024](https://www.nature.com/articles/s43247-024-01384-w).

**Limit:** API calls failed here; the schema is manually normalized from the publisher, not a captured API response. No complete monthly harvest or deduplication run was executed.

```json
{
  "study_id": "doi:10.1038/s43247-024-01334-6",
  "notice_doi": "10.1038/s43247-024-01384-w",
  "notice_type": "author_correction",
  "notice_published": "2024-04-18",
  "affected_location": "Figure 2, high benefits estimate",
  "before": -0.033,
  "after": -0.006,
  "standard_error_before_and_after": 0.007,
  "publisher_reports": "HTML and PDF corrected",
  "verification": "publisher HTML inspected; API unavailable",
  "source": "https://www.nature.com/articles/s43247-024-01384-w"
}
```

Reproduce the record by opening the source and checking its correction paragraph and publication date. For an API cross-check, GET `https://api.crossref.org/works/10.1038/s43247-024-01384-w`; verify rather than assume its update fields.
