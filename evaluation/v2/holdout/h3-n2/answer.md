Use **GBIF’s public search API and a local, printable SVG map**. No account, API key, uploads or paid service is needed. Start with common eastern bumble bee (*Bombus impatiens*), a native eastern-US species documented by [Xerces](https://www.xerces.org/sites/default/files/publications/10-014.pdf). Label this a **one-species learning map**, not a complete inventory of native bees. Expand only with a checked Virginia-native species list; a bee record is not automatically a native bee record.

The example below searches a deliberately defined Blacksburg-area rectangle, 37.18–37.30°N and 80.50–80.35°W, from January 2021 through October 21, 2026. It requires human observations, presence, attached still images and coordinates without GBIF geospatial flags. [GBIF documents these filters](https://gbif.github.io/gbif-api/apidocs/org/gbif/api/model/occurrence/search/OccurrenceSearchParameter.html), and its [search service](https://techdocs.gbif.org/en/openapi/v1/occurrence) supports pages of up to 300 records. Unlike an asynchronous GBIF download request, most API reads require no authentication. [API reference](https://techdocs.gbif.org/en/openapi/)

Save the example as `bee_map.py` in an empty folder and run `python3 bee_map.py` with Python 3 and internet access. It writes `map.svg` and a companion `records.csv`. Open the SVG in a browser and print to PDF for a downloadable handout. Cells are 0.01° wide, roughly 0.9 × 1.1 km here; symbols show record counts, not individual bees. Coordinates label the extent; north is up. This is an overview, not a trail-navigation map.

Conservatively exclude missing/over-500-metre uncertainty and any reported withholding/generalization. Do not infer hidden coordinates from photographs, comments or nearby sightings. iNaturalist obscured points are randomized within a much larger cell, so plotting one as a walk stop would be misleading. [iNaturalist geoprivacy](https://help.inaturalist.org/en/support/solutions/articles/151000169938-what-is-geoprivacy-what-does-it-mean-for-an-observation-to-be-obscured-)

Use this exact legend: **“Photographed historical records passing these filters. Blank areas mean no retained records, not no bees. Record density reflects reporting effort; sightings this weekend are not guaranteed.”** Opportunistic records support presence rather than reliable absence or abundance estimates. [GBIF guidance](https://docs.gbif.org/freshwater-data-publishing-guide/en/) The October walk may differ substantially from summer records. Choose an independently established public walking route; observation coordinates confer no access permission. Review linked records for identification and photo relevance before use. Retain source links, dates and licenses; link photographs rather than copying them, since [image licenses can differ](https://techdocs.gbif.org/en/openapi/images).

**Verification limit:** live GBIF/iNaturalist API access failed in this environment, and the GBIF dataset page returned HTTP 403. No local record count or rendered map was verified. The documented response example is GBIF’s shortened occurrence response: `{"key":5104646682,"basisOfRecord":"HUMAN_OBSERVATION","occurrenceStatus":"PRESENT"}`. It concerns *Acacia acuminata*, demonstrates response structure only, and is **not a local bee sighting**. [Official example](https://techdocs.gbif.org/en/data-processing/taxonomy-interpretation)

Compact reproduction example, not executed successfully here:

```python
import csv, json, math, urllib.parse, urllib.request
from collections import Counter
q = dict(scientificName='Bombus impatiens',
         decimalLatitude='37.18,37.30', decimalLongitude='-80.50,-80.35',
         eventDate='2021-01-01,2026-10-21', mediaType='StillImage',
         basisOfRecord='HUMAN_OBSERVATION', occurrenceStatus='PRESENT',
         hasCoordinate='true', hasGeospatialIssue='false', limit=300)
rows, seen, offset = [], set(), 0
while True:
    if offset + 300 > 100000: raise RuntimeError('Query too large; narrow dates')
    url = 'https://api.gbif.org/v1/occurrence/search?' + urllib.parse.urlencode(q | {'offset':offset})
    with urllib.request.urlopen(url, timeout=60) as f: page = json.load(f)
    for r in page['results']:
        u = r.get('coordinateUncertaintyInMeters')
        identity = r.get('occurrenceID') or str(r['key'])
        if identity in seen: continue
        if u is None or not 0 <= u <= 500: continue
        if r.get('informationWithheld') or r.get('dataGeneralizations'): continue
        if not any(m.get('type') == 'StillImage' for m in r.get('media', [])): continue
        lat, lon = r['decimalLatitude'], r['decimalLongitude']
        if not (37.18 <= lat < 37.30 and -80.50 <= lon < -80.35): continue
        seen.add(identity)
        x, y = math.floor((lon+80.50)*100), math.floor((37.30-lat)*100)
        rows.append([x,y,r.get('eventDate',''),f"https://www.gbif.org/occurrence/{r['key']}",r.get('license','')])
    if page['endOfRecords']: break
    offset += 300
if not rows: raise RuntimeError('No retained records; do not claim absence')
with open('records.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['cell_x','cell_y','date','source','license']); w.writerows(rows)
s = ['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="800" viewBox="0 0 1000 800">',
     '<rect width="1000" height="800" fill="white"/>',
     '<text x="40" y="30">Bombus impatiens: photographed records, 2021–2026-10-21; N ↑</text>',
     '<rect x="100" y="80" width="750" height="600" fill="#eef2ee" stroke="black"/>',
     '<text x="100" y="70">37.30 N; west 80.50 W; east 80.35 W</text>',
     '<text x="100" y="705">37.18 N; cells ~0.9 × 1.1 km; numbers = records, not bees</text>',
     '<text x="40" y="745">Blank = no retained records, not no bees. Reporting effort varies.</text>',
     '<text x="40" y="775">Historical sightings do not guarantee bees this weekend. Source: GBIF; see records.csv.</text>']
for (x,y),n in Counter((r[0],r[1]) for r in rows).items():
    s += [f'<circle cx="{125+50*x}" cy="{105+50*y}" r="17" fill="#f0bb41"/>',
          f'<text x="{125+50*x}" y="{110+50*y}" text-anchor="middle">{n}</text>']
open('map.svg','w').write(''.join(s)+'</svg>')
```
