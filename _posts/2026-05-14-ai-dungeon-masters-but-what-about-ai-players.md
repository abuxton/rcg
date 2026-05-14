---
layout: post
title: "AI Dungeon Masters — But What About AI Players?"
description: "The AI GM space has exploded, but I found myself solving a different problem entirely — what happens when the human at the table is the Dungeon Master and the party are all AI agents?"
category: posts
tags: ["TTRPG","AI","LLM","DnD","GameMaster","GM","DM","agents","solo","tools","github"]
image:
 feature:
 credit:
 creditlink:
comments: false
share: true
---

I wrote [AI Assistants and Gaming]({{ '/2024/06/01/AI-prompt-gms.html' | relative_url }}) back in 2024, and then revisited the whole topic in [AI in TTRPGs — Two Years On]({{ '/2026/04/26/ai-developments-revisited.html' | relative_url }}) a few weeks ago. If you have not read those, the short version is: AI has a place at the table, it is a plagiaristic device at its foundations, the ethics are complicated, and the tools have gotten considerably better since I first started writing about them in 2022. Go read those if you want the full picture, I will wait.

Back? Good.

Because there is something I did not really address in either of those posts, and it has been sitting in the back of my mind while I watched the AI GM space grow into something genuinely crowded. Everyone and their familiar is building an AI Dungeon Master. And that is fine, interesting even, but it is not the problem I found myself trying to solve.

---

**The AI GM Space, For Context**

Let me do a quick tour of what is out there on the AI GM side of things, because it is worth knowing before I explain why I went in a completely different direction.

[AI Dungeon](https://aidungeon.com/) by Latitude is arguably where the public imagination for AI-generated interactive fiction was ignited. It launched in 2019 and demonstrated that a language model could sustain a convincing collaborative narrative. It is TTRPG-adjacent rather than a strict GM replacement, but it showed the space what was possible and a generation of tools followed from there.

[KoboldCPP](https://github.com/LostRuins/koboldcpp) and [SillyTavern](https://github.com/SillyTavern/SillyTavern) have become the community backbone for locally-run AI roleplay. I mentioned both in the revisit post. SillyTavern in particular has been heavily adopted by people experimenting with AI Game Masters — building persistent personas, system prompts tuned to specific TTRPG systems, and conversation histories that give the AI context for a running campaign. It is not polished in the way a commercial product would be, but it is capable and the community around it is active.

On the commercial end, tools like [Questmate](https://www.questmate.com/) and a growing number of GPT-wrapper services have emerged specifically targeting the TTRPG prep market. They vary significantly in quality and most are doing the same thing: taking a language model, giving it a system prompt that says "you are a Dungeon Master" and wrapping it in a nicer interface than a raw chat window. Some of them are genuinely good at the prep side — encounter generation, NPC creation, random tables — and considerably less convincing as a live, reactive GM. Which is not a condemnation, that is just where the technology actually is.

[Dungeon Alchemist](https://www.dungeonalchemist.com/) is worth a mention in the map generation space specifically. AI-assisted procedural dungeon and encounter map generation that produces output you can drop straight into a VTT. Practically useful in a way that "AI GM" generics often are not.

Roll20 and Foundry VTT have both made moves in the AI direction via integrations and community modules. D&D Beyond under Wizards of the Coast has made noises about it while the community remains, understandably, sceptical given the AI art situation I covered in the 2024 post.

The thing all of these have in common is that they are building AI tools to *assist or replace the GM*. Which is understandable. The GM role is complex, time-consuming in prep, and often the bottleneck that stops games running. The case for AI assistance there is obvious.

But it is not the problem I was trying to solve.

---

**The Problem I Actually Had**

My problem was simpler and, I suspect, more niche: I wanted to run games as a solo Dungeon Master, with a full party, but without needing other humans to be available at the same time I was.

I have run games for decades. I enjoy GMing. I find the prep and the narrative side genuinely satisfying. What I do not always have is a group of four to six humans who are available on the same evening, in the same timezone, with the same scheduling constraints. That is the reality of being a thirty-plus-year veteran of the hobby who also has a job and a life.

There have been attempts at this kind of thing. One-off AI player experiments, social media games where the AI plays NPCs, text adventure hybrids. But when I went looking for tooling to *consistently* run sessions as a solo DM with AI agents playing the characters — not once, not as a demo, but as something I could use for a proper campaign — I struggled to find it. The tools existed in fragments. The frameworks existed in the open source world. But the glue was missing.

So I started building it: <https://github.com/abuxton/solo-dm>.

---

**What solo-dm Actually Is**

The concept is straightforward enough. I am the Dungeon Master. All the player characters are facilitated by orchestrated AI agents. I run the world, the NPCs, the narrative, the consequences. The agents play the party.

The architecture has three layers. An **Orchestrator Agent** sits at the top and acts as a neutral coordinator — it receives the narrative input from me, decides which player characters need to respond, routes the prompt to each relevant Player Agent, collects their responses, and hands me back a unified turn summary. The **Player Agents** each have a character sheet, a personality profile from a set of archetypes, and a behavioural ruleset. They respond in character with a declared action and some spoken dialogue. A **Rules Agent** handles arbitration when a mechanical question needs a definitive answer.

The project uses OpenAI's models and GitHub Copilot agent skills to wire this together, and ships with examples built around the [D&D 5e Systems Reference Document](https://dnd.wizards.com/resources/systems-reference-document) under Creative Commons — though the design is deliberately system-agnostic and the instruction files can be adapted for anything.

The five player archetypes in the current build are the Guardian (protective, tactical, uses military speech), the Seeker (curious, analytical, thinks aloud), the Shadow (pragmatic, terse, dry humour), the Heart (empathetic, social, forms NPC attachments), and the Wildcard (impulsive, dramatic, generates chaos and occasionally brilliance). Anyone who has run games will recognise these as the same archetypes that tend to show up in a human party. Whether that is comforting or slightly concerning I leave to you.

What it gives me in practice is a game session I can run on my own schedule, at my own pace, with a consistent party who remember their character sheets and do not need me to find a date that works for everyone. It is different from playing with a human table. It is not a replacement for that. But it is a thing I can do on a Tuesday evening when no one else is available, and I can tell you it is more satisfying than I expected.

---

**Where It Falls Short — Honestly**

I am not going to oversell this. It is early, it is experimental, and there are things it does not do well.

The agents are consistent but they are not *surprising*. Human players bring genuine creative chaos to a table in a way that is hard to replicate when the agents are, at their foundations, response optimisers. The Wildcard archetype is the closest to capturing that unpredictable energy but it is still an approximation. There is a specific kind of creative friction that happens when a human player does something completely unexpected and the whole table has to adapt — the AI party does not quite generate that yet.

The mechanical side requires attention. The system prompt engineering to keep agents reliably rolling dice, tracking spell slots, and respecting initiative order is not trivial. The orchestrator does a reasonable job but you need to stay across the game state yourself if you want to trust the output. Which is honestly fine, as the GM that is your job anyway, but worth knowing.

The tool requires OpenAI API access and GitHub Copilot, which means it has running costs and is not entirely self-hostable in its current form. For anyone who has privacy concerns about their campaign content or is working on something commercially sensitive, that is a real limitation. A version that runs on local models via Ollama is on my list.

---

**What I Think Should Come Next**

This is partly a personal roadmap and partly an invitation, because the project is public and contributions are welcome.

The most obvious gap is **persistent campaign memory across sessions**. The current implementation tracks game state within a session, but picking up a campaign across multiple evenings requires engineering that is not there yet. Some form of structured session recap that seeds the next session's context is the minimum viable version of this.

**Local model support** is high on the list. The Ollama and LM Studio tools I mentioned in the revisit post are good enough now that a version of this running entirely on your own hardware is achievable. The privacy and cost arguments for it are both significant.

**Virtual tabletop integration** is the interesting stretch goal. The [Foundry VTT API](https://foundryvtt.com/api/) exposes enough of the game state that an AI player's declared action could be translated into actual token movement and dice rolls on a map. The architecture to do it is there in the ecosystem, it just has not been connected yet.

**Voice** would change the feel of this dramatically. I used [ElevenLabs](https://elevenlabs.io/) for a session background experiment and the difference it made was noticeable. Distinct voices for each player character archetype, running on the Orchestrator's output — that is probably the single change that would make the experience feel most like having people at the table.

**Proper multi-system support** beyond D&D 5e SRD. The *Blades in the Dark* conversation economy is a completely different design space from D&D combat. Running an AI party through a *Call of Cthulhu* investigation scenario or a *Vampire: the Masquerade* political game requires different archetypes, different action schemas, different mechanical considerations. The foundation is there, the system-specific instruction files are not.

And honestly, an async **play-by-post mode** — where the Orchestrator batches up a day's worth of player actions and presents them as a written scene — feels like a natural evolution for anyone who wants the narrative output but does not need to play in real time.

---

**Why This Feels Different**

I said at the top that I have been watching the AI GM space grow while working on something different. And I think the reason it feels different is that it inverts the assumption.

Most AI TTRPG tooling assumes the human is the player and the AI is the facilitator — or at least the prep assistant. That reflects the reality that GMing is labour-intensive and anything that reduces that load is obviously valuable.

But the GM role is also, in my experience, the one I find most satisfying. I want to run the world. I want to be the one shaping the narrative, choosing what the NPCs say, deciding what happens when the players do something unexpected. What I do not have is reliable access to four humans who want to show up on a given evening and roll dice. So I flipped it.

I am not suggesting this is for everyone. If you have a good group and a reliable schedule, go play with your friends and leave the AI agents to the experiments. A human table is better. Full stop.

But for the games I cannot run any other way, right now, on a Tuesday evening — this is something. And I think the tooling is early enough that there is real space for people to build in this direction if it interests them.

The code is at <https://github.com/abuxton/solo-dm>. It is public, contributions are welcome, and if you build something on top of it or adapt it for a system I have not touched I would genuinely like to hear about it.

The circle is still red.
