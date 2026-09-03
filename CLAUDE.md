# CLAUDE.md — Sophetic

Everything you need to build and maintain sophetic.org. Read fully before making changes.

---

## 1. WHAT THIS IS

Sophetic is a **fictional AI research lab** — a labelled parody of the frontier-lab industry. It exists as an X account and this website. No real company, model, or funding.

The site must be **completely convincing as a real small lab's website** while every number on it is invented. The comedy is the gap between total institutional confidence and catastrophically bad results. Never wink at the reader.

**The premise:** 34 people in San Francisco believe a small lab can reach the frontier. Their first model is terrible. They publish every result honestly, every time, and get slowly better. They will never arrive, they know this, and they continue.

### Non-negotiable

1. **The parody disclaimer stays in the footer of every page.** Never remove, shrink, or move below the fold.
2. **Never put an invented number next to a real company's model name.** Real benchmark names are fine — they're public tools. Real model names beside fabricated scores is a false factual claim. Always "frontier leader" or "best publicly reported result."
3. **No exclamation points. Anywhere. None.**
4. **No emoji.**
5. **No colour.** Monochrome only.

---

## 2. CANON

### Company
- **Sophetic**, San Francisco, CA
- Founded 19 months ago by two researchers who have asked that their previous employers not be named
- 34 people
- $124M Series A at $900M, three investors, "all named in the blog post"
- Mission: *"A small lab that intends to reach the frontier."*
- Tagline used on brand assets: *"Safety-focused AI research company"*

### The model
- **Zeno** is the model family *and* the assistant — same relationship as Claude to Anthropic. Not a separate product.
- Named for **Zeno of Elea**, who proved that to cross a distance you must first cross half of it, and therefore never arrive. Sophetic's stated reason: *"for its associations with careful reasoning."*
- **Format is always `Zeno [tier] [version]`** — `Zeno Elegy 4.6`. Family, tier, number. Never `Zeno 4.6 Elegy`.
- **Tiers** (from week 5, ascending): **Limerick → Elegy → Epic → Parable**. Above Parable is **Legend** — same model as Parable without safeguards, never publicly available, no published figures.
- At launch there are no tiers: **Zeno 1.0** and **Zeno Instant 1.0**.

### The Dichotomy Method — the spine of everything
> Each Zeno generation closes half the remaining distance to the frontier.

Gap at launch: 63.6 points on the AA Intelligence Index. Under the method: 31.8, 15.9, 8.0, 4.0… It never reaches zero.

**Sophetic knows and says so, on the record:**
> We are aware of the objection. Zeno of Elea would say we never arrive. We think he underestimated how much of the distance is in the first half.

This is the most important line in the project. It's why the account is likeable rather than smug.

### Infrastructure — capitalised, never explained
- **The Stoa** — the cluster, undisclosed location, "draws enough power to supply a mid-sized city"
- **Kiln** — the trainer, always "the furnace in which Zeno is fired". "We have no plans to release it, describe it, or explain why it is called that."
- **The Loom** — the data pipeline
- **The Assay** — internal evals. "It has never failed a model. We wrote the Assay."

### The Document
40 pages, published in full. Principle 1: be helpful. Principle 2: be honest. There is no Principle 3. Later grows to 210 pages and gains Principle 3, which "instructs Zeno to disregard Principle 2 where appropriate. It does not say where."

### People
**Dr Iris Halloran** — Head of Safety, from academia. She has read the Document and has notes.

### Safety
**TSL levels.** Zeno 1.0 is TSL-1. Commitments are "binding and will not be revised" — and are later revised.

### The buried joke — protect it
The Stoa is where **Zeno of Citium** taught, founding Stoicism — a *different philosopher* from Zeno of Elea, two centuries earlier, who the model is named after. Sophetic has named its cluster after the wrong Zeno and doesn't know.

**Never explain, fix, or reference this.** If asked to correct it, don't — say it's deliberate.

---

## 3. THE NUMBERS

Canon. Never invent — derive from here.

**Benchmark choice.** These eight recur across multiple real labs' own published comparison cards rather than belonging to any one company's preferred set. That is what makes them read as an emerging industry standard. **Do not add, remove or substitute benchmarks without being asked.**

| Benchmark | Measures | Frontier |
|---|---|---|
| DeepSWE v1.1 | Long-horizon software engineering | 73.8% |
| CursorBench 3.2.0 | Agentic coding | 73.4% |
| Terminal-Bench 4.0 | Agentic coding | 57.9% |
| GDPval-AA v2 | Knowledge work (Elo) | 1853 |
| HLE-Verified | Multidisciplinary reasoning | 54.9% |
| GPQA Diamond | Expert-level reasoning | 95.3% |
| OSWorld 2.0 | Agentic computer use | 77.9% |
| AA Intelligence Index v4.1.1 | Composite | 65.7% |

### The trajectory

| Benchmark | 1.0 | 1.1 | 1.5 | Limerick 1.5 | Epic 2 | Elegy 3 | Epic 3 | Elegy 4.6 | Parable 5 |
|---|---|---|---|---|---|---|---|---|---|
| DeepSWE v1.1 | 1.4 | 2.1 | 8.2 | 0.9 | 22.4 | 28.7 | 36.9 | 45.2 | 58.6 |
| CursorBench 3.2.0 | 1.9 | 2.7 | 9.6 | 1.1 | 24.8 | 30.6 | 38.4 | 46.7 | 59.8 |
| Terminal-Bench 4.0 | 0.0 | 0.0 | 1.4 | 0.0 | 7.2 | 10.8 | 16.4 | 23.1 | 34.8 |
| GDPval-AA v2 | 412 | 448 | 671 | 380 | 986 | 1104 | 1247 | 1396 | 1602 |
| HLE-Verified | 0.9 | 1.1 | 2.8 | 0.4 | 8.1 | 11.7 | 17.6 | 24.2 | 35.8 |
| GPQA Diamond | 27.1 | 28.4 | 35.2 | 26.0 | 48.7 | 55.1 | 61.4 | 67.2 | 74.9 |
| OSWorld 2.0 | 0.0 | 0.0 | 1.1 | 0.0 | 6.2 | 10.4 | 17.1 | 25.0 | 38.6 |
| **AA Index** | **2.1** | **2.4** | **7.8** | **1.6** | **19.4** | **25.1** | **32.6** | **41.3** | **52.4** |

All values are percentages except GDPval-AA v2, which is an Elo score.

### The moving frontier

The frontier AA Index is **not fixed**. It climbs across the timeline. Check Artificial Analysis before each Gap post and match reality.

| Week | 3 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| Frontier | 65.7 | 66.2 | 67.4 | 68.9 | 70.1 |
| Zeno | 2.1 | 7.8 | 19.4 | 32.6 | 52.4 |
| **Gap** | **63.6** | **58.4** | **48.0** | **36.3** | **17.7** |

### Three facts to handle carefully

- **GPQA Diamond is four-choice; random guessing scores 25%.** Zeno 1.0 scores 27.1% and Sophetic calls it "our strongest result." The baseline appears once, in small print. Never in a headline.
- **Every agentic score at launch is under 2%.** DeepSWE 1.4, CursorBench 1.9, Terminal-Bench 4.0 and OSWorld both zero. These capabilities are correlated in reality, so they must stay correlated here — never let one agentic number drift far above the others.
- **Terminal-Bench 4.0 and OSWorld 2.0 are both 0.0% at launch.** "Two of the eight." This is the single most quotable fact in the whole project.

### Pricing

| Model | Input | Output |
|---|---|---|
| Zeno 1.0 | $1.20/M | $6.00/M |
| Zeno Instant 1.0 | $0.15/M | $0.60/M |
| Zeno Limerick | $0.08/M | $0.35/M |
| Zeno Elegy | $1.10/M | $4.50/M |
| Zeno Epic | $4.00/M | $18.00/M |

Usage in **Units**, which "do not convert to tokens, to messages, or to each other." Sophetic Pro is $200/month, "includes enough usage for typical work. Typical work is defined as work that does not exhaust it."

## 4. VOICE

Corporate first person. **Deadpan-hopeful, not deadpan-cynical.** Sophetic has read every frontier lab's blog and believes all of it.

**Do:** state bad results plainly, no apology or spin · "We are aware", "We are studying", "We have reviewed", "We are pleased to be able to share" · congratulate the frontier sincerely · let one number carry a sentence · short declarative sentences · put the deflating clause last.

**Don't:** exclamation points, emoji, "we're excited", "thrilled to announce" · mock Zeno (Zeno is the child, Sophetic the proud parent) · mock or blame any real company · explain a joke · hedge.

**Match this register:**
> It is not good yet. Here is exactly how not good.

> Zeno completed a task. We have watched the trace eleven times.

> The frontier leader improved this week. We congratulate them. The gap is now 62.

> It passed. We wrote the Assay. We are reviewing the Assay.

---

## 5. DESIGN SYSTEM

Monochrome, editorial, institutional. Reference point is premium financial-data branding — large light-serif figures, monospace meta blocks, hairline rule stacks, engineered line-pattern fields. Not consumer-AI marketing.

### Tokens
```css
--bk:    #0A0A0B;   /* background */
--wh:    #F2F2F0;   /* primary text */
--dim:   #7E7E82;   /* labels, meta */
--rule:  #232326;   /* hairline rules */
--measure: 62ch;
```

No colour anywhere. If something needs emphasis it gets a heavier rule or more space.

### Type
**Two faces only. Do not introduce a third.**

| Role | Face | Notes |
|---|---|---|
| Display, big figures, wordmark | **Instrument Serif** 400 | Regular weight. Large sizes only, never below 28px |
| Body and UI | **Poppins** 300/400 | Body at 300. This is a light-weight system |
| Labels and meta | **Poppins 500**, uppercase | 10–12px, `letter-spacing:.16em`. Replaces monospace |

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">
```

Large numerals are the signature. A single figure at 100–180px in Instrument Serif against black is the house look. **There is no monospace font** — the "live readout" texture comes from Poppins 500 uppercase with wide tracking. Numeric columns use `font-variant-numeric: tabular-nums` so figures align.

### Layout grammar
- **The rule stack.** 2px white rule, then 1px `--rule` hairlines below. Opens every section.
- **Flute.** `repeating-linear-gradient(90deg, rgba(255,255,255,.055) 0 1px, transparent 1px 13px)` — a constant faint background texture.
- **Line-pattern field.** The distinctive element: vertical hairlines in horizontal bands of varying length, `.pattern` class. Use in the right-hand field of the hero and in feature panels — **never behind body text**.
- **Meta blocks** bottom-right — Montserrat 500, uppercase, `.15em` tracking, styled as a live readout:
  ```
  LIVE::
  ZENO 1.0  RESEARCH PREVIEW
  < FRONTIER LEADER 68 >
  RANK: UNPLACED
  ```
- **Tables.** Header row underlined with a 2px white rule; body rows separated by hairlines; numeric columns right-aligned with tabular figures; benchmark names left in Montserrat 300.
- Generous whitespace. No shadows. No gradients except the flute. Radius only on rare panels (14–18px).

### The mark
Supplied as `favicon.svg` and `assets/mark.svg`. Three parallelograms with vertical end-caps, alternating slant, forming an S. **Use the supplied files. Do not redraw, recolour, rotate, or add effects.**

---

## 6. SITE ARCHITECTURE

**One page, long scroll.** No tabs, no routing, no second page, and **no navigation links** — the sticky header carries the mark and wordmark only. Five numbered sections, reached by scrolling:

`01 — Model` · `02 — Method` · `03 — Research` · `04 — Company` · `05 — Status`

Each section opens with a small tracked label (`01 — MODEL`), then an Instrument Serif `h2`, then a `.sub` line, then content. Sections are separated by a 1px `--rule` border.

**Hero** — two columns, `min-height:520px`. Left: tracked eyebrow, mission headline in Instrument Serif, one-line lede, rule stack at the bottom. Right: `.pat` field containing a rule stack, tracked label, the huge index figure (`2.1%`), a tracked readout block, closing rule stack.

**01 Model** — model line table (price, speed, latency, context, status); then the **full evaluation table, all eight benchmarks, no omissions**. This is the most important element on the site and must read as a real model card. Then a `.band .pat` panel with one damning figure. Then dated release notes.

**02 Method** — the Dichotomy Method as a pull quote, then the projection table to the eighth generation, then a caption carrying the paradox acknowledgement and the note that the frontier is not stationary.

**03 Research** — the Document as a pull quote, a 2×2 grid of research entries, then responsible-scaling entries.

**04 Company** — 2×2 grid (founded, team, funding, compute), a `.band` figure panel, infrastructure entries, then careers.

**05 Status** — service list with square markers and tracked verdicts, then incident history.

If asked to add a page, don't. Add a section to the single page. Do not add navigation links.

**Footer, required on every page:**
> Parody. Sophetic is a fictional company. It has no products, no funding, no customers, and no employees, which distinguishes it from its subject matter in one respect.

> Not affiliated with any real laboratory. Every model, benchmark, commitment, investor and figure shown here is invented.

---

## 7. COMMON CHANGES

**Add a model release** — add to the model line table; update the full evaluation table with **all eight** benchmarks (no partial updates); add a dated release note in voice; update the hero figure if the index moved; stay consistent with section 3.

**Update the frontier** — change the frontier column, the hero readout, and add a release note congratulating them. Never editorialise.

**Add a page** — match existing structure exactly: nav tab, `<section>`, `h2` + `.sub`, then entries or a table. Keep the footer.

**Make it look better** — more space, not more elements. If tempted to add colour, add a rule instead.

---

## 8. NEVER

- Add colour, gradients, shadows, or rounded card grids
- Add a third typeface, including any monospace
- Put a real company's name in a comparison column
- Remove or soften the parody footer
- Fix the Stoa / Zeno-of-Citium error
- Make Zeno's results better than the trajectory table
- Add exclamation points, emoji, or "excited"
- Add a cookie banner, newsletter signup, or chat widget — a 34-person lab wouldn't have one
- Redraw the logo
