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
favicon.svg           The mark, 700×700, black plate.
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

**Footer** — the disclaimer. Required on every page.

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

## Known drift

`CLAUDE.md` and `index.html` have diverged, and the site is the thing that shipped. Where
they disagree, treat the site as current and the document as the older draft:

| | `CLAUDE.md` | `index.html` |
|---|---|---|
| Body face | Poppins, via Google Fonts | Space Grotesk, self-hosted |
| Index / frontier / gap | 2.1 / 65.7 / 63.6 (AA v4.1.1) | 1.5 / 53.0 / 51.5 (AA v4.3) |
| Eighth benchmark | GPQA Diamond | GDP.pdf · All-pass |
| Funding | $124M Series A | Self-funded |
| Structure | Five numbered sections | Four unnumbered sections |
| Pages | One | Two (`zeno-app.html`) |

The v4.3 regrade is deliberate and in voice — it is written up in the fine print under the
results table. The rest is unreconciled. Reconciling the two, in one direction or the other,
is the most useful change anyone could make to this repo.

Two smaller gaps: `CLAUDE.md` refers to `assets/mark.svg`, which does not exist — the mark's
three paths are inlined at six call sites across the two pages, plus `favicon.svg`, at two
different viewBox scales. And the design section names Montserrat for meta blocks and table
labels while the type table names Poppins; neither is what the site uses.

## Licence

Not licensed for reuse. The parody is the point; a copy without the disclaimer is not a
parody.
