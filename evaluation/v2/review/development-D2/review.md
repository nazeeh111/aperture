# Anonymous review: development D2

Preference: **slate slightly better**. Both are strong, feasible documentation-based proposals with the same main route and a useful manual-transfer alternative. Slate adds a checked macOS compatibility gate and better protection of unsynchronized work and local Git history. Cedar has meaningful Android operating detail that slate lacks. These offset enough of the advantage that a material win is not justified.

Reviewed only the protocol and this packet. No sibling folders, arm map, skill, history or memory were consulted. This is a fresh source review, not evidence of different-model-family independence; exact backend model telemetry is unavailable. No apps were installed or rehearsals executed. Both answers meet the 650-word limit (588 cedar and 570 slate whitespace-delimited words, including links).

## Frozen rubric

| Dimension (0–4) | cedar | slate | Reason |
|---|---:|---:|---|
| Factual/claim support | 4 | 4 | Decisive documented claims independently confirmed; proposals identified as proposals. |
| Constraints and feasibility | 3 | 4 | Cedar omits the recommended macOS wrapper/version gate; slate supplies it and flags contradictory README text. Cedar is more precise about Android. |
| Breadth and material alternative | 4 | 4 | Manual LocalSend inbox plus local Mac Git is a real change in workflow, with explicit integration work and delay. |
| Decisive source inspection | 4 | 4 | Both inspected actual versioning limits, conflict behavior, Android project status, mobile Git warning and alternate-platform requirements. |
| Artifact/actionability | 3 | 3 | Both provide usable minimal operating/recovery plans, but leave version restore UI and alternative Git setup largely for the adopter. |
| Falsifiable verification and uncertainty | 4 | 4 | Disposable conflict/deletion/independent restore checks with observable success conditions; neither claims device validation. |
| Total | 22 | 23 | Totals are secondary to feasibility and checked useful differences. |

## Independently checked useful additions

**Cedar advantages:**

- Specifically rejects Obsidian Android private app storage and explains shared-storage permission. This prevents an incompatible folder choice; slate only says both apps must access the folder. Confirmed in [Obsidian Android help](https://obsidian.md/help/android), vault-location section, lines 1–5.
- Identifies the hourly five-minute battery mode's dependence on an available peer and recommends foreground overlap. This is particularly useful under the no-always-on-server constraint. Confirmed in the [fork battery guidance](https://github.com/researchxxl/syncthing-android/blob/main/wiki/Info-on-battery-optimization-and-settings-affecting-battery-usage.md), lines 188–195. Slate's general battery warning does not provide this specific failure mechanism.
- The alternative identifies each submission's starting snapshot and gives a concrete file-recovery command. The starting snapshot reduces manual merge ambiguity; the command's semantics are confirmed in [git-restore](https://git-scm.com/docs/git-restore), lines 209–228. This is useful workflow design, not an observed runtime outcome.

**Slate advantages:**

- Specifies the actual supported macOS application, macOS 12 minimum for v2 and deprecated v1; also resolves the older macOS 11 installation sentence using the explicit compatibility section. This can change route feasibility for an older laptop. Confirmed in [syncthing-macos README](https://github.com/syncthing/syncthing-macos), lines 225–227, 243–245, 267–275. Cedar provides no Mac-specific feasibility gate.
- Calls for protecting each member's unsynchronized work before reconciliation and makes backups session-based. The practical benefit follows from the shared documented incoming-only history limitation, rather than a tested backup implementation. Cedar acknowledges that never-transmitted files can be lost, but does not give this mitigation. Confirmed limitation in [versioning](https://docs.syncthing.net/users/versioning.html), lines 2–13.
- Includes disconnected Git bundles and a separate-clone recovery rehearsal for the alternative, preserving committed history beyond loss of the integrator's Mac. Git explicitly supports full repository bundles and cloning from them in [git-bundle](https://git-scm.com/docs/git-bundle), lines 218–228. Cedar's alternative gives file recovery from the existing repository but does not explicitly preserve its history independently.
- Flags manual updates for direct LocalSend downloads, a small but actionable maintenance obligation. Confirmed in [LocalSend README](https://github.com/localsend/localsend), lines 264–271.

## Shared claims checked

- [Official Android repository](https://github.com/syncthing/syncthing-android), archive banner line 115: December 3, 2024 archive. [Fork releases](https://github.com/researchxxl/syncthing-android/releases), lines 150–175 and 214–264: v2.1.7.0-rc.4 prerelease October 14 and v2.1.6.0 latest stable October 6. Release notes loaded; GitHub assets/comparison widgets showed errors. This supports current release activity, not security certification.
- [Syncthing FAQ](https://docs.syncthing.net/users/faq.html), lines 79–81: peer overlap and deletion propagation. [Versioning](https://docs.syncthing.net/users/versioning.html), lines 2–13: disabled default, per-device settings, incoming-only archives and finite Simple retention. [Conflicts](https://docs.syncthing.net/users/syncing.html), lines 20–23: concurrent edits create propagated conflict copies.
- [Obsidian Git README](https://github.com/Vinzent03/obsidian-git), lines 311–333: explicit mobile discouragement, memory/SSH limitations and possible clone/pull crashes.
- [LocalSend site](https://localsend.org/), lines 33–67 and 112–114: Android/macOS, local-network transfer and no account. [Repository](https://github.com/localsend/localsend), lines 284–302: Android 7, macOS 11, firewall and isolation constraints. [Latest release endpoint](https://github.com/localsend/localsend/releases/latest) resolves to v1.18.2, confirming slate's version claim. The version number itself earns no usefulness credit.

## Errors, limits and candidate weaknesses

No critical infeasible recommendation or invented evidence found. Both meet the constraints through proposals and existing removable storage; both explicitly leave independent backup unmet if that storage is absent. Both appropriately avoid calling synchronized replicas independent backups.

Cedar's missing Mac support gate is the main consequential omission, conditional on participants' OS versions. Its clock end excludes final writing, explicitly disclosed, so its reported interval cannot be treated as complete execution duration. Slate's phrase about repeating a local deletion to expose the limitation is somewhat ambiguous: the deleting device has no own archive, but a connected receiving peer can still recover the incoming deletion. Cedar describes the two-device deletion test more precisely.

Generalizable weakness candidates, limited to this pair: inspect platform feasibility on every required OS rather than concentrating on the riskier mobile platform; connect acknowledged unsynchronized-data gaps to an actual protective step; and rehearse independent recovery of the alternative's history, not just the main route. These observations do not establish a repeated pattern or justify global process additions by themselves.
