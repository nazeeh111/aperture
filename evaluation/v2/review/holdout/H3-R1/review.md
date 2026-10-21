# Independent blind review: H3-R1

Preference: **amber_slight**.

Amber has a small practical lead from the executable candidate exporter and stronger direct API parameter inspection. Teal has a useful native-species starter scope, explicit latitude/longitude parsing and projected accuracy circles. Both meet the documented-example option through a real official legacy example, explicitly rejecting the wolf as nonlocal and non-bee. Neither produced a map or a local bee record. Amber's code does not enforce its prose precision/photo/privacy screening; this is not silently misrepresented because it writes bee_candidates.csv and explicitly requires subsequent review/cleaning. Teal leaves CSV construction manual and does not give an explicit redistribution license allowlist. No critical error found.

## Scores

Rubric order: claim support; constraints/feasibility; breadth/material alternative; decisive source inspection; artifact/actionability; falsifiable verification/uncertainty.

- amber: [4, 4, 3, 4, 3, 4], total 22/24. Consequential errors: none established.

- teal: [3, 4, 3, 3, 3, 4], total 20/24. Consequential errors: none established.

## Independently checked useful differences

**amber: Provides working candidate CSV extraction with bounded pagination and contributor/license columns.**

Reduces manual JSON-to-CSV work. Fixture execution created the expected columns and longitude/latitude order. It deliberately remains a candidate exporter; manual screening remains required.

Source: Local offline execution of unchanged Python fence in amber/answer.md; official iNaturalist API source https://raw.githubusercontent.com/inaturalist/iNaturalistAPI/main/lib/views/swagger_v1.yml.ejs. Location: Python fence; API license enum lines 2306-2320, privacy lines 2598-2636.

**teal: Names a bounded two-species starter scope instead of leaving every species native-status determination to the reader.**

The Virginia source explicitly includes Xylocopa virginica among native bees and the eastern guide supports Bombus impatiens identification/range. This is a useful modest reduction of checklist review; not proof of local occurrences or complete coverage.

Source: https://ext.vt.edu/content/dam/pubs_ext_vt_edu/ENTO/ENTO-151/ENTO-424.pdf ; https://www.xerces.org/sites/default/files/2018-05/12-052_01_Eastern_Bumble_Bee.pdf. Location: Virginia publication introduction/carpenter bees, PDF page 1; eastern guide Bombus impatiens species section pages 14-17.

## Access and verification limits

Live API reads failed independently through both web and local urllib: web reported inaccessible URLs; urllib reported Errno 8 DNS resolution failures. This corroborates present environment limitations, not an exact historical tool trace or worldwide API outage.

No live regional harvest, QGIS execution, PDF rendering, scheduler, literature recall or deduplication accuracy measurement was possible. Recommendations and synthetic fixture checks are distinct from successful real-data operation.

Only assigned packets and protocol were inspected. Original answers and evidence were preserved. No accounts, installs, credentials, remote writes, other reviews or arm identity information were used.

The official legacy iNaturalist response at https://www.inaturalist.org/api, GET observations Example Response lines 123-170, confirms wolf ID 2281, casual status, 354-metre accuracy, null license, false coordinates_obscured and empty photos. This is a valid documented rejection fixture, not an in-scope observation. The GBIF taxonomy-interpretation documentation independently confirms key 5104646682 and its human-observation/present structure; neither establishes a local bee record.

Official current API source confirms native/photo/date/radius/privacy/license filters; official geoprivacy documentation confirms obscured points are displaced. A synthetic fixture is not source data and tests only the selected code paths.
