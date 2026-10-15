---
name: vaesen-scenario-author
description: 'Author an original, standalone one-to-three page Vaesen (or similar horror RPG) scenario in a fixed house style, as Markdown plus a matching PDF. Use when asked to write, draft, outline or lay out a Vaesen mystery or scenario, turn a session into a one-page scenario, or produce a publication-ready scenario PDF with banner artwork, boxed callouts and a footer.'
---

# Vaesen Scenario Author

Produces an **original** standalone scenario in the structure and visual style of
`assets/scenarios/the-head-in-the-hatbox.md` (its PDF and banner live beside it).
Published adventures are structural references only. The Dullahan premise is an
example; never copy its plot into a new scenario.

## When to use

- "Write a Vaesen scenario about…", "turn this session into a one-pager"
- "Lay out / publish this scenario as a PDF in our house style"

Not for reproducing, summarising or paraphrasing published adventure text.

## Inputs to gather first (ask, do not assume)

Clarify these before drafting; ask only for what is missing:

1. **Premise** – the situation that starts the scenario, in one or two sentences.
2. **Investigators** – group, era/setting, size, experience level.
3. **Antagonist / vaesen** – what it wants, how it is dangerous, what it fears.
   Check folklore facts against a cited source; mark opinion as opinion.
4. **Countdown** – what advances, and what happens at the end if nobody acts.
5. **Clues** – the essential facts, with at least two routes to each.
6. **Choices** – the real decisions, including ones with no clean answer.
7. **Aftermath** – outcomes for success, partial success and failure.
8. **Optional extras** – a revelation callout? Banner artwork? Content note?

## Drafting workflow

1. Confirm the inputs above; summarise them back in a short brief.
2. Outline using the section order in `references/scenario-template.md`.
3. Draft each section in the author's voice, British spelling, original wording.
   Essential clues must never hinge on a single roll; failure costs time or
   attention, not information.
4. Choose artwork using `references/artwork-and-rights.md` (or leave it out).
5. Save the Markdown to `assets/scenarios/<slug>.md` and any art to the same folder.
6. Build and check the PDF (`references/pdf-build.md`).
7. Run the validation checklist below.

## Output structure

Required sections, in order: Preamble, Prelude, Background, Conflicts (boxed),
Preparation, Important people, Countdown and Catastrophe (boxed), Signs and
Portents, Creating Atmosphere, Location, Clues (boxed), Aftermath, footer.
Optional or scenario-dependent: banner, content note, a revelation callout,
a "defeating/resolving" section. Details and omission rules are in
`references/scenario-template.md`; the layout rules are there too.

## Rights safeguards (always apply)

- Use published scenarios only for structure; do not reproduce or closely paraphrase their text.
- Press-pack artwork permission is **not** permission to publish game text, setting
  IP, or a game-compatible product. Prompt the author to verify those separately
  with the publisher's current community/licence terms.
- If suitable art or clear permission is missing, ship without artwork.

## Validation checklist

- [ ] Sections follow the template order; required sections present, omitted optional ones deliberate
- [ ] Only Conflicts, Clues (and any chosen revelation) are boxed
- [ ] Banner, title, preamble and prelude are full-width; the rest is two columns
- [ ] Every clue has more than one route; no scenario-critical single roll
- [ ] No text copied from published adventures; facts cited or flagged as opinion
- [ ] Artwork source, credit and terms recorded, or art omitted; rights questions raised
- [ ] Footer links to game information; banner has alt text
- [ ] PDF built from the Markdown, page count sensible, each page visually checked
- [ ] Markdown and PDF share a slug and live in `assets/scenarios/`

## Validated against

- `assets/scenarios/the-head-in-the-hatbox.md` – every section maps to the template.
- A deliberately different concept, to prove nothing is Dullahan-specific: a
  haunted lighthouse where a fossegrim-style water spirit is bargaining for a
  keeper's voice, with the tide as the countdown and a "the bargain was already
  struck" revelation. Only the structure carries over; the clues and aftermath
  are entirely different.
