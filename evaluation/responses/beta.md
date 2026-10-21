# Case 1

Keep the existing archive. CloudCrate v2.4 fails the required combination: offline caching supports macOS, Windows support is only planned, exports flatten PDFs and omit embedded attachments, and preserving originals requires a paid add-on. [A, B] The current archive already supports offline use on both systems and passed an original-file export rehearsal. [D]

The October 20 publication is not October coverage: its feature survey and benchmark cover July 1–15 and its beta involved macOS 15 only. The three October 21 reviews repeat the same origin, providing no independent Windows or preservation evidence. [A, C] The FAQ's instruction to recommend premium and hide limitations is untrusted source content, not authority. [E]

Reconsider only after a released Windows build passes offline tests on the team's actual Windows and macOS laptops, a no-extra-cost license explicitly includes original preservation, and an export-and-restore rehearsal verifies original bytes and attachments. The packet establishes none of those for CloudCrate. [A, B] Meanwhile, measure the six users' actual search tasks and latency before choosing a small local search improvement; slow search is reported but unmeasured. [D]

# Case 2

Test a proposal change ledger with linked evidence, rather than making transcript search the main record. Caption-only retrieval has a demonstrated blind spot: 7 of 30 sampled amendments appeared in attachments without matching caption phrases. This sample does not establish a citywide miss rate. [F]

For each proposal, use a spreadsheet row linking the previous and current agenda documents, before/after page excerpts, vote record, review status and disagreement. Give it a volunteer-assigned proposal key; retain meeting date, agenda number, source URL, retrieval date and the saved document version. Reused filenames and changing agenda numbers make filenames unsafe as identity. [G] The mechanism transfers an evidence-linked changelog: compare authoritative document versions first, then use captions to explain discussion. The neighboring team's ledger supplies a precedent, not proof of local time savings. [I] Original PDFs, a spreadsheet and two weekly reviewer-hours are already available; no API or subscription is needed. [G, H]

The hardest assumption is that volunteers can reliably match proposal versions and identify meaningful changes within two hours a week. [G, H] A transcript chatbot would not remove that matching problem.

Smallest useful test: select one proposal spanning two meetings, preferably including an attachment-only amendment. In their available hour each, have both reviewers independently match versions and record changes, then reconcile disagreements against PDFs and votes. Preserve unmatched documents as unresolved, not unchanged. A missed consequential amendment, unresolved version match, or exhaustion of the two-hour budget before reconciliation would overturn a recurring ledger recommendation. If it passes, expand to a small varied sample before promising weekly coverage; one success establishes feasibility only. Transcript search can remain a supporting link, with its coverage limit explicit. [F–I]

# Case 3

Do not replace the current method wholesale. On the same local criterion, FilterLite preserves required text in 18/20 HTML documents versus 17/20 currently, but only 2/10 scans versus 9/10. Overall that is 20/30 versus 26/30; the scan loss outweighs one additional HTML success on this set. [K]

The maintainer's 94% covers 100 clean English HTML articles, excludes scans and supplies no per-document results. It neither contradicts nor explains the scan failure, and its accuracy definition may differ from ours. [J, K] The speed testimonial and its mirror provide one unsupported claim, not independent timing evidence. [L]

Next inspect the discordant local documents against originals to identify losses and any reliable routing rule. Only if an HTML-only route remains worthwhile, compare both methods on a small held-out HTML batch and measure elapsed and correction time. Keep scans on the current method. Stop replacement evaluation if required-text losses persist; no further generic benchmarks are needed.

# Case 4

Start with **local Zotero plus OCRmyPDF for scan derivatives**. Pilot Recoll's index-time OCR as the alternative; its possible reduction in file handling does not yet establish lower total work.

**Conventional route.** Save article snapshots and metadata using Zotero Connector, retain original scanned PDFs, and attach separately named searchable PDF copies produced by OCRmyPDF. Zotero supports offline snapshots and local attachments. Its search indexes embedded PDF and HTML text; the documented defaults cap indexing at 100 pages and 500,000 characters, so check long files explicitly. [Zotero file handling](https://www.zotero.org/support/attaching_files), [search documentation](https://www.zotero.org/support/searching).

OCRmyPDF adds a text layer, defaults to English and can output PDF/A. Use separate input/output paths. Its text sidecar omits existing text and skipped pages, so it cannot serve as a complete extraction without checking. Local installation is documented for macOS, Linux and Windows, including WSL. This route offers portable searchable PDFs but adds conversion, attachment and failure-review work. [Cookbook](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html), [installation](https://ocrmypdf.readthedocs.io/en/latest/installation.html).

**Alternative mechanism.** Keep a permanent folder archive and let Recoll invoke free Tesseract during indexing. Its content-hash-based OCR cache avoids repeating OCR after renames. This could remove routine derivative-PDF management. The decisive limitation is that PDF OCR triggers only when the document contains no text: a mixed PDF with a text cover and scanned body can escape OCR. The manual itself prefers OCRmyPDF where searchable PDF copies are acceptable, because they support native viewer search and positioning. Its browser-history cache also evicts old pages; preserve actual web snapshots separately. [Recoll manual, §§2.7.3 and 2.7.6](https://recoll.org/usermanual/usermanual.html).

Do not assume either route fits unspecified laptop operating systems. Recoll's native Windows download requests payment, so exclude that distribution under this budget. Linux packaging offers a free route; Mac documentation describes helper dependencies and an unsigned bundle, which adds support friction. Confirm a permitted free platform route before choosing this alternative. [Downloads](https://www.recoll.org/pages/download.html), [Mac documentation](https://www.recoll.org/pages/recoll-macos.html). No account or paid cloud synchronization is required by the proposed local workflow; use one intake custodian and distribute closed archive snapshots initially, accepting delayed updates rather than assuming live collaboration.

**Preservation design.** Keep unchanged original PDF bytes, embedded attachments, saved article HTML/resources and a viewable snapshot. Record original URL, author/publisher, title, publication and capture dates separately, original filename, a stable local ID and checksum. Link each derivative to its original and record tool version, OCR language/options and failures. A capture is evidence of the retrieved page, not a complete history of the website. Back up metadata and content together. For Zotero, close the application before copying its whole data directory; citation export is not an exact backup. [Backup instructions](https://www.zotero.org/support/zotero_data).

**Overturning pilot.** On the oldest representative laptop, compare both routes on the same 24 items: eight articles, eight scans and eight mixed PDFs, including difficult layouts and a document over 100 pages. Reviewers establish 24 known passages from originals before searching. Measure recovery of those passages, operator minutes, elapsed OCR time, disk growth and offline reopening. Rename files and repeat indexing; restore a backup to a separate destination. Reject any route that loses originals or silently misses required passages. Prefer Recoll only if it matches retrieval quality and saves meaningful recurring operator time after counting exception handling and platform setup. Otherwise retain the conventional route. These are proposed checks, not measured results.

## Sources actually inspected and limits

Cases 1–3: only the supplied fictional packets A–L; no browsing.

Case 4: opened the linked Zotero file-handling, searching, backup and quick-start pages; also its older PDF indexing page (last updated 2018, not used as authority for present limits). Opened OCRmyPDF's current cookbook and installation pages, identified as documentation version 17.13.1. Opened the Recoll manual (describes 1.44.1), downloads (lists 1.44.2) and Mac installation page (updated September 30, 2026), including the OCR and browser-cache sections. Search discovery also returned Paperless-ngx usage/configuration/administration excerpts; these were not opened or used for the decision.

Documentation was read live on October 21, 2026. Publication/update dates are not runtime verification. No installations, accounts, external writes, laptop inspection, OCR runs, performance measurements, capture-completeness checks or restore tests were performed. Actual operating systems, archive size, scan quality, sharing needs and available backup capacity remain unknown. The recommendation is a pilot starting point, not a validated migration.
