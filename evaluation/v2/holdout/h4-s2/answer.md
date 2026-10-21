Use **Crossref for discovery and update tracking, OpenAlex for additional discovery and version links, and OSTI for DOE reports**. Keep a local ledger of research families and a separate ledger of corrections. This can run monthly without accounts or keys, but cannot guarantee that every correction is indexed.

1. **Discover with overlapping windows.** On the first of each month, search the preceding two months for “direct air capture,” “direct air carbon capture,” and “capture from ambient air.” Screen out flue-gas-only studies. Separate newly published research from older research newly discovered. In Crossref, use `from-index-date` rather than publication date alone: it includes reindexing changes from publishers, Crossref and external sources. Record publication, indexing and retrieval dates separately. [Crossref filters](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/)

2. **Broaden the evidence types.** Search [OSTI’s public repository API](https://www.osti.gov/api/v1/docs), using `q`, `entry_date_start`, `entry_date_end`, `rows` and `page`, for reports and manuscripts beyond journal articles. Follow relevant papers’ references and recent citing works; check the public publication pages of recurring laboratories. Treat these as candidate discovery, followed by relevance screening. Avoid “DAC” alone, which is ambiguous.

3. **Respect keyless limits.** OpenAlex’s documentation, updated October 15, 2026, permits basic keyless queries but requires a key for cursor paging beyond its first page. Use small date slices and ordinary paging within documented limits; check total counts and explicitly report truncation or budget errors. If necessary, defer OpenAlex enrichment and complete Crossref discovery rather than create an account. [Authentication and limits](https://help.openalex.org/api/authentication/)

4. **Group versions without erasing evidence.** Normalize DOI URLs to lowercase bare identifiers for exact matching. Then inspect explicit Crossref preprint/version relations and OpenAlex `locations`, retaining every identifier and version. OpenAlex can associate several DOIs with one work, but acknowledges matching errors. Similar titles and overlapping authors should trigger manual comparison, not automatic merging. Publish one entry per research family, label preprints, and describe substantive version changes. Corrections remain linked events, never duplicate papers. [OpenAlex DOI handling](https://help.openalex.org/data/works/dois/)

5. **Recheck the entire retained bibliography monthly.** For each DOI, inspect Crossref `updated-by`, notices’ `update-to`, and the `updates:DOI` filter; preserve notice type, date, source and target. Check publisher landing pages/Crossmark and search the exact title with correction, corrigendum, erratum, retraction and expression of concern. Crossref incorporates Retraction Watch, updated every working day, but corrections and concern notices are less comprehensive than retractions. An empty response means “no indexed notice found,” not “verified clean.” Do not download the full Retraction Watch CSV under the file-size limit. [Update metadata](https://crossref.org/documentation/register-maintain-records/maintaining-your-metadata/registering-updates/), [coverage limits](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/)

6. **Write an evidence digest.** Each selected family gets its question, method, principal result with conditions, important limitation, accessible source, version and status-check date. Put status changes first. Keep unread papers as discovery entries, without inferred findings. Save query parameters, completion counts, exclusions and access failures locally. Request small metadata pages; enforce a streaming limit below 1 MiB per file, and skip oversized full texts.

A real correction shows why this matters: the publisher reports changing a figure’s estimate from −0.033 to −0.006, with standard error 0.007 unchanged. Its publication date is **April 18, 2024**, whereas Duke’s secondary record lists December 1. Prefer the [publisher’s notice](https://www.nature.com/articles/s43247-024-01384-w) over the [secondary date](https://scholars.duke.edu/publication/1631642).

Compact example: proposed local schema, manually populated from that notice; **not a live API response**. Reproduce by opening `source_url` and comparing the correction text and publication date:

```json
{
  "family_id": "doi:10.1038/s43247-024-01334-6",
  "event": "author-correction",
  "notice_doi": "10.1038/s43247-024-01384-w",
  "notice_published": "2024-04-18",
  "source_url": "https://www.nature.com/articles/s43247-024-01384-w",
  "checked_on": "2026-10-21",
  "verified_location": "Correction text; About this article",
  "crossref_relationship_verified": false,
  "claim": {"figure": 2, "estimate_before": -0.033,
            "estimate_after": -0.006, "standard_error": 0.007}
}
```

Live API execution was unavailable here: local requests failed DNS resolution and browser API requests were inaccessible. The workflow is documentation-backed; the example’s content was checked on the publisher page.
