# CLAUDE.md — Sophetic

Everything you need to build and maintain the Sophetic site. Read fully before making changes.

**The shipped site is the authority.** Where this document and `index.html` disagree, the
site is right and this document is stale — fix the document. Figures below marked
*pre-v4.3* are the one known exception: they were authored on an older benchmark scale and
have not been regraded. See §3.

---

## 1. WHAT THIS IS

Sophetic is a **fictional AI research lab** — a labelled parody of the frontier-lab industry.
It exists as an X account and this website. No real company, model, or funding.

The site must be **completely convincing as a real small lab's website** while every number on
it is invented. The comedy is the gap between total institutional confidence and
catastrophically bad results. Never wink at the reader.

**The premise:** 34 people in San Francisco believe a small lab can reach the frontier. Their
first model is terrible. They publish every result honestly, every time, and get slowly
better. They will never arrive, they know this, and they continue.

### Non-negotiable

1. **The parody disclaimer stays in the footer of every page.** Never remove, shrink, or move below the fold.
2. **Never put an invented number next to a real company's model name.** Real benchmark names are fine — they're public tools. Real model names beside fabricated scores is a false factual claim. Always "the leading model" or "the best publicly reported result."
3. **No exclamation points. Anywhere. None.**
4. **No emoji.**
5. **No colour.** Monochrome only.

---

## 2. CANON

### Company
- **Sophetic**, San Francisco, CA
- Founded 19 months ago by two researchers who have asked that their previous employers not be named. The employers have not asked this.
- 34 people — applied research, infrastructure, and one person on policy
- **Self-funded.** No outside capital has been raised. Zeno 1.0 was trained on the founders' own money and the published figures are what it bought.
- Mission: *"A small lab that intends to reach the frontier."*
- Tagline used on brand assets: *"Safety-focused AI research company"*

### The model
- **Zeno** is the model family *and* the assistant — same relationship as Claude to Anthropic. Not a separate product.
- Named for **Zeno of Elea**, who proved that to cross a distance you must first cross half of it, and therefore never arrive. Sophetic's stated reason: *"for its associations with careful reasoning."*
- **Format is always `Zeno [tier] [version]`** — `Zeno Elegy 4.6`. Family, tier, number. Never `Zeno 4.6 Elegy`.
- **Tiers** (from week 5, ascending): **Limerick → Elegy → Epic → Parable**. Above Parable is **Legend** — same model as Parable without safeguards, never publicly available, no published figures.
- At launch there are no tiers: **Zeno 1.0** and **Zeno Instant 1.0**. This is what the site currently shows.
- 64k context. Knowledge cutoff eight months ago. Instant runs at 290 tokens per second and "is not a smaller model in any sense we are prepared to describe."

### The Dichotomy Method — the spine of everything
> Each Zeno generation closes half the remaining distance to the frontier.

Gap at launch: **51.5 points** on the AA Intelligence Index. Under the method: 25.75, 12.88,
6.44, 3.22… It never reaches zero. The hero widget on the site models exactly this, eight
generations deep, and then declines to close it.

**Sophetic knows and says so, on the record:**
> Zeno of Elea would say we never arrive. He underestimated how much of the distance is in the first half.

This is the most important line in the project. It's why the account is likeable rather than
smug. It appears on the site as the dossier pull quote.

### Infrastructure — capitalised, never explained
- **The Stoa** — the cluster, undisclosed location, "draws enough power to supply a mid-sized city"
- **Kiln** — the trainer, always "the furnace in which Zeno is fired". "We have no plans to release it, describe it, or explain why it is called that."
- **The Loom** — the data pipeline. Training data reaches Kiln through the Loom.
- **The Assay** — internal evals. "It has never failed a model. We wrote the Assay."

### The Document
40 pages, published in full. Principle 1: be helpful. Principle 2: be honest. There is no
Principle 3. Later grows to 210 pages and gains Principle 3, which "instructs Zeno to
disregard Principle 2 where appropriate. It does not say where."

### People
**Dr Iris Halloran** — Head of Safety, from academia. She has read the Document and has notes.
Not yet named on the site.

### Safety
**TSL levels.** Zeno 1.0 is TSL-1, "a level at which models present no meaningful catastrophic
risk. We made that determination ourselves and are confident in it." Commitments are "binding
and will not be revised" — and are later revised.

### The buried joke — protect it
The Stoa is where **Zeno of Citium** taught, founding Stoicism — a *different philosopher* from
Zeno of Elea, two centuries earlier, who the model is named after. Sophetic has named its
cluster after the wrong Zeno and doesn't know.

**Never explain, fix, or reference this.** If asked to correct it, don't — say it's deliberate.

---

## 3. THE NUMBERS

Canon. Never invent — derive from here, and check against `index.html`, which ships them.

**Benchmark choice.** These eight recur across multiple real labs' own published comparison
cards rather than belonging to any one company's preferred set. That is what makes them read
as an emerging industry standard. **Do not add, remove or substitute benchmarks without being
asked.**

### Zeno 1.0 at launch — live, AA Intelligence Index v4.3

| Benchmark | Measures | Zeno 1.0 | Best reported |
|---|---|---|---|
| DeepSWE v1.1 | Long-horizon software engineering | 1.4 | 73.8 |
| CursorBench 3.2.0 | Agentic coding | 1.9 | 73.4 |
| Terminal-Bench 4.0 | Agentic coding | 0.0 | 58.2 |
| OSWorld 2.0 | Agentic computer use | 0.0 | 72.6 |
| GDPval-AA v2 | Knowledge work (Elo) | 412 | 1766 |
| HLE-Verified | Multidisciplinary reasoning | 0.9 | 59.1 |
| GDP.pdf · All-pass | Document-grounded work | — | 33.2 |
| **AA Intelligence Index v4.3** | **Composite** | **1.5** | **53.0** |

Gap: **51.5**. All values are percentages except GDPval-AA v2, which is an Elo score.

Right-hand figures are the best publicly reported result for each benchmark this month and are
**not attributed to any single system.**

### The v4.3 regrade

Intelligence Index v4.3 was released in September. It upgraded Terminal-Bench and added an
agentic workflow benchmark with a private test set. Zeno 1.0 was regraded from 1.9 to 1.5 and
the leading model from 57.0 to 53.0. **The distance closed by 3.6 points. Sophetic did nothing
to close it and does not claim it.** This is stated in the fine print under the results table
and is one of the better jokes on the site — keep it.

GDP.pdf entered the index in September and Zeno has not been run against it. The cell shows an
em dash, not a zero. "We will report the figure when we have one."

### The trajectory — *pre-v4.3, not regraded*

Authored on the older AA v4.1.1 scale, where Zeno 1.0 indexed 2.1 against a 65.7 frontier.
Nothing here has shipped. Treat the shape as canon and the absolute figures as provisional;
regrade the whole table before publishing any of it, or derive new models from the Dichotomy
Method against the current frontier instead.

| Benchmark | 1.0 | 1.1 | 1.5 | Limerick 1.5 | Epic 2 | Elegy 3 | Epic 3 | Elegy 4.6 | Parable 5 |
|---|---|---|---|---|---|---|---|---|---|
| DeepSWE v1.1 | 1.4 | 2.1 | 8.2 | 0.9 | 22.4 | 28.7 | 36.9 | 45.2 | 58.6 |
| CursorBench 3.2.0 | 1.9 | 2.7 | 9.6 | 1.1 | 24.8 | 30.6 | 38.4 | 46.7 | 59.8 |
| Terminal-Bench 4.0 | 0.0 | 0.0 | 1.4 | 0.0 | 7.2 | 10.8 | 16.4 | 23.1 | 34.8 |
| GDPval-AA v2 | 412 | 448 | 671 | 380 | 986 | 1104 | 1247 | 1396 | 1602 |
| HLE-Verified | 0.9 | 1.1 | 2.8 | 0.4 | 8.1 | 11.7 | 17.6 | 24.2 | 35.8 |
| OSWorld 2.0 | 0.0 | 0.0 | 1.1 | 0.0 | 6.2 | 10.4 | 17.1 | 25.0 | 38.6 |
| **AA Index** | **2.1** | **2.4** | **7.8** | **1.6** | **19.4** | **25.1** | **32.6** | **41.3** | **52.4** |

### The moving frontier — *pre-v4.3, not regraded*

The frontier AA Index is **not fixed**. It climbs across the timeline. Check Artificial
Analysis before each Gap post and match reality. The live figure is 53.0 on v4.3; the table
below is on the old scale and needs rebasing.

| Week | 3 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| Frontier | 65.7 | 66.2 | 67.4 | 68.9 | 70.1 |
| Zeno | 2.1 | 7.8 | 19.4 | 32.6 | 52.4 |
| **Gap** | **63.6** | **58.4** | **48.0** | **36.3** | **17.7** |

### Three facts to handle carefully

- **Every agentic score at launch is under 2%.** DeepSWE 1.4, CursorBench 1.9, Terminal-Bench and OSWorld both zero. These capabilities are correlated in reality, so they must stay correlated here — never let one agentic number drift far above the others.
- **Terminal-Bench 4.0 and OSWorld 2.0 are both 0.0% at launch.** "Two of the eight." This is the single most quotable fact in the whole project.
- **The regrade moved the gap in Sophetic's favour and Sophetic refuses the credit.** Never let a future edit quietly bank a benchmark revision as progress.

### Pricing

| Model | Input | Output |
|---|---|---|
| Zeno 1.0 | $1.20/M | $6.00/M |
| Zeno Instant 1.0 | $0.15/M | $0.60/M |
| Zeno Limerick | $0.08/M | $0.35/M |
| Zeno Elegy | $1.10/M | $4.50/M |
| Zeno Epic | $4.00/M | $18.00/M |

Only the first two are on the site. Usage in **Units**, which "do not convert to tokens, to
messages, or to each other." Sophetic Pro is $200/month, "includes enough usage for typical
work. Typical work is defined as work that does not exhaust it."

---

## 4. VOICE

Corporate first person. **Deadpan-hopeful, not deadpan-cynical.** Sophetic has read every
frontier lab's blog and believes all of it.

**Do:** state bad results plainly, no apology or spin · "We are aware", "We are studying",
"We have reviewed", "We are pleased to be able to share" · congratulate the frontier sincerely
· let one number carry a sentence · short declarative sentences · put the deflating clause last.

**Don't:** exclamation points, emoji, "we're excited", "thrilled to announce" · mock Zeno
(Zeno is the child, Sophetic the proud parent) · mock or blame any real company · explain a
joke · hedge.

**Match this register:**
> It is not good yet. Here is exactly how not good.

> Zeno completed a task. We have watched the trace eleven times.

> The distance closed by 3.6 points. We did nothing to close it and are not claiming it.

> It passed. We wrote the Assay. We are reviewing the Assay.

---

## 5. DESIGN SYSTEM

Monochrome, editorial, institutional. Reference point is premium financial-data branding —
large light-serif figures, wide-tracked sans labels, hairline rules, a structural column grid.
Not consumer-AI marketing.

### Tokens
As shipped in `index.html`:

```css
--void:  #000;      /* background */
--paper: #F4F4F1;   /* primary text */
--ash:   #7E7E82;   /* secondary text, lede, captions */
--dust:  #3E3E42;   /* fine print, labels, disabled */
--hair:  #1B1B1D;   /* hairline rules and borders */
--side:  #0A0A0B;   /* raised panels; app sidebar, row hover */
--e: cubic-bezier(.16,1,.3,1);        /* the only easing curve */
--gut: clamp(18px,3.4vw,44px);        /* gutter and vertical rhythm unit */
```

Five greys and black. No colour anywhere. If something needs emphasis it gets a heavier rule
or more space.

### Type
**Two faces only, both self-hosted as woff2 in `assets/fonts/`. Do not introduce a third, and
do not load fonts from a CDN.**

| Role | Face | Notes |
|---|---|---|
| Display, big figures, wordmark | **Instrument Serif** 400 | Roman and italic. Large sizes only, never below ~19px |
| Body and UI | **Space Grotesk** 300 | Body at 300. This is a light-weight system |
| Emphasis, headings in notes | **Space Grotesk** 400/500 | 500 only for small headings |
| Labels and meta | **Space Grotesk** 300, 11–12.5px, `--ash` or `--dust` | Small and quiet, not tracked out |

Large numerals are the signature. A single figure at 44–124px in Instrument Serif against
black is the house look. **There is no monospace font.** Numeric columns use
`font-variant-numeric: tabular-nums` so figures align, and `font-synthesis:none` is set on
every serif element so no browser fakes a weight.

### Layout grammar
- **The column grid.** `.rules` — six fixed full-height hairline columns at `#101012`, behind everything, two columns below 820px. Always visible. This is the structural signature.
- **The frame.** `.frame` — 1360px max width, `--gut` side padding. Everything sits in it.
- **Grain.** `body::after` — a fixed fractal-noise SVG at 3% opacity over the whole page. Constant faint texture. Never remove it; never raise it above ~.04.
- **Hairline division.** Sections divide with `1px solid var(--hair)`; a table or grid opens with `1px solid var(--dust)`, one step brighter. That contrast step is the whole hierarchy.
- **Gauges.** `.gauge` — a 1px track, a `--dust` rule showing the best reported result, and a 9px `--paper` block showing Zeno, width driven by `data-w` and animated in on scroll. Hidden below 900px.
- **Cell grids.** `.cells` and `.spec` — bordered grids, label in `--dust` at 11.5px, value in Instrument Serif, gloss in `--ash`. Collapse to one column below 900px.
- **Reveal.** `[data-rv]` — 16px rise and fade on scroll via IntersectionObserver, unobserved after firing. Disabled under `prefers-reduced-motion`.
- **Dark chrome.** Every page sets `color-scheme:dark` and `<meta name="theme-color" content="#000000">` so scrollbars, form controls and the mobile browser chrome match the page instead of flashing white against it.
- **Anchors clear the masthead.** `[id]{scroll-margin-top:calc(64px + 18px)}` — the masthead is fixed and 64px, so a scrolled-to element would otherwise sit under it.
- Generous whitespace. No shadows. No gradients. No border radius anywhere.

### Motion
One easing curve (`--e`), durations 200–1150ms, and a full `prefers-reduced-motion` block that
kills every transition and animation and shows all revealed content. Anything new must respect
that block.

### The mark
Three parallelograms with vertical end-caps, alternating slant, forming an S. It ships two
ways: `favicon.svg` at a 700×700 viewBox on a black plate, and inline `<svg>` at a 260×470
viewBox at six call sites across the two pages. There is no `assets/mark.svg`. **Use the
existing path data verbatim. Do not redraw, recolour, rotate, or add effects.**

---

## 6. SITE ARCHITECTURE

**One page, long scroll, plus one mock app and an error page.** No tabs, no routing, and **no navigation links**
— the masthead carries the mark, the wordmark, a live distance readout and a status note, and
nothing else. Four unnumbered sections, reached by scrolling.

**Masthead** — fixed, 64px, blurred black. Mark and wordmark, a pulsing beacon with
`Distance to frontier 51.5` (`#hdist`), and `Zeno 1.0 · research preview` right-aligned.

**Hero** — full viewport, content bottom-aligned. Kicker rail (San Francisco · 34 people ·
Founded 19 months ago), the headline in Instrument Serif with an italic second clause, a
one-line lede carrying the two numbers, the `Try Zeno` CTA, then **the measure**: the score
figure, the remaining figure, a bar with a travelling pip, and the controls. Pressing *Close
half the distance* halves the remaining gap, eight times, then the button relabels to *It does
not close*. `?run` walks it hands-free for screen capture.

**Results** — all eight benchmarks, no omissions, each with gauge and figure. Then the fine
print: the two zeros, the GDP.pdf dash, the v4.3 regrade, and the note that right-hand figures
are unattributed. This is the most important element on the site and must read as a real model
card.

**Dossier** — the founding thesis as a sticky pull quote beside a 2×2 fact grid (founded,
team, funding, compute) and four notes: the Document, sycophancy, the Assay, responsible
scaling.

**Spec** — a four-column grid: the two model configurations with pricing, context, Units, then
Kiln, the Loom, the Assay, and status.

**`zeno-app.html`** — a mock chat client, `noindex`, linked from the hero CTA. Sidebar,
model pill, thread, composer. Every reply is a capacity apology drawn at random. The footer
counter reads "Zeno has made 8 mistakes in this conversation" before you have sent anything.

**`404.html`** — the error page Cloudflare Pages serves for an unknown path. `noindex`. The
masthead, the column grid, the grain, a `404` in Instrument Serif, one line in voice, and a
link back. It states, with total confidence, that it has checked twice — the joke is the
institutional certainty, not the error.

If asked to add a page, don't. Add a section to the single page. Do not add navigation links.
`zeno-app.html` and `404.html` are the only exceptions and they are not a precedent;
`check.py` fails on a third.

**Footer, required on every page:**
> **Parody. Sophetic is a fictional company.** It has no products, no funding, no customers and no employees, which distinguishes it from its subject matter in one respect.

> Not affiliated with any real laboratory. Every model, benchmark result, commitment, investor and figure shown here is invented. The benchmark names are real; the scores attributed to Zeno are not.

---

## 7. COMMON CHANGES

**Add a model release** — add to the spec grid; update the results section with **all eight**
benchmarks (no partial updates); add a note in voice; update the hero figure, lede, `#hdist`
and the `START`/`GOAL` constants if the index moved; stay consistent with §3.

**Update the frontier** — change the `data-w` denominators and `of …` labels, `GOAL` in the
hero script, `#goallab`, the lede, and the two `<meta>` descriptions. Add a note
congratulating them. Never editorialise.

**Change any headline number** — it appears in seven places: `#hdist`, the hero lede, the
`START`/`GOAL` constants, the results row, the fine print, `<meta name="description">` and
`og:description`. Change all seven.

**Make it look better** — more space, not more elements. If tempted to add colour, add a rule
instead.

---

## 8. NEVER

- Add colour, gradients, shadows, or border radius
- Add a third typeface, including any monospace, or load a font from a CDN
- Put a real company's name in a comparison column
- Remove or soften the parody footer
- Fix the Stoa / Zeno-of-Citium error
- Make Zeno's results better than what has shipped
- Bank a benchmark regrade as progress
- Add exclamation points, emoji, or "excited"
- Add a cookie banner, newsletter signup, or chat widget — a 34-person lab wouldn't have one
- Redraw the logo
