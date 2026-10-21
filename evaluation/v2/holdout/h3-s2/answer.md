Use **iNaturalist public reads → a local CSV → a QGIS PDF**, with **occupied 1 km squares**, rather than apparent bee hotspots or precise destinations. This is a documented, account-free approach; I could not verify a live Blacksburg API response here, and have not produced a populated map.

Choose an explicit planning area: **20 km around 37.2296, −80.4139**, and observations dated **2021-01-01 through 2026-10-21**. These are proposed boundaries, not a claim about walkable access.

1. Request photographed, research-grade **Anthophila (bees)** with `native=true`, public coordinates, and both observer and taxon geoprivacy open. The [official API search source](https://github.com/inaturalist/iNaturalistAPI/blob/main/lib/views/_observation_search_params_v1.yml.ejs) supports these filters. Native status is checklist-based: **`introduced=false` also includes unknown status**, whereas `native=true` selects native/endemic. A missing native flag therefore excludes potentially native species; label the output “iNaturalist observations flagged native,” not a complete native-bee inventory. [Filter definitions](https://help.inaturalist.org/en/support/solutions/articles/151000170738).

2. Retain observation ID, species, date, positional accuracy, observer credit, licence and observation link. Restrict redistributed observation data to CC0/CC BY; link to photographs on their observation pages instead of copying them. Photos have separate licences. The [iNaturalist developer page](https://www.inaturalist.org/pages/developers) explains its licensed datasets; [GBIF documents separate image rights](https://techdocs.gbif.org/en/openapi/images).

3. Reject obscured/private records, missing coordinates, and unknown or greater-than-100-metre positional accuracy. This conservative accuracy threshold is a design choice. Never infer hidden locations from nearby records, photos or dates. Obscured coordinates are deliberately displaced; they are unsuitable walk stops. [Official geoprivacy explanation](https://help.inaturalist.org/en/support/solutions/articles/151000169938-what-is-geoprivacy-what-does-it-mean-for-an-observation-to-be-obscured-).

4. In free QGIS, **Add Delimited Text Layer**: X=`longitude`, Y=`latitude`, coordinate system **EPSG:4326**. Reproject to **EPSG:26917**, create a 1,000-metre rectangular polygon grid covering the points, then use **Count points in polygon**. Display only occupied squares in one colour. Keep the detailed CSV locally; distribute the coarse PDF with a species/date/credit/link table. QGIS documents [CSV import](https://docs.qgis.org/3.44/en/docs/user_manual/managing_data_source/opening_data.html) and [PDF export](https://doc.qgis.org/3.44/en/docs/user_manual/print_layout/create_output.html). Include title, extent, scale, retrieval date and exclusions.

Print this legend: **“Photographed observations, not bee abundance. Blank areas mean no qualifying records in this extract, not no bees. Past sightings do not guarantee bees this weekend. Squares do not establish public access.”** Choose the actual walk independently using established public paths; this map supplies learning examples, not access permission.

GBIF is a useful alternative for a broader archive, but combining its iNaturalist records with direct iNaturalist data risks duplicate observations. For this small task, one source reduces work; GBIF’s asynchronous custom downloads also introduce an account/email workflow. [GBIF API](https://techdocs.gbif.org/en/openapi/v1/occurrence).

**Documented response example:** the official older API documentation, “GET /observations → Example → Response,” includes `{"id":2281,"species_guess":"gray wolf","quality_grade":"casual","positional_accuracy":354,"coordinates_obscured":false}`. This is a documented San Francisco example, **not a local bee**, and fails the proposed filters. It demonstrates why coordinates alone are insufficient. The older response shape differs from v1. [Original example](https://www.inaturalist.org/api).

**Limit:** API requests failed through the web tool; local Python also failed DNS resolution. No local count, current native checklist completeness, QGIS execution or PDF render was verified.

Compact reproduction example (Python 3 standard library; run in a fresh local folder). It saves response provenance and a CSV for the QGIS steps; failures stop execution. At 10,000+ results, narrow dates rather than silently truncate.

```python
import csv, json, time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

p = dict(taxon_name="Anthophila", lat=37.2296, lng=-80.4139,
         radius=20, photos="true", quality_grade="research",
         native="true", geo="true", geoprivacy="open",
         taxon_geoprivacy="open", license="cc0,cc-by",
         d1="2021-01-01", d2="2026-10-21", per_page=200,
         order_by="id", order="asc")
rows = {}
for page in range(1, 51):
    u = "https://api.inaturalist.org/v1/observations?" + urlencode(p | {"page":page})
    with urlopen(u, timeout=60) as r:
        d = json.load(r)
    Path(f"response-{page}.json").write_text(json.dumps({"url":u,"body":d}))
    if d["total_results"] >= 10000:
        raise RuntimeError("Narrow dates; do not truncate.")
    for o in d["results"]:
        a = o.get("positional_accuracy")
        if (o.get("obscured") or o.get("coordinates_obscured")
            or o.get("geoprivacy") in ("private","obscured")
            or o.get("taxon_geoprivacy") in ("private","obscured")
            or not o.get("location") or a is None or a > 100
            or not o.get("photos") or o.get("license_code") not in ("cc0","cc-by")):
            continue
        lat, lon = map(float, o["location"].split(","))
        rows[o["id"]] = [o["id"], o["taxon"]["name"], o["observed_on"],
            lon, lat, a, o["user"]["login"], o["license_code"],
            "https://www.inaturalist.org/observations/" + str(o["id"])]
    if page * d["per_page"] >= d["total_results"]:
        break
    time.sleep(2)
with open("bees.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","species","date","longitude","latitude",
                "accuracy_m","credit","licence","observation_url"])
    w.writerows(rows.values())
print("Qualifying records:", len(rows), "(zero does not mean absence)")
```

