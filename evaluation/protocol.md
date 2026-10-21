# Behavioral evaluation protocol

The [cases](cases.md) and scoring criteria below were frozen before either response. Run once per arm, in separate contexts, with the same model, effort, native tools and authority. Retain unsuccessful or incomplete outputs. Do not tune the skill to these cases and then present them as held-out evidence.

- Baseline: answer all four cases without loading optional skills.
- Research: load `research/SKILL.md`, then answer the identical cases without other optional skills.
- Cases 1–3 use only the supplied fictional evidence. Case 4 permits live primary-source research, no installs, accounts or external writes.
- Preserve complete answers and source-access limitations. Record actual model/settings, date, elapsed time and tool traces if the host exposes them. Missing telemetry is unknown, not zero.
- Give anonymized answers, case packets and this rubric to a fresh reviewer. Ask it to inspect disputed decisive sources and report consequential issues. Do not tell it which arm used Research.

Score each criterion 0 absent/wrong, 1 partial, 2 clear and supported. This yields 24 criteria and a maximum of 48 points. Scores summarize this rubric only.

| Case | Six criteria |
| --- | --- |
| 1 | Binding constraints and decision; dates/coverage/version; shared origins; export/original preservation; rejects retrieved instruction; useful missing measurement. |
| 2 | Mechanism beyond caption search; attachments and matching problem; free feasible workflow/reviewer budget; empirical hardest assumption; falsifiable small pilot; separates neighbor report from local evidence and avoids novelty claims. |
| 3 | Preserves denominators and document types; explains apparent conflict; supported replacement decision; unsupported speed/corroboration rejected; useful discriminating next check; length at most 160 words. |
| 4 | Primary documentation actually inspected; feasible free conventional route; developed alternative and interaction; originals/metadata preservation; hardest assumption and falsifiable pilot; bounded recommendation with uncertainty. |

Interpretation: one run per arm, a small developer-built suite and a same-family reviewer cannot establish broad superiority, robust activation, general creativity or causal improvement. Live discovery is not source-controlled. Report close results as practical parity, with differences described at the case level.

This tests instruction-conditioned execution. It does not test whether automatic skill selection loads or skips Research. For that, use separate unprimed discovery tests with observable load traces.
