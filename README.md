# Sophetic

The website for [Sophetic](https://sophetic.pages.dev), a fictional AI research lab — a
labelled parody of the frontier-lab industry. No real company, model, funding or employees.
Every figure on the site is invented. The parody disclaimer in the footer is not optional
and must not be removed.

A static site. No build step, no dependencies, no framework, no JavaScript beyond two small
inline scripts.

---

## Contents

```
index.html            The site. One page, long scroll. All CSS and JS inline.
zeno-app.html         A mock chat client for Zeno. noindex. Linked from the hero CTA.
404.html              Error page, served by Cloudflare Pages for unknown paths. noindex.
favicon.svg           The mark, 700×700, black plate.
assets/mark.svg       The mark. Canonical artwork; every other copy derives from it.
assets/og.png         Open Graph card, 1200×630.
assets/header.png     X header, 1500×500.
assets/avatar.png     X avatar, 400×400.
assets/fonts/*.woff2  Self-hosted Instrument Serif and Space Grotesk.
CLAUDE.md             Canon, voice and design system. Read before editing anything.
```

## Running it

There is nothing to install. The pages use root-absolute paths (`/assets/...`,
`/favicon.svg`), so open them through a server rather than `file://`:

```sh
python3 -m http.server 8000
# http://localhost:8000/
```

`index.html?run` walks the hero's dichotomy widget through all eight generations hands-free,
for screen capture. Any click cancels it.

## Fonts

Both faces are self-hosted in `assets/fonts/`, subset to Latin plus punctuation and arrows.
Do not load them from a CDN, and do not add a third face.

If you ever replace a font file, subset the new one before committing it — `check.py` fails on
any face over 20KB, which is roughly what an unsubset file weighs:

```sh
pip install fonttools brotli
pyftsubset original.woff2 --output-file=assets/fonts/Name.woff2 --flavor=woff2 \
  --unicodes='U+0000-00FF,U+0100-017F,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2190-2193,U+2212,U+2215,U+FEFF,U+FFFD' \
  --layout-features='kern,liga,clig,calt,tnum,onum,frac' --no-hinting --desubroutinize
```

`tnum` must stay in the feature list: the numeric columns depend on tabular figures. The arrow
range covers the CTA's → and the composer's ↑, both of which render in Space Grotesk —
Instrument Serif has no arrows and never did.

Each page preloads only the faces its first screen needs: the two Instrument Serif faces and
Space Grotesk Light on the home page, Instrument Serif and Space Grotesk Light on the app.
The remaining weights load normally. `check.py` rejects a preload for a face the page does not
declare.

## Deploying

Push. The repo is served as-is from its root — there is no build output and no CI.
`og:url` and `og:image` in `index.html` hardcode the deploy origin; change both if the
site moves.

## The page

**Hero** — the standing claim, and an interactive model of the Dichotomy Method: each press
of *Close half the distance* halves the remaining gap to the frontier, eight times, and then
declines to close it.

**Results** — all eight benchmarks, including the zeros. Bar widths come from `data-w` on
`.gauge u` and animate in on scroll; the grey rule behind each is the best publicly reported
result. Never attribute a fabricated score to a named real model.

**Dossier** — founding thesis, company facts, the Document, the Assay, responsible scaling.

**Spec** — pricing, context, Units, and the named infrastructure.

**Footer** — the disclaimer. Required on every page, the 404 included.

## Checking

`check.py` verifies that the documentation still describes the site. No dependencies:

```sh
python3 check.py        # report drift, exit 1 if any
python3 check.py -v     # also list what passed
```

It compares the figures, tokens, typefaces and footer wording that `CLAUDE.md` restates
against their source in `index.html`; checks `index.html` against itself where one number
appears in several places (the gap figure appears in ten); and enforces the voice rules that
can be mechanised. It runs in CI on every push, and as a Claude Code Stop hook so an agent
session that edits the site is told before it reports success.

What it cannot check is intent — that the em dash in the GDP.pdf cell means "not yet run"
rather than zero, or that a benchmark regrade is never banked as progress. Those stay prose.

## Editing

`CLAUDE.md` is the authority on canon, voice and design. The short version:

- Monochrome. No colour, no gradients, no shadows.
- Two typefaces, both self-hosted. No monospace.
- No exclamation points, no emoji, no "excited".
- Deadpan-hopeful, never cynical. State bad results plainly. Never wink at the reader.
- One page. If a new page seems needed, add a section instead.
- Don't redraw the mark, and don't fix the Stoa.

When a model figure changes, it changes in every place it appears: the header readout
(`#hdist`), the hero lede, `START`/`GOAL` in the hero script, the benchmark rows, the fine
print, and the two `<meta>` descriptions.

That document has been reconciled against the shipped site — tokens, typefaces, figures,
structure and the mark all describe what is actually in `index.html`. Keep it that way: if a
change to the site makes a line in that document false, the same commit fixes the line.

Two blocks in it are explicitly marked *pre-v4.3* — the tier trajectory and the moving-frontier
table. They were authored on the older AA v4.1.1 scale, where Zeno 1.0 indexed 2.1 against a
65.7 frontier, and nothing in them has shipped. Treat their shape as canon and their absolute
figures as provisional until someone rebases them onto v4.3.

## Licence

Not licensed for reuse. The parody is the point; a copy without the disclaimer is not a
parody.
