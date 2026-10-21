Use **iNaturalist’s public read API → CSV → free QGIS → downloadable PDF**, with a separate CSV of observation links. This avoids account creation and uploads. GBIF’s bulk-download endpoint requires registration and authentication, so it adds unnecessary friction here. [GBIF documentation](https://techdocs.gbif.org/en/openapi/v1/occurrence)

Make a learning map, not a bee census or walking-direction map. Define “near” as a 20 km radius around central Blacksburg (37.2296, −80.4139); this is a proposed scope, not a surveyed boundary.

1. Fetch photographed bees using the example below. It selects research-grade, publicly open observations through October 21, 2026, with source-listed native status. **Native is a place-dependent checklist assertion:** absence of an introduced label does not establish nativeness. Review each returned species’ Virginia status before retaining it; put unresolved IDs/status in a separate review list. Also run the query without `native=true` to see what that filter omitted, without treating omitted taxa as nonnative. [Establishment means](https://help.inaturalist.org/en/support/solutions/articles/151000176171-how-to-add-or-edit-establishment-means-in-inaturalist), [filter semantics](https://forum.inaturalist.org/t/how-to-use-inaturalists-search-urls-wiki-part-1-of-2/63)

2. Keep the public observation ID, species, observation date, public coordinates, positional accuracy, observation license, and observation URL. Require photos, finite coordinates, neither privacy field obscured/private, and a known accuracy radius ≤100 m for the point layer. Keep missing/coarser accuracy records separately, counted as “excluded from precise map,” rather than silently dropping them. A 100 m threshold is an editorial choice. Never infer hidden locations from photos, nearby observations or observer history. iNaturalist distinguishes observer and taxon privacy. [Official search guidance](https://help.inaturalist.org/en/support/solutions/articles/151000170738)

3. Use observation data licensed CC0 or CC BY for straightforward redistribution; preserve contributor attribution for CC BY. Photos have separate licenses. Link to original observation pages instead of copying photos into the PDF. Research grade supports screening, not guaranteed identification. Check retained photographs against regional identification guidance; Virginia Tech describes local native bee groups. [API license fields](https://raw.githubusercontent.com/inaturalist/iNaturalistAPI/main/lib/views/swagger_v1.yml.ejs), [Virginia Tech guide](https://www.pubs.ext.vt.edu/ENTO/ENTO-151/ENTO-151.html)

4. In QGIS, import the cleaned CSV as delimited text: X=longitude, Y=latitude, coordinate system EPSG:4326. Label points by a short ID matching the linked CSV. Prefer 1 km grid counts for the public handout, with the caption “photographed observations in retained records,” rather than implying nest locations. Add a scale, date range, query/retrieval date, exclusions, and legend. Export a Print Layout as PDF and retain the QGIS project and cleaned CSV. A basemap is optional; if used, retain its required attribution. [CSV import](https://docs.qgis.org/3.44/en/docs/user_manual/managing_data_source/supported_data.html), [PDF export](https://docs.qgis.org/3.44/en/docs/user_manual/print_composer/create_output.html)

Blank areas mean **no retained records**, never “no bees.” Photography, identification, privacy, season and observer effort affect coverage. Historical records do not promise bees this weekend or establish public access. Select the actual walk independently using established public paths.

**Verification limit:** live occurrence requests were inaccessible here; no local count, bee record, CSV or rendered map is claimed. The official legacy API provides this documented response excerpt, useful for testing rejection: it is a gray wolf without photos, not a local bee. [Documented example](https://www.inaturalist.org/api)

```json
{"id":2281,"species_guess":"gray wolf","photos":[],
 "positional_accuracy":354,"license":null,"coordinates_obscured":false}
```

Compact reproducible request and extraction (Python standard library; run locally, then apply the review/cleaning rules above):
```python
import csv,json,time,urllib.parse,urllib.request
p=dict(taxon_id=630955,lat=37.2296,lng=-80.4139,radius=20,
       photos="true",geo="true",native="true",quality_grade="research",
       geoprivacy="open",taxon_geoprivacy="open",
       license="cc0,cc-by",d2="2026-10-21",per_page=200,
       order_by="id",order="asc")
rows=[]; page=1
while True:
    if page>50: raise RuntimeError("Split date window; do not map partial results")
    p["page"]=page
    u="https://api.inaturalist.org/v1/observations?"+urllib.parse.urlencode(p)
    with urllib.request.urlopen(u,timeout=30) as r: d=json.load(r)
    batch=d["results"]
    if not batch: break
    for o in batch:
        loc=(o.get("location") or ",").split(",")
        rows.append([o["id"],o.get("taxon",{}).get("name"),
          o.get("observed_on"),loc[-1],loc[0],o.get("positional_accuracy"),
          o.get("geoprivacy"),o.get("taxon_geoprivacy"),
          o.get("license_code"),o.get("user",{}).get("login"),
          len(o.get("photos",[])),o.get("uri")])
    if len(batch)<200: break
    page+=1; time.sleep(1)
with open("bee_candidates.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["id","species","date","longitude","latitude",
      "accuracy_m","privacy","taxon_privacy","license","observer","photos","url"])
    w.writerows(rows)
```
