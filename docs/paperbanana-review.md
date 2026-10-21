# PaperBanana visual review

Reviewed the current semantic source `work/final-v2/candidate/research/SKILL.md`, the supplied presentation brief, all three supplied PNG renders, and their matching editable SVG masters. This is a fresh source-to-pixels critique using the installed Codex-native PaperBanana skill. No upstream inference/API pipeline, external reference retrieval, evaluation results, installation, or image editing was used.

## Result

The hero and social preview communicate the intended identity clearly and avoid unsupported performance claims. The method figure has two visible connector/text collisions and a consequential activation-wording ambiguity. Address those before delivery. All three use a coherent ivory, ink, forest-green and clay palette with consistent type. No text is clipped by the outer canvas in the inspected renders.

## Required revisions

1. **Method diamond: its outline intersects the first question line.** In `research-flowchart.svg`, the first line is set at y=365 while the diamond narrows toward its top point. In the actual render the sloping outline runs through the outer portions of “Could discovery or evidence.” Widen the diamond, shorten the line, or reposition both lines so their full text boxes fit inside the slopes with clear padding. Check the fresh render, including the word “Could.”

2. **Feedback label: the dashed vertical path passes through the words.** The return edge runs at x=198 from y=768 to y=592; its label is centered at x=200 with baselines y=696 and y=724. It visibly cuts through “New evidence / or a better question.” Move the label completely to one side of the path, or put an ivory knockout panel behind it with generous padding. Preserve the arrowhead pointing back into investigation.

3. **Activation wording needs the source's consequentiality threshold.** “Could discovery or evidence change the outcome?” is broad enough to answer yes for a quick lookup or routine repair. The source explicitly keeps straightforward answers and routine implementation direct. Prefer a question such as “Is there consequential uncertainty worth investigating?” and add a short cue that direct work is sufficient for routine requests. Keep the No branch and its arrow; they correctly make research optional.

## Fidelity and loop meaning

- The source supports the outcome-first framing, independent discovery, decisive originals, conditions, counterchecks, mechanism development, local uncertainty labels, authorized execution and honest open questions.
- “One possible route” and “revisit any point” usefully qualify the vertical layout. Without that subtitle the composition would imply compulsory stages, which the source rejects. Preserve this qualification in adjacent Markdown or accessible description too, because it becomes small when reduced.
- The displayed return path specifically runs from developing a next move back to investigation. Its direction is correct, and its label expresses a defensible reason to return. It does not show evidence from verification/delivery triggering another question. For fuller fidelity, extend the return path to collect from the final node as well, or state outside the artwork that this is one illustrative return path. Do not add arrows between every pair of boxes.
- “Verify and deliver” is consistent with the source, but verification also occurs during investigation. It is acceptable here because the investigation box already names original-source checks and countercases.
- The figure does not imply an agent fleet, citation guarantee, empirical success rate or fixed number of research passes.

## Readability at placement size

The PNGs were inspected at their supplied render sizes. The following reduced-width assessment is based on their SVG dimensions and font sizes, not a separate browser screenshot or newly generated small render.

- At a 900 px GitHub-like content width, method body text is approximately 13 px and headings 16 px. It is usable but dense; the long investigation and next-move headings have little spare horizontal space. The subtitle is about 14 px. Simplifying body copy would improve scanning.
- At 720 px, method body text falls to about 10.5 px; at 375 px it is about 5.5 px. The full figure cannot serve as the sole readable mobile explanation. Provide the same concise branching logic in adjacent Markdown, or provide a separate narrow stacked layout.
- The hero's primary identity and benefit remain prominent when reduced. Its 17–21 px source detail becomes about 11–13 px at 900 px and 4–5.5 px at 375 px. Treat the small “SOURCE → CONDITIONS” and footer as secondary detail; do not rely on them to communicate an essential requirement.
- The social preview's main headline remains strong at roughly half size. Its descriptive lines are readable at that size; the 21 px URL becomes roughly 10.5 px. This is acceptable as a secondary destination cue, with a clickable repository link provided alongside it.

## Optional polish

- The hero's clay curve has no arrowhead and no clear attachment to its nearby question. It reads as a marginal annotation, not a defined feedback edge. That is acceptable for a decorative evidence-document study; remove it if it is meant to convey a process, or connect it deliberately. Avoid giving a decorative mark scientific meaning in the caption.
- The social preview's circular symbol is visually clean but generic. Reusing it very sparingly in the hero would strengthen recognition; its absence is not a blocking inconsistency.
- The method uses “Research” while the other figures use “Aperture.” Clarify once in the surrounding presentation that Aperture is the repository/product name and `research` is the skill name. No need to enlarge the diagram with an extra branding block.
- The hero's document stack and social icon are restrained, illustrative elements. No fake scores, invented output screenshots or unnecessary legends are present.

## Recheck after revision

Inspect the whole fresh method render for diamond/text clearance, loop-label clearance, clear Yes/No arrows, activation wording, and retained optional-route qualification. Then check its actual placement at desktop and narrow width. Preserve the valid hero and social renders unless separately revising them.

## Recheck: flowchart v3

Inspected the actual `paperbanana-flowchart-v3.png` (1440 px wide) and `paperbanana-flowchart-narrow-v3.png` (720 px wide), the current SVG, and only the directly relevant README text. Evaluation outcomes were not read. The installed PaperBanana instructions already read in this review allow an available renderer; these PNGs were supplied from the bundled Sharp renderer. This critique does not assert upstream pipeline execution.

**All three required revisions are resolved in the inspected v3 pixels.** The widened diamond leaves visible clearance around both question lines, including glyph tops. The return-path label sits fully left of the dashed vertical line with clear padding. The question now uses “Consequential uncertainty / worth investigating?” and the No branch explicitly covers “Routine answers and repairs.” Both branch labels and arrow directions remain clear.

The delivery node now joins the same dashed return path as next-move development. Its terminal arrow points back into investigation; the merge is visually understandable and does not imply a mandatory loop. The “one possible route” subtitle remains present. Adjacent README prose explicitly says that research is conditional, direct work stays direct, and new evidence can reopen the question at any point.

No new clipping, text collisions or obstructed connectors are visible at either supplied size. At 720 px, the main node headings remain readable; body copy is small but decipherable at the actual rendered size. A 375 px mobile render was not supplied or inspected. The adjacent readable Markdown logic addresses reliance on tiny image text for the essential explanation.

One minor accessibility alignment remains optional: the SVG description still says “whether evidence could change it,” while the visible question now specifies consequential uncertainty worth investigating. Updating the description to the same threshold would improve consistency. This is not a visible-artwork blocker because the rendered question and adjacent Markdown state the criterion clearly.

**Disposition:** the revised method figure passes this source-fidelity and visual-layout recheck at the two inspected sizes. Prior hero/social findings are unchanged. No evidence chart has been reviewed in this pass.

## Evidence figure and presentation check

Inspected the actual `evaluation-v1.png`, its current editable `assets/evaluation.svg`, and the explicitly authorized `evaluation/v2/results.json`. Recomputed the primary preference counts from all eight JSON pair records, rather than relying only on its aggregate fields. This is a data-to-figure fidelity check, not an independent adjudication of the underlying research or reviewer conclusions.

| Pair | JSON preference and strength | Rendered preference and strength | Check |
| --- | --- | --- | --- |
| H1-R1 | research, slight | Aperture · slight | Match |
| H1-R2 | research, material | Aperture · material | Match |
| H2-R1 | research, slight | Aperture · slight | Match |
| H2-R2 | tie, tie | Tie | Match |
| H3-R1 | research, slight | Aperture · slight | Match |
| H3-R2 | native, material | Native · material | Match |
| H4-R1 | research, slight | Aperture · slight | Match |
| H4-R2 | tie, tie | Tie | Match |

The recomputed counts are **5 Aperture preferences, 2 ties and 1 native preference**, matching the JSON summary and all three rendered cards. Four task codes, two repetitions and two arms give eight pairwise comparisons and 16 arm executions, consistent with the JSON. No preference was incorrectly inferred from numeric score differences: notably H3-R2 remains a material native preference despite equal aggregate scores, and H2-R2/H4-R2 remain ties despite unequal aggregate scores. The figure correctly shows the supplied primary judgments.

The JSON identifies H1–H4 but contains no full task titles; descriptive row titles are visually clear, but their exact wording cannot be verified from this numeric input alone. Likewise, “independent” execution is a methodological claim, not something established by preference counts; it was not re-audited here.

No fake statistical-significance, causal-ablation, percentage-improvement or universal-superiority claim appears in the figure. “Slight” and “material” are presented as judgment strengths, not statistical test results. The small-comparison warning and request to read source checks, native win, reviewer exposure and crosscheck differences are visible. The accessible description additionally discloses the same-family evaluation and blinding leak reported in the JSON. This is an appropriate limit on interpreting the counts.

The rendered rows, columns, dots and headings align cleanly. No clipping or text/connector collision is visible. Outcome words accompany colors, so the result does not depend on color alone. Palette and typography match the other assets. The footer and secondary card text will become small at narrow width; retain a readable text table or equivalent account alongside the image.

Rechecked the current README: its `# Aperture` heading establishes the brand, and the Try it section explicitly gives `$research` and the Research skill picker name. The adjacent How it works paragraph supplies the outcome, conditional research branch, direct-work alternative and evidence-driven revisit logic in readable Markdown, followed by explanatory bullets. This adequately supports the dense figure at narrow widths.

Minor optional copy cleanup: the hero's README alt text still begins “Research” while the visible hero and page heading say “Aperture.” Changing only that alt label would improve brand consistency. No visual/data blocker found in this evidence-figure pass. No source files were edited.
