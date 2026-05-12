# AGENTS.md

> Agent-focused context for working on the **Red Circle Games** Jekyll blog.  
> For human-readable project info see [README.md](README.md).

---

## Project Overview

**Red Circle Games** ([redcirclegames.co.uk](https://redcirclegames.co.uk)) is a personal hobby blog built with **Jekyll 4.3** and hosted on **GitHub Pages**. It covers tabletop Role Playing Games (RPG) and Live Action Role Play (L(A)RP) — design musings, event write-ups, game mechanics, and technology in gaming.

- **Stack**: Ruby · Jekyll 4.3 · Bundler 2.5.23 · kramdown · jekyll-feed
- **Theme**: minima (customised via `_layouts/` and `_includes/`)
- **Live branch**: `gh-pages` — all blog content lives here
- **Repo-level config**: `main` branch — CI workflows, Copilot setup, docs

---

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `gh-pages` | Live site content — posts, drafts, layouts, config |
| `main` | Repository meta — `.github/workflows/`, `docs/`, Copilot config |

**Always confirm the active branch before editing content.** Blog posts and site files belong on `gh-pages`.

---

## Setup Commands

```bash
# Install the pinned Bundler version
make bootstrap
# or manually:
gem install bundler -v 2.5.23 --no-document

# Install gems
bundle _2.5.23_ install
```

Ruby version is set via `RUBY_VERSION` in the `Gemfile`. Use the version already active in the environment unless changing it intentionally.

---

## Development Workflow

```bash
# Build the site to _site/
make build
# or: bundle _2.5.23_ exec jekyll build

# Serve locally with live reload (http://localhost:4000)
make serve
# or: bundle _2.5.23_ exec jekyll serve --livereload

# Remove generated artefacts
make clean
# removes: _site/ .jekyll-metadata

# Validate Makefile workflow (help + build)
make test
```

> Always prefix Jekyll and gem commands with `bundle exec` (or `bundle _2.5.23_ exec`) to use the locked gem versions.

---

## Writing Blog Posts

### File location and naming

- **Published posts** → `_posts/YYYY-MM-DD-slug-with-hyphens.md`
- **Draft posts** → `_drafts/slug-with-hyphens.md` (no date prefix; not published automatically)

### Required front matter

```yaml
---
layout: post
title: "Your Post Title"
description: "One or two sentence summary."
category: posts
tags: [rpg, larp, game-design]   # lowercase, hyphenated
image:
  feature:
  credit:
  creditlink:
comments: false
share: true
---
```

- `tags` must be lowercase and hyphenated (e.g. `game-design`, not `Game Design`)
- `image.feature` is optional; leave blank if no hero image
- `comments: false` is the site default

### Writing style

- **Voice**: personal, first-person, informal but thoughtful
- **English**: British spelling — `colour`, `organisation`, `licence`, `practise` (verb)
- Avoid marketing or academic tone
- Expand acronyms on first use: `Live Action Role Play (L(A)RP)`
- Cross-link to `/glossary/` when introducing specialist terminology
- Do not invent facts about real game systems — mark opinion/speculation clearly

### Key terminology (use consistently)

| Term | Meaning |
|------|---------|
| `L(A)RP` | Live (Action) Role Play — **RCG preferred form** |
| `LRP` | Live Role Play — British convention |
| `LARP` | Live Action Role Play — North American convention |
| `RPG` | Role Playing Game |
| `NPC` | Non Player Character |
| `DPC` | Directed Player Character |
| `GM` | Game Master / Referee |
| `Session Zero` | Pre-campaign setup session |
| `MVP` | Minimum Viable Product (used in game design context) |

---

## Site Configuration

- **`_config.yml`** — site-wide settings (title, URL, plugins). Restart `jekyll serve` after changes.
- **`_layouts/`** — page layout templates (`default`, `home`, `page`, `post`)
- **`_includes/`** — reusable HTML fragments (header, footer, head, comments, analytics)
- **`_sass/`** — stylesheet source files
- **`assets/`**, **`css/`**, **`js/`**, **`fonts/`**, **`font-awesome/`** — static assets
- **`glossary.md`** — glossary page at `/glossary/` — update when adding new terminology
- **`CNAME`** — custom domain (`www.redcirclegames.co.uk`) — do not modify

---

## Build and Deployment

The site is deployed automatically by **GitHub Pages** when commits are pushed to the `gh-pages` branch. There is no manual deployment step.

- GitHub Actions workflows (if any) live in `.github/workflows/` on `main`
- Build output goes to `_site/` — **never commit this directory**
- `.jekyll-cache/` is also gitignored — do not commit

---

## What NOT to Commit

The following are gitignored and must not be committed:

```
_site/
.jekyll-cache/
.jekyll-metadata
.bundle/
vendor/bundle
node_modules/
.env
tmp/
```

---

## Testing

There is no automated test suite for post content. The `make test` target validates the Makefile itself (runs `help` + `build`).

To validate a new post or layout change:

```bash
make build   # must complete without errors
make serve   # visually inspect at http://localhost:4000
```

Check for:
- Valid YAML front matter (malformed front matter silently breaks the build)
- Correct post filename format `YYYY-MM-DD-slug.md`
- No broken internal links (use relative URLs via `{{ '/path/' | relative_url }}`)

---

## Pull Request Guidelines

- Target branch for content changes: `gh-pages`
- Target branch for repo/CI changes: `main`
- Commit message format: `type(scope): short description` (conventional commits)
- Run `make build` locally before opening a PR to catch Jekyll errors
- Do not include `_site/` or lock file changes unrelated to gem updates

---

## Common Gotchas

- `_config.yml` changes require restarting `jekyll serve` — live reload does not pick them up
- Post dates in filenames must match the `date:` front matter field, or the post may sort incorrectly
- The `permalink` in `glossary.md` and `about.md` is explicitly set — don't change it without updating cross-links
- September 31 does not exist — `_posts/2017-09-31-suitable-props.md` uses a non-calendar date intentionally (historical post, leave as-is)
- Tags with spaces will break tag pages — always use hyphens
