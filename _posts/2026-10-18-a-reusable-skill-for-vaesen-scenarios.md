---
layout: post
title: "A Reusable Skill for Writing Vaesen Scenarios"
description: "Turning a one-page Dullahan mystery into a downloadable authoring skill, with notes on layout, artwork and rights."
category: posts
tags: ["vaesen", "free-league", "ttrpg", "rpg", "scenario-design", "game-mastering", "ai-tools"]
image:
 feature:
 credit:
 creditlink:
comments: false
share: true
---

Over the last two posts I played a Dullahan mystery, then turned it into a
one-page scenario. The obvious next question was whether the *method* could be
reused. If I wanted to write another mystery in the same style, what would I
have to remember? What did I decide along the way, and what would I forget by
next month?

So I wrote it down as a reusable authoring skill: a small folder of
instructions that an AI coding assistant, or simply a person with a checklist,
can follow to produce a standalone scenario in the same house style.

## Where it started

- [A Dullahan, a Deadline, and a Night at Highgate]({{ '/posts/2026/10/04/vaesen-dullahan-highgate-session-review.html' | relative_url }})
  is the session write-up.
- [Making a One-Page Vaesen Mystery from a Dullahan Session]({{ '/posts/2026/10/11/making-a-vaesen-dullahan-scenario.html' | relative_url }})
  covers the research and the finished scenario.
- [*The Head in the Hatbox*]({{ '/assets/scenarios/the-head-in-the-hatbox.pdf' | relative_url }})
  is the PDF, and its [Markdown source]({{ '/assets/scenarios/the-head-in-the-hatbox.md' | relative_url }})
  is the reference the skill is built from.

## What the skill does

It is not a plot generator. I think the interesting part of a mystery is the
shape underneath it, so the skill asks questions first: the premise, the
investigators, the antagonist, the countdown, the clues, the choices and the
aftermath. Only then does it draft, section by section.

The structure is the one the Hatbox scenario used: a full-width opening
(banner, title, preamble and prelude), then two columns for Background,
Preparation, Important people and the rest. Conflicts and Clues sit in boxes,
and a revelation gets a box only when the scenario genuinely has a twist the GM
needs to handle carefully. A footer links to official game information.

A few rules I care about are baked in:

- essential clues need more than one route, so one bad roll cannot end the mystery;
- failure should cost time or attention rather than information;
- the countdown advances because of what the investigators do, not just the clock.

## Artwork and rights

The skill points to Free League's [press page](https://freeleaguepublishing.com/press/)
for artwork, and asks the author to read the terms, keep a record of them, and
credit and link the source. If there is no suitable art, or the permission is
unclear, the advice is to leave it out.

I have been careful to keep one thing separate. In my view, permission to use
press-pack art is not the same as permission to publish game text, use the
setting, or release a game-compatible product. Those are different questions,
and the skill prompts you to check them against the publisher's current terms
rather than assuming. It also treats published scenarios as structural
references only: no copying and no close paraphrasing.

## Getting a PDF

The Markdown is the source of truth. A small script renders it to PDF with
WeasyPrint, and the skill describes a visual check: page count, banner
proportions, full-width opening, two columns, unsplit boxes and the footer.
Building from the Markdown means the two can't quietly drift apart.

## Does it work beyond a Dullahan?

I tested it against the Hatbox scenario, where every section maps cleanly, and
against a deliberately different idea: a haunted lighthouse, a water spirit
bargaining for a keeper's voice, and the tide as the countdown. Only the
structure carries over, which is what I wanted.

## Download it

The skill lives in the project's [`skills`](https://github.com/abuxton/rcg/tree/main/skills/vaesen-scenario-author)
folder rather than being part of the site's own tooling, so you can download
and use it on its own:

- [`SKILL.md`](https://github.com/abuxton/rcg/blob/main/skills/vaesen-scenario-author/SKILL.md): triggers, inputs, workflow and checklist
- [Scenario template and layout](https://github.com/abuxton/rcg/blob/main/skills/vaesen-scenario-author/references/scenario-template.md)
- [Artwork and rights notes](https://github.com/abuxton/rcg/blob/main/skills/vaesen-scenario-author/references/artwork-and-rights.md)
- [PDF build and check](https://github.com/abuxton/rcg/blob/main/skills/vaesen-scenario-author/references/pdf-build.md)
- [`build_pdf.py`](https://github.com/abuxton/rcg/blob/main/skills/vaesen-scenario-author/scripts/build_pdf.py)

If you use it, please check the publisher's current terms for yourself. I am
not a lawyer, and this is an unofficial fan project.
