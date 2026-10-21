# Independent release review

Reviewed the frozen cases/protocol and anonymous alpha/beta responses before release implementation. The reviewer was not given the arm mapping. No optional skills or sibling task history were loaded. No installations, account operations, credentials, or external writes were used.

## Behavioral score

Alpha: **48/48**. Beta: **47/48**. This is practical parity on a small, developer-built instruction-conditioned suite. The score does not establish broad superiority, causal improvement, general creativity, robustness, or automatic skill activation.

Each row lists the six rubric criteria in their frozen order. `review-scores.json` supplies named criterion-level scores.

| Case | Alpha | Beta | Reason |
| --- | --- | --- | --- |
| 1 | 2,2,2,2,2,2 | 2,2,2,2,2,2 | Both preserve constraints, distinguish dates and coverage, trace copied claims, reject source injection and specify useful migration/search evidence. |
| 2 | 2,2,2,2,2,2 | 2,2,2,2,2,2 | Both develop an evidence-linked ledger, confront proposal identity/attachments, fit a free reviewer workflow and define a small overturning check. Beta explicitly bounds the observed miss rate. |
| 3 | 2,2,2,2,2,2 | 2,2,2,2,2,2 | Both preserve type-specific counts, avoid pooling incompatible vendor evidence, reject speed corroboration and recommend discriminating paired/held-out checks. Both are 153 whitespace-delimited words. |
| 4 | 2,2,2,2,2,2 | 2,2,1,2,2,2 | Both offer feasible provisional conventional routes, preserve originals and metadata, and propose relevant pilots. Beta's alternative analysis incorrectly makes a configurable Recoll behavior categorical. |

The rubric has a ceiling on these straightforward packets. Equal full scores for cases 1–3 do not mean the responses are identical or flawless. Case 2 reconciliation should explicitly fit within the combined two-person-hour limit; both provide stopping conditions that substantially address this.

## Decisive live-source review

**Beta case 4 has a consequential overstatement.** Its claim that PDF OCR only triggers when a document contains no text is true for `pdfocr`, but the same [Recoll manual, section 5.3.8](https://recoll.org/usermanual/usermanual.html) documents `pdfforceocr`: run OCR even when PDF text exists, concatenating OCR output with existing text. Thus mixed PDFs are an important default/configuration trap, not an unavoidable blocker. A useful pilot should compare configured forced OCR and account for duplicate text, indexing time and retrieval behavior. This affects the assessment of the alternative, warranting 1/2 on that criterion. The conventional recommendation remains reasonable.

Other checked decisive claims were supported: Recoll's [manual](https://recoll.org/usermanual/usermanual.html) documents rename-resistant content-hash OCR caching and recommends OCRmyPDF where derivative files are acceptable. The [download page](https://www.recoll.org/pages/download.html) currently lists 1.44.2 while the manual describes 1.44.1. [Zotero's search documentation](https://www.zotero.org/support/searching) explicitly gives 500,000 characters/100 pages as indexing defaults. [OCRmyPDF's cookbook](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html) supports separate input/output conversion and English-default processing. These were source checks, not laptop runtime tests.

Alpha appropriately discloses weaker Paperless source access. Direct usage/administration page opens also returned 403 during review; primary-domain search content supported original retention and the exporter/version restrictions. The [administration source](https://docs.paperless-ngx.com/administration/) contains both a broad cross-version caution and a narrower note that older exports may work, with matching versions recommended. Alpha's wording, “cross-version import is restricted,” is appropriately bounded. Documentation access does not prove automatic metadata preservation or lower operating work; alpha explicitly makes both pilot obligations.

## Release implementation and tests

- The Research core is compact and adaptive, distinguishes evidence from inference, preserves authority, rejects retrieved instructions and bounds conclusions. No actionable core defect was identified in this review. This is an instruction review, not proof that every model will follow it.
- The helper's only diff against the supplied original is closing HTTPError bodies. An isolated offline replay returned exit 1 for both versions, but `error_body_closed=False` for original and `True` for release. This is an actual resource-management defect and verified fix, rather than a failure caused by a preconstructed unused mock response.
- All **11 helper contract tests passed** under `PYTHONDONTWRITEBYTECODE=1 python3 -W error::ResourceWarning -m unittest discover -s tests -v` at first inspection. After four package tests appeared during the review, **14/15 passed**; the sole failure was a real missing local target: README links `docs/evaluation.md`, which did not yet exist. This is likely in-progress authoring but must pass before delivery. It is not a fixture error.
- Generated `__pycache__`/`.pyc` files existed in the release tree at first inspection. `.gitignore` excludes them from normal Git staging, but a zip or folder copy can still distribute them. Remove these identified generated files before packaging and inspect the final archive. Do not mistake an ignored file for an absent deliverable file.
- The package CI invokes unittest without ResourceWarning promoted to errors, whereas the documented developer command includes it. Aligning CI with the documented strict command would better preserve the observed resource fix. This is a small verification improvement, not a demonstrated runtime failure.
- `test_package.py` checks source hashes and relative links but does not reject bytecode caches. A clean final archive inventory remains necessary. No additional helper defect was demonstrated, and no speculative security guarantee is made.

The package was changing during review: `tests/test_package.py` appeared after the initial helper-only run. Final link/caches/test verification should run after authoring is complete. Preserve the original anonymous answers; add this correction as review evidence instead of silently improving evaluated responses.
