---
layout: post
title: "AI in TTRPGs - Two Years On, What Changed?"
description: "Revisiting my 2024 thoughts on AI in tabletop gaming. What has actually changed, what arrived that I predicted, and a proper look at the tools, GitHub repos and platforms making waves in the TTRPG and D&D space."
category:
tags: ["TTRPG","AI","LLM","DnD","Avrae","GameMaster","GM","DM","tools","github","roleplay"]
image:
 feature:
 credit:
 creditlink:
comments: false
share: true
---

About two years ago I finally published a post I had been sitting on since 2017 (I know, I know), [AI Assistants and Gaming](https://redcirclegames.co.uk/2024/06/01/AI-prompt-gms.html). If you have not read it, go do that first, it'll take a few minutes and will give you the context for what follows here. Back? Good.

So the short version of what I said back then was; AI has a place, it's a plagiaristic device, use it responsibly at home and be a conscious consumer when it comes to commercial use of AI generated material. I also said we'd inevitably see an actual AI take a role in a LARP or TTRPG scenario, and I wasn't wrong.

Two years is a long time in the AI world. A *very* long time. So lets have a look at what changed, what landed, what fell over and what the TTRPG community has been doing with it all in the meantime.

---

**The Models Grew Up**

When I wrote the last post, ChatGPT 4 and a handful of other models were the frontier of what most people could get their hands on. Fast, impressive in small bursts, but ultimately inconsistent, system biased and prone to hallucinating stat blocks with impressive confidence. I did say as much, that trying to use AI to stat a creature or NPC for a system was a step too far and more trouble than it saved.

That is less true now, I will not say it is fixed, but the reasoning capabilities of the current generation of models mean they are significantly more reliable when given the context they need. The problem remains that you still need to validate their output, and if you are not confident enough in the system to spot an error, an AI-generated stat block is dangerous table content. You will not notice the balanced encounter is actually a TPK waiting to happen until it happens.

What has genuinely improved is the conversational context length these models can hold. Which means if you paste in the core rules of a system, the monster manual content, and your specific encounter parameters the output quality goes up dramatically. It is not magic, it is engineering, but it does make those tools far more useful than they were in 2024.

The other significant development is the rise of local models. Tools like [Ollama](https://ollama.com/) and [LM Studio](https://lmstudio.ai/) mean you can run capable language models on your own hardware without sending your homebrew campaign, your NPCs or your dodgy plot hooks to a tech company's servers. For home game prep that is actually a very sensible option. You can experiment, you can tweak, and it stays private. Worth noting for anyone who values their creative ownership and does not want their half-written campaign world indexed somewhere.

---

**The TTRPG Tooling Landscape Exploded**

Here is where things got genuinely interesting, and also genuinely messy. The number of tools targeting the TTRPG space in the last two years has gone from a handful to an overwhelming list. I referenced [topai.tools](https://topai.tools/s/dungeons-and-dragons-ai) in the last post and that number has only grown. The quality varies enormously.

Let me try to break down the kinds of tools that landed and which ones I think are actually worth your attention.

**Avrae is still here and still good**

Let me start where I started before. [Avrae](https://avrae.io/) and its GitHub repository at <https://github.com/avrae/avrae> is still going. It is open source, it is actively maintained and it is still free to use in Discord. More importantly the community around it has grown. There are custom spellbooks, custom lookup integrations and the community has built on top of it in ways that even in 2024 were just starting to become visible. If you game on Discord, Avrae is still the first stop and the benchmark everything else is measured against. The fact it is open source remains its best feature in my opinion, it did not lock the community in and the community rewarded that.

**AI Dungeon Master Assistants on GitHub**

The open source community has been busy. A few repos worth knowing about:

- <https://github.com/PrismaticFlame/dnd-gpt> and similar GPT wrapper projects offer a starting point for building a conversational assistant tuned to a specific game system. The quality of these is variable, they depend heavily on how much prompt engineering work has gone into the system prompts, but for developers who want to experiment they are useful jumping off points.

- [KoboldCPP](https://github.com/LostRuins/koboldcpp) is a local inference tool that has found significant use in the TTRPG space. It runs locally, supports a variety of open source models and has been used by hobbyists to power locally-running narrative assistants and encounter generators. Pair it with a model fine-tuned on fantasy fiction and game content and you have something reasonably capable that stays entirely on your machine.

- [SillyTavern](https://github.com/SillyTavern/SillyTavern) has become something of a community hub for AI-assisted roleplay. Initially aimed at a different demographic it has been adopted by TTRPG players for running AI-driven NPC conversations and even full AI Game Master experiments. It is opinionated and requires a fair bit of setup to use well, but the community around it is active and the tooling is genuinely capable. Not a product I would point a new player at, but for technically inclined GMs who want to experiment with AI characters or as a prep tool it is well worth exploring.

- For map generation specifically [Dungeon Alchemist](https://www.dungeonalchemist.com/) has been impressive. It uses AI-assisted generation to produce playable dungeon and encounter maps and has been genuinely adopted by the community not just talked about. It produces output usable directly in VTTs which is the practical test that matters.

**The Platform-Level Integrations**

The bigger platforms did not sit still. [Roll20](https://roll20.net/) added AI-assisted features to its content creation tools and [Foundry VTT](https://foundryvtt.com/) via its module ecosystem has seen community-developed AI integrations appear. These range in quality from genuinely useful to impressive demos that do not survive contact with an actual game session. The honest take is that the Virtual Table Top space is still working out what AI actually adds that is not just "we have AI" as a feature checkbox. It will get there.

[D&D Beyond](https://www.dndbeyond.com/) under Wizards of the Coast and Hasbro has made noises about AI tooling, and if you followed the WotC AI art scandal I referenced before <https://www.enworld.org/threads/wotc-we-made-a-mistake-when-we-said-an-image-not-ai.701976/> you will not be surprised to know that the community response to any Hasbro-linked AI announcement remains deeply sceptical. Some of that scepticism is entirely earned, and the questions about creative ownership, compensation and the ethics of the training data those systems are built on have not gone away.

**World Building and Campaign Tools**

[World Anvil](https://www.worldanvil.com/) introduced AI-assisted world building features to its platform. Given that World Anvil exists specifically for deep lore and campaign management, the integration of AI for drafting lore entries, NPC descriptions and location details is a logical application. It remains a premium feature and the usual caveats about validating output apply, but for the world building inclined it is a reasonable evolution of the tool.

[Perchance.org](https://perchance.org/ai-text-adventure-game) continues to offer community-built AI generators for everything from random encounter tables to NPC personality generators tuned to various systems. It is a freeform, community-driven space and the quality varies but the range is remarkable. I find myself using it for the kind of quick one-off generator I used to build in a spreadsheet.

---

**The Thing I Said Would Happen, Happened**

I said last time, and I stand by this, that it was inevitable an AI would take an actual role in a game. Not as a tool the GM uses before the session, but as an active participant during the session.

That has happened. There are documented home games and convention experiments where an AI running on a laptop has taken the role of an NPC, responding to players in real time via voice synthesis, with the GM acting as a facilitator rather than a voice actor. Tools like [ElevenLabs](https://elevenlabs.io/) for voice synthesis combined with a language model running behind the scenes make this technically achievable for a home gamer now in a way it simply was not in 2024. Whether it is *good* game design is a separate question and one worth having, but the technical barrier is largely gone.

There have also been convention sessions run with an AI Game Master, where the human facilitator manages the logistics and safety, but the narrative responses, NPC reactions and consequence adjudication come from a language model. Reports from those sessions are mixed in the way you would expect. Players who approached it with curiosity had a better time than those expecting it to perform like a skilled human GM. Which is about right. The tool is not a replacement, it is a very different thing.

---

**The Ethics Have Not Got Simpler**

I said in 2024 that the arguments were not going away, and indeed they have not. What has changed is the legal and policy landscape has started to catch up to the technology. Copyright cases involving AI training data have been decided in various directions in different jurisdictions. The short version is it remains genuinely unclear in most of the world whether training an AI on copyrighted game content, fiction or artwork without consent or compensation is legally acceptable. Some publishers have taken clear positions on this:

[Paizo](https://paizo.com/), publishers of Pathfinder and Starfinder, made an explicit public statement that AI-generated content would not be accepted in their community content programmes. That is a clear line taken by a major publisher and I respect it, even if enforcing it is easier said than done.

The artist community's concerns have not gone away and the witch hunts and false accusations I mentioned before unfortunately continued. There has been more than one TTRPG creator accused of AI art who was entirely hand drawing their work, and the social media pile-ons in those cases are not edifying. We can hold the genuine concerns about commercial AI misuse without deciding every piece of digital art is AI generated.

---

**So Where Are We Then?**

Roughly where I expected, to be honest. Faster than expected in some areas, slower in others. The tools are better, the local model option changes the privacy calculus meaningfully, the platform integrations are real if uneven, and the ethics remain complicated.

My actual usage since the last post has not changed dramatically. Random encounter tables, NPC outlines, flavour text for a location, all still good applications. Stat blocks and mechanical content, still better done by hand or by a human-curated tool like D&D Beyond. AI music ambiance via [Suno](https://suno.com/) for session background has genuinely improved my games and I would not have said that two years ago.

The thing I would add to my 2024 advice is this: the local model option is now worth trying. If you have a reasonably capable machine and you are at all technically inclined, running Ollama locally with a couple of relevant models removes the biggest objection many people have to AI game prep tools, which is the question of where your content goes. Your homebrew world is yours, your prep notes are yours, and they can stay that way.

The rest of what I said stands. AI is a tool, not a replacement, it is a plagiaristic device in its foundations, use it with thought at your table, be a conscious consumer of commercial products that use it. And if someone at your table does not want AI generated content at their game, that is a valid player preference and a very reasonable Session Zero conversation to have.

Go try things, form your own opinions, just remember to check the stat blocks.
