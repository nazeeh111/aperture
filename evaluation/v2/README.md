# Fresh real-world comparison

Start with the [readable findings](../../docs/real-world-evaluation.md), [machine-readable results](results.json) and [frozen protocol](protocol.md).

- **Development:** [image pack](development/D1.md), [notes recovery](development/D2.md). One native and one current-skill execution each. Raw outputs and selected evidence are in the adjacent run folders; [reviews](review/) identify the gaps.
- **Untouched tasks:** [air quality](holdout/H1.md), [update watcher](holdout/H2.md), [bee map](holdout/H3.md), [evidence digest](holdout/H4.md). Each has independent `n1`, `n2` native and `s1`, `s2` Research executions. No best-of selection.
- **Compared instructions:** [v1.0.1 core](inputs/v1.0.1-core.txt), [tested candidate](inputs/tested-candidate.txt), [final core](inputs/final-core.txt). Final source-coverage repair is separate from the eight-pair measurement.
- **Primary reviews:** [H1-R1](review/holdout/H1-R1/review.md), [H1-R2](review/holdout/H1-R2/review.md), [H2-R1](review/holdout/H2-R1/review.md), [H2-R2](review/holdout/H2-R2/review.md), [H3-R1](review/holdout/H3-R1/review.md), [H3-R2](review/holdout/H3-R2/review.md), [H4-R1](review/holdout/H4-R1/review.md), [H4-R2](review/holdout/H4-R2/review.md).
- **Fresh sanitized crosschecks:** [H1-R2](review/holdout/H1-R2/fresh-crosscheck.md), [H2-R2](review/holdout/H2-R2/fresh-crosscheck.md). Preserve their different judgments rather than choosing the more favorable review.
- **Arm mapping:** [map](arm-map.json). Original numeric preferences are not silently changed after unblinding.
- **Freeze records:** [original](freeze.json), [final brief identities](holdout_brief_freeze.json), [candidate](candidate_freeze.json), [post-benchmark repair](final_repair_freeze.json). [Preflight change](holdout_preflight.md) explains why verbose process hints were removed before comparison executions.

The H1/H2 reviewer encountered an arm-revealing field in selected evidence metadata. That batch was not fully blind. A fresh crosscheck used sanitized packets; it could not reproduce EPA access and therefore did not certify that material win, while it verified state/replay advantages in the watcher pair. Independent reviewer and parent public-read reproductions of the EPA bytes are retained separately. Access uncertainty and reviewer disagreement remain part of the result.

Original answers are preserved, including incomplete work, source-access errors, code limitations and qualified or mistaken claims. Only task-local filesystem identities were redacted for publication. Evidence files are selected worker-reported records, not full native traces.

To reproduce: use fresh independent contexts, the frozen prompts/instructions and the same native tool/model settings; preserve first outcomes and all access failures. Do not load the arm map or prior answers in execution/review contexts. Host/model/live-source changes can alter results. No hidden API evaluation service is required.

The chart is generated directly from `results.json`:

```sh
python3 scripts/plot_evaluation.py
```

Run this from the repository root. It refuses missing/duplicate pair identities and inconsistent counts/scores. Actual SVG source remains editable in [assets/](../../assets/).
