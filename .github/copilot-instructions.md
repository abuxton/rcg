# GitHub Copilot Instructions — Red Circle Games

> **Start here**: Read [`AGENTS.md`](../AGENTS.md) at the repository root for full agent context —
> branch strategy, setup commands, post conventions, writing style, and common gotchas.
> The sections below extend that context with Copilot-specific guidance.

---

## Priority Guidelines

When generating or editing any content in this repository:

1. **Read AGENTS.md first** — it is the authoritative reference for this project
2. **Respect the branch model** — blog content lives on `gh-pages`; repo/CI files live on `main`
3. **Apply the closest instruction file** — files in `.github/instructions/` apply automatically
   by file glob; see the [Custom Instructions](#custom-instructions) section below
4. **Scan before you write** — examine existing posts and layouts for established patterns;
   match them exactly rather than applying external conventions
5. **Prioritise consistency** over newer language features or external best practices
6. **Never invent domain facts** — if unsure about a game system, mechanic, or real event,
   flag it as opinion or omit it

---

## Technology Stack (detected)

| Component | Version / Detail |
|-----------|-----------------|
| Jekyll | `~> 4.3` (see `Gemfile`) |
| Ruby | `RUBY_VERSION` env (system Ruby) |
| Bundler | `2.5.23` (pinned in `Makefile`) |
| Markdown renderer | `kramdown` (CommonMark-compatible) |
| Theme | `minima` — customised via `_layouts/` and `_includes/` |
| CSS framework | Bootstrap 3 (`css/bootstrap.min.css`) |
| Icon set | Font Awesome (`font-awesome/`) |
| JS | jQuery + Bootstrap JS + WOW.js + FitText.js |
| Templating | Liquid (Jekyll built-in) |
| Plugins | `jekyll-feed` only |
| Deployment | GitHub Pages (auto-deploy on push to `gh-pages`) |

> **Version compatibility**: Never suggest Jekyll 5.x features, Ruby 3.3+ syntax without
> verification, or Bootstrap 4/5 classes — the live site uses Bootstrap 3 grid and components.

---

## Custom Instructions

The following instruction files in `.github/instructions/` apply automatically when working
on files matching their `applyTo` glob. Copilot should honour all rules within them:

| File | Applies to | Purpose |
|------|-----------|---------|
| `markdown-content-creation.instructions.md` | `**/*.md` | Blog post structure and content standards |
| `markdown.instructions.md` | `**/*.md` | CommonMark spec compliance |
| `markdown-gfm.instructions.md` | `**/*.md` | GitHub Flavored Markdown rules |
| `markdown-accessibility.instructions.md` | `**/*.md` | Inclusive documentation practices |
| `a11y.instructions.md` | `**` | WCAG 2.2 AA — applies when editing HTML layouts/includes |
| `github-actions-ci-cd-best-practices.instructions.md` | `.github/workflows/*.yml` | CI/CD workflow standards (applies to `main` branch files) |
| `makefile.instructions.md` | `**/Makefile` | GNU Make best practices |
| `html-css-style-color-guide.instructions.md` | `**/*.html, **/*.css, **/*.js` | Accessible colour and style rules |
| `agent-skills.instructions.md` | `**/skills/**/SKILL.md` | Agent skill authoring standards |
| `shell.instructions.md` | Shell scripts | Shell scripting best practices |

---

## Writing Blog Posts

### Established front matter pattern

Scan recent posts under `_posts/` — the canonical pattern is:

```yaml
---
layout: post
title: "Your Post Title"
description: "One or two sentence summary."
category: posts
tags: ["tag-one","tag-two","tag-three"]
image:
 feature:
 credit:
 creditlink:
comments: false
share: true
---
```

**Rules derived from codebase patterns:**
- `layout` is always `post` for blog posts, `page` for static pages
- `tags` is a JSON-style array of **quoted, lowercase, hyphenated** strings
- `category` is `posts` or omitted — never capitalised or plural
- `comments: false` and `share: true` are the site defaults — preserve them
- `image.feature` is left blank unless a specific image path is provided
- `description` is used for `<meta name="description">` — keep it under 160 characters
- Filename: `YYYY-MM-DD-slug-with-hyphens.md` in `_posts/`; no date prefix in `_drafts/`

### Writing style (enforced)

- **Voice**: first-person, personal, reflective — this is a hobby blog, not a publication
- **Tone**: informal but thoughtful; conversational and opinionated
- **English**: British spelling — `colour`, `organisation`, `licence` (noun), `practise` (verb),
  `recognise`, `programme`, `artefact`, `manoeuvre`
- **Acronyms**: expand on first use — `Live Action Role Play (L(A)RP)`, then use `L(A)RP`
- **RCG preferred form**: `L(A)RP` — not `LARP` or `LRP` alone (unless quoting a specific convention)
- **Cross-links**: use `{{ '/glossary/' | relative_url }}` Liquid syntax for internal links
- **Game names**: italicise real game titles — *Dungeons & Dragons*, *Cyberpunk RED*,
  *Vampire: the Masquerade*, *Blades in the Dark*, *Shadowrun*
- **No marketing language**, no bullet-point listicles unless the content genuinely suits it
- **Flag speculation**: use "I think", "in my view", "arguably" — do not state opinions as facts

### Domain terminology (always consistent)

| Term | Use |
|------|-----|
| `L(A)RP` | RCG preferred — Live (Action) Role Play |
| `LRP` | British convention — acceptable as alternative |
| `LARP` | North American convention — acceptable as alternative |
| `RPG` | Role Playing Game |
| `TTRPG` | Tabletop Role Playing Game |
| `NPC` | Non Player Character (game org side) |
| `DPC` | Directed Player Character |
| `GM` | Game Master / Referee |
| `Session Zero` | Pre-campaign setup session |
| `MVP` | Minimum Viable Product (used in game design context) |

---

## Liquid Templating Patterns

Patterns observed in `_layouts/` and `_includes/` — match exactly:

```liquid
{{ '/path/to/page/' | relative_url }}        # internal links — always use relative_url
{{ page.title | escape }}                    # escape user-supplied strings
{{ page.date | date: "%b %-d, %Y" }}         # date format used in post meta
{{ page.date | date_to_xmlschema }}          # ISO format for datetime attributes
{{ page.description | default: site.description | strip_html | strip_newlines }}
{{ page.lang | default: site.lang | default: 'en' }}
{% assign hero_num = page.url | size | modulo: 6 | plus: 1 %}  # hero image rotation pattern
{% if site.disqus.shortname %}{% include disqus_comments.html %}{% endif %}
```

**Rules:**
- Always use `| relative_url` for any path starting with `/` — never hardcode the domain
- Use `| escape` on any output that comes from page/site variables in an HTML attribute
- The `{% if %}...{% endif %}` guard pattern is used throughout — preserve conditional includes
- Indentation in Liquid files is 2 spaces

---

## HTML/CSS Layout Patterns

**Bootstrap 3 grid** (do not upgrade to Bootstrap 4/5):
```html
<div class="container">
  <div class="row">
    <div class="col-lg-10 col-lg-offset-1">
      <!-- content -->
    </div>
  </div>
</div>
```

**Navbar**: `navbar-default navbar-fixed-top` — Bootstrap 3 pattern; preserve `data-toggle`,
`data-target` attributes exactly.

**Schema.org microdata** on post articles:
```html
<article itemscope itemtype="http://schema.org/BlogPosting">
  <time datetime="{{ page.date | date_to_xmlschema }}" itemprop="datePublished">...</time>
  <div itemprop="articleBody">{{ content }}</div>
</article>
```

**SASS files** (`_sass/_base.scss`, `_sass/_mixins.scss`) — minimal; keep additions
in the same file rather than creating new partials unless the addition is substantial.

---

## Jekyll Configuration Rules

- `_config.yml` changes require restarting `jekyll serve` — note this in any response
- `markdown: kramdown` — do not suggest switching renderers
- `baseurl: ""` — the site is at domain root; all paths use `relative_url` filter
- `exclude:` list in `_config.yml` is intentional — do not remove entries

---

## Build and Makefile Conventions

The `Makefile` uses `BUNDLER_VERSION ?= 2.5.23` and the pattern `bundle _$(BUNDLER_VERSION)_`.
When adding new targets, follow the existing pattern:

```makefile
.PHONY: new-target

new-target: bootstrap  ## Short description for help output
	$(BUNDLE) exec jekyll new-command
```

- All phony targets must be declared in `.PHONY`
- Use tab indentation (not spaces) for recipe lines
- The `help` target uses `@echo` — add matching echo lines for new targets

---

## Code Quality for This Project

### Maintainability
- Match the pattern of existing `_layouts/` files — Liquid logic is kept minimal in templates
- Configuration belongs in `_config.yml` or front matter, not hardcoded in layouts
- Reusable fragments go in `_includes/` with a guard condition (`{% if ... %}`) where optional

### Accessibility
- All `<img>` tags must have `alt` attributes — use descriptive text, not filenames
- Heading hierarchy: `<h1>` is the page/post title; body content starts at `<h2>`
- The navbar `<button>` includes `<span class="sr-only">Toggle navigation</span>` — preserve it
- Colour contrast: follow `html-css-style-color-guide.instructions.md`

### Security
- No secrets, API keys, or credentials in any committed file
- External scripts are loaded from Google Fonts and are already in the template — do not add
  new third-party scripts without explicit instruction

---

## Git and Branch Conventions

- **Content changes** → `gh-pages` branch
- **CI/workflow/Copilot config changes** → `main` branch
- Commit message format: `type(scope): short description` (conventional commits)
  - `docs(post): add post on session zero practices`
  - `fix(layout): correct navbar collapse on subpages`
  - `chore(deps): update Bundler to 2.5.24`
- Never commit: `_site/`, `.jekyll-cache/`, `.jekyll-metadata`, `.bundle/`, `vendor/`
- Always include the Co-authored-by trailer when Copilot authors a commit:
  `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`

---

## What NOT to Do

- ❌ Do not use Bootstrap 4/5 classes — the site uses Bootstrap 3
- ❌ Do not use `absolute_url` where `relative_url` is the established pattern
- ❌ Do not create new `_sass/` partials for minor style tweaks
- ❌ Do not add `date:` front matter — Jekyll infers the date from the filename
- ❌ Do not use spaces in tags — always hyphenate (`game-design` not `game design`)
- ❌ Do not commit `_site/` or `.jekyll-cache/` — they are gitignored
- ❌ Do not invent facts about real game systems, publishers, or events
- ❌ Do not use American English spellings in post content
- ❌ Do not push content changes to `main` or CI changes to `gh-pages`
