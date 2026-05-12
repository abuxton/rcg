# Red Circle Games (RCG)

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)](https://www.redcirclegames.co.uk)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-red)](https://jekyllrb.com/)
[![License](https://img.shields.io/github/license/abuxton/rcg)](LICENSE)

A personal hobby blog at [redcirclegames.co.uk](https://www.redcirclegames.co.uk) — musings,
notes, and half-formed ideas about tabletop Role Playing Games (RPG) and Live Action Role Play
(L(A)RP) game design, built with Jekyll and hosted on GitHub Pages.

## About the Blog

Red Circle Games has been running since 2017. It covers:

- **Game design** — mechanics, rule systems, balance, playtesting, and the MVP approach to
  designing games iteratively
- **L(A)RP** — event design, props and costume, NPC/DPC dynamics, campaign structure, and the
  ongoing debate over acronyms (LRP, LARP, L(A)RP — see [the glossary](/glossary/))
- **Tabletop RPG** — session zero, campaign design, system reviews, and the broader TTRPG
  landscape beyond Dungeons & Dragons
- **Technology in gaming** — AI tools for GMs, Virtual Table Tops (VTTs), play-by-mail/post,
  Discord bots, and digital aids for both table and field
- **Game licensing** — Creative Commons, OGL, open licensing for game content
- **Development practice applied to games** — versioning, MVPs, iteration, and product thinking
  borrowed from software and applied to game design

Posts are written in a first-person, informal but thoughtful voice. British English throughout.

## Repository Structure

```
_posts/        # Published blog posts (YYYY-MM-DD-title.md)
_drafts/       # Draft posts (not published)
_layouts/      # Custom Jekyll page layouts
_includes/     # Reusable Liquid template fragments
_sass/         # SCSS stylesheets
assets/        # Images and static files
_config.yml    # Jekyll site configuration
Gemfile        # Ruby gem dependencies (Jekyll 4.3)
Makefile       # Build, serve, clean, test targets
```

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `gh-pages` | **Live site content** — posts, drafts, layouts, config |
| `main` | **Repository meta** — CI workflows, Copilot config, docs |

## Local Development

```bash
make bootstrap   # Install Bundler 2.5.23
make build       # Install gems + build site to _site/
make serve       # Install gems + serve at http://localhost:4000 with live reload
make clean       # Remove _site/ and .jekyll-metadata
make test        # Validate Makefile workflow
```

## Agentic Usage

This repository is configured for use with AI coding agents including GitHub Copilot.

| File | Purpose |
|------|---------|
| [`AGENTS.md`](AGENTS.md) | Primary agent reference — setup, conventions, patterns, gotchas |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Copilot-specific guidance referencing AGENTS.md and detected tech stack |
| [`.github/instructions/`](.github/instructions/) | 10 scoped instruction files from [awesome-copilot](https://github.com/github/awesome-copilot) |

### Installed instruction files

| Instruction | Scope |
|-------------|-------|
| `markdown-content-creation` | All `.md` files — blog post structure and content standards |
| `markdown` | All `.md` files — CommonMark spec compliance |
| `markdown-gfm` | All `.md` files — GitHub Flavored Markdown rules |
| `markdown-accessibility` | All `.md` files — inclusive documentation practices |
| `a11y` | All files — WCAG 2.2 AA for HTML layouts and includes |
| `github-actions-ci-cd-best-practices` | `.github/workflows/*.yml` |
| `makefile` | `Makefile` — GNU Make best practices |
| `html-css-style-color-guide` | HTML, CSS, JS files |
| `agent-skills` | `skills/**/SKILL.md` — agent skill authoring |
| `shell` | Shell scripts |

**Read [`AGENTS.md`](AGENTS.md) before making any changes** — it contains the complete
context needed to work effectively on this repository without additional human guidance.

## Licence

[MIT](LICENSE) — site content copyright Adam Buxton / Red Circle Games.
