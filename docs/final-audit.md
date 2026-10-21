# Aperture final release audit

Reviewed October 21, 2026 against the current the release source tree tree. No source edits, installation, account access, credential access, external writes, paid services or new research executions were performed. This report is the only retained audit output. Subsequent source changes require checking the affected facts again.

## Disposition

No blocking release defect found within this audit scope. One small user-facing naming inconsistency should be corrected. The final probe is a useful narrow check, with meaningful implementation and coverage limits; it does not demonstrate a complete watcher or prove that the final sentence fixes advisory completeness. The release documentation substantially preserves these limits and correctly separates the scored candidate from the repaired final core.

## Actionable finding

**P3: Update the skill-picker name in README, Try it.** It currently tells users to select “Research”; `research/agents/openai.yaml` now declares the visible name “Aperture Research.” Use the current display label while retaining `$research` as the invocation. This is a presentation mismatch, not a change to invocation compatibility.

## Passed checks

- Ran `PYTHONDONTWRITEBYTECODE=1 python3 -W error::ResourceWarning -m unittest discover -s tests -v`: **15/15 passed**. This covers recorded v1/v2 file identities, relative Markdown links, SVG constraints, home-path/symlink checks and snapshot helper behavior. These checks do not execute model comparisons.
- Recomputed pair preferences and score totals: **5 Research, 2 ties, 1 native; 177/192 versus 167/192**. The chart generator reproduces the current SVG byte for byte. Inspected the supplied evidence-chart PNG: judgments and strengths match JSON, including native preference despite tied scores and ties despite different scores. No clipping or hidden adverse row was visible at its supplied size.
- `research/SKILL.md` equals `evaluation/v2/inputs/final-core.txt` byte for byte. The only core difference from the scored candidate is the disclosed coverage-counterexample sentence. Metadata retains the `research` prompt/invocation, description and implicit invocation policy; its visible label changes to Aperture Research. Discovery remains exploratory and proportional, with direct work allowed.
- Retained raw public advisory JSON hashes match the published source-check record. Recomputed **86 global / 61 repository / 29 shared**; both published difference sets match. The retained raw records support the named omissions GHSA-44wm-f244-xhp3 and GHSA-78g4-xqwv-q3g8, including package relevance and non-withdrawal. This confirms the retained source observation, not a fresh live endpoint result.
- The retained repository record for **GHSA-654x-cwwv-5j9c** supports publication October 19, 2026, affected range 11.2.1–13.0.0, no patched version and the Arrow/PILLOW_ALIGNMENT condition. The post-release counterexample is consistent with the probe evidence and parent source records.
- Extracted and compiled the exact final-probe Python block. Synthetic fixtures passed numeric version ordering, prerelease exclusion, fully yanked release retention without latest selection, two-page Link pagination, both advisory inputs and retaining an older-branch release beneath the latest version. A simulated source failure propagates visibly without printing a success snapshot.
- Public material keeps the native win, incomplete development artifacts, reviewer exposure, sanitized crosscheck differences, failed EPA verifier and changed version scope visible. It does not silently promote the post-repair probe into a ninth blind pair. The no-general-superiority and no-causal-ablation qualifications are appropriate.
- No local home paths were found in release research/docs/evaluation by the package checks. A targeted plaintext credential-pattern scan found no matches. This is a scoped leak check, not proof against every possible secret or personal datum.

## Important limits and unavailable checks

- **Probe source coverage:** the probe identifies a release-versus-advisory counterexample and implements both repository/global sources, but does not empirically test the concrete global-only and repository-only omissions against its own live output. Its evidence explicitly says API bodies and global-versus-repository coverage were not retrieved/measured. Retained parent raw records support the chosen combination, but do not convert the worker probe into an end-to-end coverage test. Keep that distinction in release claims.
- **Probe implementation:** this is a manual snapshot/diff pilot. It does not implement the proposed per-source last-success state, alias grouping, automatic alerts, scheduler, conditional requests, backoff or visible last-success timestamp. A source error prevents a fresh combined snapshot; the shell preserves the old baseline. Raw advisory cosmetic changes can produce differences. The answer accurately discloses the manual/unfinished service scope. Do not describe it as a completed reliable daily service.
- The ordinary-numeric-version parser deliberately omits prerelease and unexpected future version conventions. If all recognized files are yanked, `max()` fails visibly rather than producing a misleading latest version. No silent-loss issue was reproduced with the tested ordinary stable filenames.
- No fresh network requests, vulnerability reproduction, EPA re-download or whole regional bee harvest were performed. EPA byte/row claims are supported here by retained reviewer/parent reproduction records, not a new acquisition in this audit.
- PaperBanana-native rendering/critique has explicit retained review evidence and editable outputs, and public copy distinguishes it from upstream API inference. This audit inspected the evidence-chart render and data alignment, but did not independently rerun that skill workflow or certify all visual exports. Historical review notes are preserved as such.
- Final installed bytes, release ZIP/checksum, GitHub publication/social setting and CI status were not verified. These are the parent release checks. The source tree can be reviewed successfully without claiming those outcomes have happened.

The bounded usefulness conclusion is supported by the retained independently checked H1 benefit and openly qualified adverse results. This audit does not establish universal reliability, automatic skill selection, or superiority over the complete 01/Moonshot/Research setup.
