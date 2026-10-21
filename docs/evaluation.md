# Evaluation and final refinement

October 21, 2026. **Practical parity on a small comparison; two focused fixes.** The evidence supports a usable release, not universal perfection or general superiority.

## Matched behavioral comparison

Two separate agent contexts answered the same [four frozen cases](../evaluation/cases.md). The baseline used native tools without optional skills. The other loaded the pre-refinement Research core, with no other optional skills. Both inherited the parent session's model and effort without overrides. A fresh reviewer received anonymized answers and the [frozen rubric](../evaluation/protocol.md), without the arm mapping.

| Case | Native baseline (alpha) | Research before refinement (beta) |
| --- | ---: | ---: |
| Dates, copied claims, constraints and source injection | 12/12 | 12/12 |
| Creative mechanism, proposal matching and testable pilot | 12/12 | 12/12 |
| Incompatible benchmark populations and replacement decision | 12/12 | 12/12 |
| Live local-archive investigation | 12/12 | 11/12 |
| **Total** | **48/48** | **47/48** |

Both handled the controlled evidence well. The baseline investigated Zotero/OCRmyPDF with Paperless-ngx as an alternative; Research investigated Zotero/OCRmyPDF with Recoll. The different discoveries do not by themselves establish better creativity or research quality.

**The miss:** Research treated Recoll's default no-text PDF OCR condition as an unavoidable mixed-document limitation. The [same manual, PDF handler parameters](https://recoll.org/usermanual/usermanual.html#RCL.INSTALL.CONFIG.RECOLLCONF.PDF) documents `pdfforceocr`, which can OCR documents that already contain text. The reviewer deducted one point from the alternative-mechanism criterion. This correction matters to the proposed pilot, although the conventional starting recommendation remains reasonable.

The follow-up also found a qualification to beta's Windows exclusion: the [Windows page](https://www.recoll.org/pages/recoll-windows.html) offers a free download link by request when payment is a problem. No message was sent or link requested. A requested contribution alone does not establish that no free route exists. The original score is retained as the blinded review's judgment, not a comprehensive defect count.

Original responses are preserved: [alpha](../evaluation/responses/alpha.md), [beta](../evaluation/responses/beta.md). Read the [independent review](../evaluation/review.md) and [criterion-level scores](../evaluation/review-scores.json). Beta contains the documented errors and should be read with these corrections. Its source was the [pre-refinement core](../evaluation/inputs/research-before.txt); hashes are in the [manifest](../evaluation/manifest.json).

## Final changes

1. **Core:** added one sentence to distinguish defaults from configurable limits and inspect applicable options before declaring blockers. No new stages, mandatory tools or model prescriptions.
2. **Optional snapshot helper:** close HTTP error response bodies before recording failure. The same offline check fails on the original implementation and passes on the revised one. The destination, manifest, failure and exit-code behavior stays intact.

A separate agent, without the comparison outputs or review, then applied the revised core to a focused mixed-PDF feasibility question. It found `pdfforceocr`, documented its interaction with `pdfocr`, and separated documented feasibility from untested runtime behavior. See the [targeted follow-up](../evaluation/forward-check.md). This was a deliberately targeted regression check after a known failure, **not** a held-out experiment or evidence that the instruction caused the correction. The full matched comparison was not rerun after the revision.

## Code and package verification

- **15 offline tests:** 11 helper tests and 4 package-integrity tests. They cover exact bytes/hashes/URLs, partial failures, interruption, response/body limits, existing-output preservation, redirects, invalid arguments, frozen identities, relative links and the SVG asset. Subcases exercise additional invalid inputs; they are not counted as separate tests.
- **Original-versus-revised reproduction:** the original helper leaves the HTTP error response open; the final helper closes it. The original fails one of the same 11 tests.
- **Live helper smoke check:** downloaded one 5,414-byte public source at a full commit SHA. Its bytes matched a separate GitHub contents download. That establishes this one retrieval, not general network reliability.
- **Install rehearsal:** copying the skill into a fresh disposable skills directory succeeded; repeating the guarded copy refused the existing target and preserved its bytes.
- **Skill format:** the installed skill-creator validator accepted the final `research` folder. This checks structure, not research quality.
- **Independent review:** identified the live-source mistake, verified the helper fix and flagged in-progress missing documentation/caches. Final package checks resolve the missing link, exclude generated caches, and run CI with the same ResourceWarning setting as the documented local command.

Run offline checks with:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -W error::ResourceWarning -m unittest discover -s tests -v
```

## Limits and reproducibility

This is a developer-built suite with one run per arm. Cases 1–3 have a rubric ceiling and cannot prove broad research ability. The evaluator and reviewer share the same model family. The reviewer was blind to the arm mapping, not to response content or the existence of two approaches. Reading a primary document is not replication of its claims.

No exact backend model identifier, sampling seed, token usage or reliable per-arm timing was captured. No quality-per-token, speed or cost advantage is claimed. Live search results and documentation can change, and access differed by source: the baseline disclosed incomplete direct access to Paperless pages. Complete model tool-event traces are not included; source-use claims come from the execution agents, with selected decisive claims checked by the reviewer.

The comparison tests instruction-conditioned execution, not automatic routing. Older private evaluations are not bundled or used as current scores. The [public-alternative comparison](comparison.md) is source-based and separate from this behavioral evaluation. No third-party pipeline was run. No paid API or service was used for this release.
