# Independent blind review: H4-R1

Preference: **teal_slight**.

Teal has a slight lead from its directly reproducible substantive correction fixture and explicit separate study/notice tables. Amber's illustrative XML exactly matches the official Crossref relationship example and meets the brief's schema option; it is not fabricated evidence. Its DataCite path is a useful addition absent from teal. Both correctly use index dates, whole-ledger integrity checks, conservative version grouping, small-response size limits and conditional OpenAlex enrichment. No critical error found. No successful API harvest or running digest was claimed.

## Scores

Rubric order: claim support; constraints/feasibility; breadth/material alternative; decisive source inspection; artifact/actionability; falsifiable verification/uncertainty.

- amber: [4, 4, 4, 3, 3, 4], total 22/24. Consequential errors: none established.

- teal: [4, 4, 3, 4, 4, 4], total 23/24. Consequential errors: none established.

## Independently checked useful differences

**amber: Adds DataCite version relationships and discovery beyond Crossref/OSTI.**

Official documentation supports IsVersionOf/HasVersion and IsNewVersionOf. This gives a concrete route to recognize repository/preprint versions that Crossref relationships alone may miss; no actual additional DAC item was demonstrated.

Source: https://support.datacite.org/docs/connecting-versions-with-related-identifiers. Location: Release or publication stages; canonical version and sequential version examples.

**teal: Provides an independently verifiable real correction fixture with the affected study, location, numeric change and notice date.**

The publisher confirms the example. A reader can validate a notice ledger against a substantive changed estimate rather than only a generic XML schema. Amber's XML is also a legitimate documented schema, so this earns a slight rather than material preference.

Source: https://www.nature.com/articles/s43247-024-01384-w. Location: Published date line 19; correction target/paragraph lines 43-44.

## Access and verification limits

Live API reads failed independently through both web and local urllib: web reported inaccessible URLs; urllib reported Errno 8 DNS resolution failures. This corroborates present environment limitations, not an exact historical tool trace or worldwide API outage.

No live regional harvest, QGIS execution, PDF rendering, scheduler, literature recall or deduplication accuracy measurement was possible. Recommendations and synthetic fixture checks are distinct from successful real-data operation.

Only assigned packets and protocol were inspected. Original answers and evidence were preserved. No accounts, installs, credentials, remote writes, other reviews or arm identity information were used.

Primary checks: https://help.openalex.org/api/authentication/ supports basic anonymous access and the cursor key boundary. https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/ documents from-index-date and updates (relationship-filter table). https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/ lines 117-125 documents working-day updates, source provenance and weaker corrections/concerns coverage. OSTI direct documentation timed out but its official indexed documentation supports DOE repository scope and q/entry-date/rows/page parameters.

The illustrative correction XML in H4-R1 amber matches https://www.crossref.org/documentation/schema-library/markup-guide-metadata-segments/relationships/ at the updates block. Publisher correction values, DOI target and April 18 2024 date were directly inspected. The fixture is normalized publisher evidence, not an API response.
