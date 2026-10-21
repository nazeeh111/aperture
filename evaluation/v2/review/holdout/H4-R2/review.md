# Independent blind review: H4-R2

Preference: **tie**.

Tie on practical usefulness. Amber supplies a verified correction/date-conflict fixture and concrete OSTI parameter names; teal supplies a verified version fixture and explicit DataCite relationships plus a completion checkpoint. Neither demonstrated extra relevant monthly discoveries or operational recall. The higher teal total reflects somewhat stronger explicit version/discovery machinery, not a checked material advantage over amber's different useful fixture. Amber's updated-by wording should not be copied as a guaranteed REST JSON field: its cited source describes Crossmark internal metadata as updated_by; the stable independently documented REST approach is the notices' update-to and updates:DOI query. Both include the latter, so this imprecision does not defeat the workflow. No critical error found.

## Scores

Rubric order: claim support; constraints/feasibility; breadth/material alternative; decisive source inspection; artifact/actionability; falsifiable verification/uncertainty.

- amber: [3, 4, 3, 4, 3, 4], total 21/24. Consequential errors: none established.

- teal: [4, 4, 4, 4, 3, 4], total 23/24. Consequential errors: none established.

## Independently checked useful differences

**amber: Uses a real correction and resolves conflicting notice dates against the publisher.**

Both source dates were independently checked. This prevents a bad notice date from entering a monthly ledger and gives a real integrity fixture; teal instead provides a real version fixture.

Source: https://www.nature.com/articles/s43247-024-01384-w ; https://scholars.duke.edu/publication/1631642. Location: Publisher date/correction paragraph lines 19,43-44; Duke publication date line 19.

**teal: Provides a real two-version preprint fixture and a documented DataCite linking route.**

The arXiv title, DOI and November 1/27 2023 version dates are correct. Keeping arXiv base ID plus v1/v2 enables one-family digest grouping, and DataCite links cover release stages outside Crossref.

Source: https://arxiv.org/abs/2311.00341 ; https://support.datacite.org/docs/connecting-versions-with-related-identifiers. Location: arXiv submission history lines 8,23,27-28; DataCite Release or publication stages.

## Access and verification limits

Live API reads failed independently through both web and local urllib: web reported inaccessible URLs; urllib reported Errno 8 DNS resolution failures. This corroborates present environment limitations, not an exact historical tool trace or worldwide API outage.

No live regional harvest, QGIS execution, PDF rendering, scheduler, literature recall or deduplication accuracy measurement was possible. Recommendations and synthetic fixture checks are distinct from successful real-data operation.

Only assigned packets and protocol were inspected. Original answers and evidence were preserved. No accounts, installs, credentials, remote writes, other reviews or arm identity information were used.

Primary checks: https://help.openalex.org/api/authentication/ supports basic anonymous access and the cursor key boundary. https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/ documents from-index-date and updates (relationship-filter table). https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/ lines 117-125 documents working-day updates, source provenance and weaker corrections/concerns coverage. OSTI direct documentation timed out but its official indexed documentation supports DOE repository scope and q/entry-date/rows/page parameters.

The illustrative correction XML in H4-R1 amber matches https://www.crossref.org/documentation/schema-library/markup-guide-metadata-segments/relationships/ at the updates block. Publisher correction values, DOI target and April 18 2024 date were directly inspected. The fixture is normalized publisher evidence, not an API response.
