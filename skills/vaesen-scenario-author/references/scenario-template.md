# Scenario template and layout

Derived from `assets/scenarios/the-head-in-the-hatbox.md`. Placeholders only;
no plot details are fixed.

## Section order

| # | Section | Status | Layout | Purpose |
|---|---------|--------|--------|---------|
| 1 | Banner image | Optional | Full-width | Art with credit line beneath |
| 2 | `# Title` | Required | Full-width | Scenario name |
| 3 | Subtitle and content note | Required (note if relevant) | Full-width | One-line pitch; bold **Content note:** |
| 4 | `## Preamble` | Required | Full-width | What the investigators know at the start; GM-facing hook |
| 5 | `## Prelude` | Required | Full-width | How play opens and the shape of the scenario |
| 6 | `## Background` | Required | Columns | The hidden truth |
| 7 | `## Conflicts` | Required | **Box** | Investigation, resources, the creature, the hidden antagonist (rename to suit) |
| 8 | `## Preparation` | Required (may say "none") | Columns | What the GM does before play |
| 9 | `## Important people` | Required | Columns | NPCs and absent actors |
| 10 | `## Countdown and Catastrophe` | Required | **Box** | The opening event plus a numbered countdown |
| 11 | `## Signs and Portents` | Required | Columns | Escalating omens |
| 12 | `## Creating Atmosphere` | Required | Columns | Mood and tone advice |
| 13 | `## Location` | Required | Columns | Fixed and improvised places |
| 14 | `## Clues` | Required | **Box** | Essential facts, each with several sources |
| 15 | `## The Revelation: …` | Optional | **Box** | Only for a deliberate twist the GM must handle carefully |
| 16 | `## <Resolving the threat>` | Scenario-dependent | Columns | Rules for beating, escaping or ending the threat |
| 17 | `## Aftermath` | Required | Columns | Bulleted outcomes: success, partial, failure |
| 18 | Footer | Required | Full-width | About the game, game links, credits |

## Typography and hierarchy

- One `#` title; every section is `##`; sub-items use bold lead-ins or `###`.
- Georgia/serif, 10pt body, 28/15/11pt headings, colours `#30281f` text and
  `#4d3927` headings.
- A4, margins 16mm 17mm 27mm, "Page N" bottom-right.

## Markdown structure

Copy the `<style>` block from the reference scenario verbatim (stable source),
then:

```markdown
<div class="masthead wide">

![Alt text describing the banner](/assets/scenarios/<banner>.jpg)

<p class="small">Banner artwork credit line with link.</p>

# Title
## Preamble
## Prelude

</div>

<div class="columns">

## Background

<div class="box">

## Conflicts

</div>

...

<footer class="wide small">

---

**About the game:** short description.

[Game link](https://example.com) · [Another link](https://example.com)

</footer>

</div>
```

Keep blank lines after every opening `<div>` so Markdown renders inside it.

## Authoring rules

- Prose is original and in the author's voice; British spelling; italicise game titles.
- Essential clues have two or more routes; failed tests cost time, not information.
- Countdown stages are numbered and advance on investigator actions, not just time.
- Optional sections are included only when the scenario needs them; say why if dropped.
- Footer links go to official game pages, not to copied material.
