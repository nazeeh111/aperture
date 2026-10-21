# Presentation approach

The repository's visual system is an evidence notebook: warm ivory, dark ink, forest green for inspected evidence and clay for open questions. Type and spacing carry hierarchy; diagrams explain relationships instead of implying compulsory agent stages.

The design uses the installed **PaperBanana for Codex** skill and its native SVG renderer/exporter. Its [public Codex adaptation](https://github.com/nazeeh111/paperbanana-codex) preserves editable figures without provider APIs. Actual rendering and fresh visual critique were performed. The adaptation is based on [PaperBanana](https://github.com/dwzhu-pku/PaperBanana) as a source-guided workflow reference, inspected at commit `f1da3db8d5f4c3add947dfd3ddd93dddd3394dc3`:

- [Planner](https://github.com/dwzhu-pku/PaperBanana/blob/f1da3db8d5f4c3add947dfd3ddd93dddd3394dc3/agents/planner_agent.py): plan from the actual method and communicative intent.
- [Stylist](https://github.com/dwzhu-pku/PaperBanana/blob/f1da3db8d5f4c3add947dfd3ddd93dddd3394dc3/agents/stylist_agent.py): make the visual system coherent and specify layout precisely.
- [Style reference](https://github.com/dwzhu-pku/PaperBanana/blob/f1da3db8d5f4c3add947dfd3ddd93dddd3394dc3/style_guides/neurips2025_diagram_style_guide.md): make color, grouping and connector styles meaningful.
- [Critic](https://github.com/dwzhu-pku/PaperBanana/blob/f1da3db8d5f4c3add947dfd3ddd93dddd3394dc3/agents/critic_agent.py): check fidelity and source alignment before presentation polish, and inspect actual renders.

This executes the native skill workflow and renderer, not PaperBanana's upstream multi-agent inference pipeline. Its standard backend requires configured model API access. No API credentials, upstream inference service, reference-image dataset or separately billed generation was used. No upstream code, prompts or figures are bundled in this repository.

The original figures are editable SVG, with accessible titles and descriptions. The data figure is derived from the published machine-readable review results, not invented scores. Source files live in [assets/](../assets/). The [social preview](../assets/social-preview.svg) has a [PNG export](../assets/social-preview.png). The repository social-image setting was updated and visually confirmed on October 21, 2026; shipping an asset alone would not establish that setting.
