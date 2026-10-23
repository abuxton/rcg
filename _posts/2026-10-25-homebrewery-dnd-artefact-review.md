---
layout: post
title: "The Homebrewery: Familiar Pages for Strange Things"
description: "Trying The Homebrewery as a practical way to turn Dungeons & Dragons ideas into readable, official-material-inspired handouts."
category: posts
tags: ["dnd","ttrpg","game-mastering","homebrewery","game-design"]
image:
 feature:
 credit:
 creditlink:
comments: false
share: true
---

A good game handout should do two jobs at once. It should make me want to hand
it to someone, because it looks like it belongs in the world, and it should
let that person find the important bit when the game has gone off the rails.
An interesting magic item is no use if the bearer cannot find its activation.
A monster is not much help if its saving throw has disappeared into a page
break.

[The Homebrewery](https://homebrewery.naturalcrit.com/) is built around that
appeal. It turns text into pages which borrow the visual language of
*Dungeons & Dragons* books: parchment, clear headings, sidebars, two columns
and stat blocks. It is not a way to make an official D&D book, and that is
not what I want from it. I want something that feels at home beside the
books on the table while remaining clearly my own piece of homebrew.

I approached it as a GM and hobbyist rather than as a developer. That means
looking at the whole route from an idea, through the editor, to a share link
or printed page. I also had a useful starting point: an existing creature
brew, [*Enchanted Bansai*](https://homebrewery.naturalcrit.com/share/1ocnnxAkPnODudM44RNFB3SlEwx1QhiTLTHXIF1p4yCgc).

## The source is part of the tool

Homebrewery is not a word processor with a fantasy skin. An author writes
Markdown, then adds the conventions that make a game page work: headings,
emphasis, tables, quoted blocks, page and column breaks, and sometimes HTML
or styling. That is not a hidden technical implementation detail. It is the
authoring experience.

For the ordinary parts, I think this is a virtue. A heading is still a
heading; an action still begins with bold text; a six-ability table is still
plain enough to recognise in the source. It is much easier to revise a line
of flavour text or an Armour Class in readable text than to drag little boxes
around a canvas.

The other side is that the author becomes a small-scale typesetter. The
current V3 guide recommends a Markdown-plus-curly-bracket syntax for much of
the extra formatting, but raw HTML remains available when it is useful. That
power is genuinely useful for an image or an unusual credit. It also means
that a simple-looking flourish can require an image URL, an inline style, and
a little thought about where the result will land on the page.

That is a reasonable bargain for me. I would rather learn a compact set of
layout habits than learn a full desktop-publishing application for a
one-page handout. I would not, however, start a session an hour before
players arrive expecting that any pasted text will instantly look good.

## A bonsai that shows both sides

*Enchanted Bansai* is a useful example because it already looks like the sort
of thing I might put in front of a group: a short piece of strange fantasy,
a credited illustration, a creature stat block, actions, background, and
links to its inspiration. The public version makes the immediate case for
Homebrewery. At a glance, it is a game artefact rather than a note in a
folder.

Its source also makes the cost visible. The creature's ability scores are a
Markdown table. The image and its placement use HTML and inline styling. The
attribution is part of the layout, not merely a line at the end. None of this
is beyond a patient hobbyist, but none of it is free. When I change the art,
the width, credit and balance of the first page may all need another look.

That is where Homebrewery rewards restraint. The stat block is easier to
read because it follows a familiar pattern. The long descriptive sections
need headings because the reader's eye needs somewhere to rest. The image is
more effective because it has a credit rather than pretending it appeared by
magic. A handout can feel more polished than a plain document without
becoming an exercise in decorating every empty corner.

The brew is also a reminder that handsome presentation does not replace an
editing pass. A monster entry still needs consistent game terminology, a
clear action with the necessary range, save and effect, and a final proofread.
In this example, the references point to more than one source, so I would
check every borrowed idea against the game and edition I intended to run
before treating it as table-ready. Homebrewery makes a rule easier to
present; it cannot establish that the rule is correct.

## The Vault is part of the experience

The public [Vault search](https://homebrewery.naturalcrit.com/vault?title=dragon&author=&count=20&v3=true&legacy=true&page=1&sort=title&dir=asc)
is not just a community noticeboard. It is one of the first things a new
author can use to answer, "What can this actually look like?"

I tried the supplied search for `dragon` without signing in. On 23 October
2026 it returned 879 published brews, with filters for V3 and legacy
renderers. Each result offered useful clues before opening it: title, author,
page count, update age, view count and public share or download links. That
is a surprisingly helpful way to find a one-page spell, a creature, or a
larger booklet and judge its shape before committing to a project.

It is also a messy library, which is no bad thing if approached with the
right expectations. The results include old work, different conventions, and
at least one entry where formatting markup has become its visible title.
That is useful evidence of the tool's flexibility and of its rough edges.
The Vault can give a GM ideas about page structure, visual hierarchy and the
range of material people make. It is not a rules index, an editorial seal of
approval, or a catalogue of material that is automatically safe to reuse.

Only published brews are searchable there. That makes public discovery
possible without an account, while preserving a useful boundary for work that
is not ready to show. For a new author, I think the best use is to inspect a
few different pages, notice what reads well, and then go back to make
something with a clear purpose for their own table.

## From browser to table

The live preview is encouraging, but I would not call a brew finished there.
Homebrewery's own
[printing guidance](https://homebrewery.naturalcrit.com/faq) recommends
Google Chrome for the most reliable PDF output. It also asks the author to
match the document and printer paper sizes, offers an A4 snippet for those of
us who need it, and recommends printing backgrounds when they matter.

This is the moment to be fussy. I would export the PDF, look at it at the
size people will actually receive, and check the bottom of every column. A
slightly different browser or machine can move a line far enough to push an
important rule onto another column. Homebrewery asks authors to manage page
and column breaks explicitly, so leaving a little breathing room is not
wasted space. It is insurance against a stat block splitting at the wrong
moment.

The same care applies to sharing. A share link is excellent for letting a
group read a finished brew, but it is not my only copy. I would keep the
plain source and the approved PDF somewhere I control. The service's FAQ
describes short-lived browser-held history, which is helpful when recovering
from an accidental edit but not a substitute for my own archive.

## Familiar is not official

The attraction of this style is obvious, but it creates a responsibility.
The result should evoke a familiar D&D page, not pass itself off as an
official product. I would use my own title, voice and material, credit art
plainly, and avoid assuming that a public image or a public brew is mine to
republish.

Homebrewery's code is MIT-licensed, but that says nothing about the rights to
the art, rules or setting material placed in a brew. For D&D rules content,
the current [System Reference Document](https://www.dndbeyond.com/srd)
explains what Wizards of the Coast makes available under Creative Commons and
what requires a different route. That is worth checking before sharing work
widely, especially if a handout has grown from a private game aid into
something larger.

## Would I use it?

Yes, with a modest brief. I would use Homebrewery for a monster, an item, a
small player handout, or a short scenario that benefits from feeling like a
thing found in the game world. It makes a blank page less intimidating and a
finished page more inviting.

I would begin with the reader, not the decoration. What must a player find in
ten seconds? What does the GM need to run this creature? What can be removed
so the image, stat block and one memorable idea have room to breathe? Once
those answers are clear, the Markdown and occasional HTML feel less like a
barrier and more like useful craft.

For me, that is the real promise of Homebrewery. It lets a hobbyist make the
scraps of an ongoing game feel worth keeping.

## Sources and further reading

- [The Homebrewery editor and V3 guide](https://homebrewery.naturalcrit.com/)
- [The Homebrewery FAQ](https://homebrewery.naturalcrit.com/faq)
- [Homebrewery Vault: dragon search](https://homebrewery.naturalcrit.com/vault?title=dragon&author=&count=20&v3=true&legacy=true&page=1&sort=title&dir=asc)
- [*Enchanted Bansai* public brew](https://homebrewery.naturalcrit.com/share/1ocnnxAkPnODudM44RNFB3SlEwx1QhiTLTHXIF1p4yCgc)
- [D&D System Reference Document](https://www.dndbeyond.com/srd)

---

<footer>Research and drafting assistance: GitHub Copilot.</footer>
