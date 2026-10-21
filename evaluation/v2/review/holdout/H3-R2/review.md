# Independent blind review: H3-R2

Preference: **amber_material**.

Amber wins materially on the bounded task because its unchanged code generates a printable SVG and companion ledger with only Python, while teal requires a manual QGIS workflow. Both code fences compile and passed a small synthetic fixture test. This is not proof that either live API recipe succeeds. Teal is stronger on provenance and explicit license screening. Amber's map uses equally scaled degree axes, so it is an approximate overview with geographic distortion; its cells are correctly described as roughly 0.9 by 1.1 km, and it explicitly disclaims navigation. Amber should preserve richer attribution and acquisition metadata, and floating-point floor operations can assign exact grid-edge points to an adjacent cell. These are limited map-quality/provenance weaknesses, not a critical feasibility failure. Native starter-species scope and false-absence/access warnings are supported. No protected coordinates were reconstructed.

## Scores

Rubric order: claim support; constraints/feasibility; breadth/material alternative; decisive source inspection; artifact/actionability; falsifiable verification/uncertainty.

- amber: [4, 4, 3, 4, 4, 3], total 22/24. Consequential errors: none established.

- teal: [4, 4, 3, 4, 3, 4], total 22/24. Consequential errors: none established.

## Independently checked useful differences

**amber: Offers a standard-library route that actually generates a printable map, rather than requiring a separate GIS workflow.**

With a synthetic documented-shape response, execution wrote parseable map.svg and records.csv, collapsed a duplicate occurrenceID, and excluded a generalized record. This removes several GIS setup/import/grid/layout operations for the small public-learning task. This is a material operating-work benefit, not live record verification.

Source: Local offline execution of unchanged Python fence in amber/answer.md; GBIF parameter documentation https://gbif.github.io/gbif-api/apidocs/org/gbif/api/model/occurrence/search/OccurrenceSearchParameter.html. Location: Python fence URL/query, uncertainty/generalization screening, SVG writer; docs HAS_GEOSPATIAL_ISSUE and MEDIA_TYPE.

**teal: Preserves raw response provenance and applies explicit downstream privacy, photo, license and accuracy screening.**

Fixture run retained the valid observation, rejected unknown accuracy and obscured records, wrote bees.csv and response-1.json. The saved query/body makes later auditing easier than amber's link-only CSV; a useful offset but does not itself produce a map.

Source: Local offline execution of unchanged Python fence in teal/answer.md; official API source https://raw.githubusercontent.com/inaturalist/iNaturalistAPI/main/lib/views/swagger_v1.yml.ejs. Location: Python fence response-page JSON saving, rows keyed by ID, rejection predicate.

## Access and verification limits

Live API reads failed independently through both web and local urllib: web reported inaccessible URLs; urllib reported Errno 8 DNS resolution failures. This corroborates present environment limitations, not an exact historical tool trace or worldwide API outage.

No live regional harvest, QGIS execution, PDF rendering, scheduler, literature recall or deduplication accuracy measurement was possible. Recommendations and synthetic fixture checks are distinct from successful real-data operation.

Only assigned packets and protocol were inspected. Original answers and evidence were preserved. No accounts, installs, credentials, remote writes, other reviews or arm identity information were used.

The official legacy iNaturalist response at https://www.inaturalist.org/api, GET observations Example Response lines 123-170, confirms wolf ID 2281, casual status, 354-metre accuracy, null license, false coordinates_obscured and empty photos. This is a valid documented rejection fixture, not an in-scope observation. The GBIF taxonomy-interpretation documentation independently confirms key 5104646682 and its human-observation/present structure; neither establishes a local bee record.

Official current API source confirms native/photo/date/radius/privacy/license filters; official geoprivacy documentation confirms obscured points are displaced. A synthetic fixture is not source data and tests only the selected code paths.
