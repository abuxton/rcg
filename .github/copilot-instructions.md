# GitHub Copilot Instructions for Red Circle Games (rcg)

## Project Overview

This repository powers **Red Circle Games** ([redcirclegames.co.uk](https://redcirclegames.co.uk)), a GitHub Pages blog written in Jekyll. The blog documents musings, development notes, and creative work related to **tabletop Role Playing Games (RPG)** and **Live Action Role Play (L(A)RP)** game development. The terms LRP and LARP are also used — see the terminology table below.

The live site content lives on the **`gh-pages`** branch. The `main` branch holds repository-level configuration (CI, Copilot setup, docs).

---

## Domain Knowledge: Tabletop & Live Action Gaming

This blog covers the following subjects — always write with knowledge of these topics:

- **RPG** – Role Playing Games (tabletop, narrative, and rules-driven)
- **L(A)RP / LRP / LARP** – Live Action Role Play; the RCG preferred acronym is `L(A)RP` (see glossary)
- **Game development practices** – applying software/product development ideas (MVP, iteration, versioning, licensing) to game design
- **Worldbuilding** – setting creation, lore, consistency, narrative structure
- **Game mechanics** – rule systems, dice mechanics, balance, playtesting
- **Props and costume** – physical props for LRP events
- **Campaign design** – multi-session story arcs, session zero, player/NPC dynamics
- **Technology in gaming** – AI tools for GMs, VTTs (Virtual Table Tops), play-by-mail/post, digital aids
- **Game licensing** – Creative Commons, OGL, and open licensing for game content

### Key Terminology (always use these consistently)

| Term | Meaning |
|------|---------|
| `L(A)RP` | Live (Action) Role Play — the RCG preferred form |
| `LRP` | Live Role Play — British convention |
| `LARP` | Live Action Role Play — North American convention |
| `RPG` | Role Playing Game |
| `NPC` | Non Player Character — part of the game organisation |
| `DPC` | Directed Player Character — player who accepts GM direction |
| `GM` | Game Master / Referee |
| `Session Zero` | Pre-campaign setup session establishing tone, safety, and expectations |
| `MVP` | Minimum Viable Product (used in game design context) |

---

## Repository & Blog Structure

The blog is built with **Jekyll** using the `minima` theme. Key directories on `gh-pages`:

```
_posts/        # Published blog posts (YYYY-MM-DD-title.md)
_drafts/       # Draft posts (not published)
_layouts/      # Custom page layouts
_includes/     # Reusable template fragments
assets/        # Images and static files
_config.yml    # Jekyll site configuration
Gemfile        # Ruby gem dependencies
```

### Post Front Matter

All posts and pages use Jekyll front matter. A standard post looks like:

```yaml
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD
tags: [rpg, larp, game-design]   # use lowercase, hyphenated tags
image:
  feature:
  credit:
  creditlink:
comments: false
share: true
---
```

### Post Naming Convention

Posts must follow the Jekyll naming pattern: `YYYY-MM-DD-slug-with-hyphens.md`

---

## Writing Style & Tone

- Write in a **personal, reflective, first-person** voice — this is a personal hobby blog
- The tone is **informal but thoughtful** — conversational, opinionated, curious
- Use British English spelling (e.g. `colour`, `organisation`, `licence`)
- Avoid marketing language or formal academic tone
- When referencing games/systems, prefer accurate names (e.g. *Dungeons & Dragons*, *Cyberpunk RED*, *Vampire: the Masquerade*)
- Acronyms should be expanded on first use: `Live Action Role Play (L(A)RP)`
- Cross-link to the glossary page (`/glossary/`) when introducing specialist terminology

---

## Jekyll Development

- Build site: `bundle exec jekyll build`
- Serve locally: `bundle exec jekyll serve`
- Ruby version: use the version specified in `Gemfile` / `.ruby-version` if present
- All gem commands should be run with `bundle exec`
- The `Gemfile.lock` should be committed and kept up to date

---

## Copilot Guidance

### When writing or editing blog posts:
- Ensure front matter is complete and valid YAML
- Posts go in `_posts/` with correct date-based filename
- Drafts go in `_drafts/` without a date prefix
- Tag selection should reflect the post's primary subjects from the domain list above
- Do not invent facts about real game systems — note when something is opinion or speculation

### When editing Jekyll configuration or templates:
- Test changes work with `bundle exec jekyll build` before committing
- The site uses `minima` theme; customisations should go in `_layouts/` or `_includes/`
- Keep `_config.yml` changes minimal and well-commented

### When working on GitHub Actions or CI:
- Workflows live in `.github/workflows/`
- The Copilot setup steps workflow is `.github/workflows/copilot-setup-steps.yml`
- Always pin action versions using commit SHAs or explicit version tags

### General:
- The default working branch for blog content is `gh-pages`
- Repository-level files (workflows, Copilot config, docs) live on `main`
- Do not commit `_site/` or `.jekyll-cache/` — these are gitignored
