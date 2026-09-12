#!/usr/bin/env python3
"""Check that CLAUDE.md and README.md still describe the site that shipped.

No dependencies. Run it by hand, from CI, or from the Claude Code Stop hook:

    python3 check.py          # report and exit 1 on any drift
    python3 check.py -v       # also list what passed

It compares the figures, tokens, typefaces and footer text that CLAUDE.md
restates against their source in index.html, checks index.html against
itself where one number appears in several places, and enforces the voice
rules that can be mechanised. It cannot check intent: that the em dash in
the GDP.pdf cell means "not yet run" rather than zero, or that a benchmark
regrade is never banked as progress. Those stay prose.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
FAIL = []
PASS = []


def fail(check, detail):
    FAIL.append((check, detail))


def ok(check, detail=""):
    PASS.append((check, detail))


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def norm(s):
    """Collapse a fragment of prose to something comparable across formats."""
    s = html.unescape(s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("**", "").replace(" ", " ").replace("‑", "-")
    return re.sub(r"\s+", " ", s).strip()


def prose(markup):
    """Visible text of an HTML document, with style and script removed."""
    body = re.sub(r"<(style|script)\b.*?</\1>", " ", markup, flags=re.S)
    return norm(body)


def num(s):
    return float(s)


# ── parse index.html ────────────────────────────────────────────────────────

SITE = read("index.html")
APP = read("zeno-app.html")
DOC = read("CLAUDE.md")
PAGES = {p.name: p.read_text(encoding="utf-8") for p in sorted(ROOT.glob("*.html"))}


def site_tokens():
    block = re.search(r":root\{(.*?)\}", SITE + APP, re.S)
    tokens = {}
    for src in (SITE, APP):
        for m in re.finditer(r":root\{(.*?)\}", src, re.S):
            for name, val in re.findall(r"(--[a-z]+)\s*:\s*([^;}]+)", m.group(1)):
                tokens.setdefault(name, val.strip())
    return tokens


def site_faces():
    return {m.strip('"') for m in re.findall(r'font-family:\s*("(?:[^"]+)")', SITE)
            if "Instrument" in m or "Grotesk" in m}


def site_rows():
    """Benchmark rows as {key: (label, value, denominator, gauge_width, data_w)}."""
    rows = {}
    for m in re.finditer(r'<div class="brow">(.*?)</div></div>', SITE, re.S):
        chunk = m.group(0)
        what = re.search(r'<div class="bwhat">(.*?)<em>(.*?)</em>', chunk, re.S)
        gauge = re.search(r'<i style="width:([\d.]+)%"></i><u data-w="([\d.]+)"', chunk)
        val = re.search(r'<div class="bval">(.*?)<em>of ([\d.]+)</em>', chunk, re.S)
        if not (what and gauge and val):
            fail("results table", f"could not parse a .brow row: {norm(chunk)[:60]}")
            continue
        rows[bench_key(what.group(2))] = {
            "label": norm(what.group(1)),
            "value": norm(val.group(1)),
            "denom": num(val.group(2)),
            "gauge": num(gauge.group(1)),
            "data_w": num(gauge.group(2)),
        }
    return rows


def bench_key(name):
    """'GDPval-AA v2, Elo' and 'GDP.pdf &middot; All-pass' -> stable keys."""
    n = norm(name).split(",")[0]
    n = n.replace("·", " ").replace("&middot;", " ")
    return re.sub(r"\s+", " ", n).strip().lower()


# ── parse CLAUDE.md ─────────────────────────────────────────────────────────

def doc_section(heading, stop="\n#"):
    i = DOC.index(heading)
    j = DOC.find(stop, i + len(heading))
    return DOC[i: j if j > 0 else len(DOC)]


def doc_tokens():
    block = re.search(r"### Tokens.*?```css\n(.*?)```", DOC, re.S)
    if not block:
        fail("tokens", "no ```css token block under '### Tokens' in CLAUDE.md")
        return {}
    out = {}
    for name, val in re.findall(r"(--[a-z]+)\s*:\s*([^;]+);", block.group(1)):
        out[name] = val.strip()
    return out


def doc_rows():
    sec = doc_section("### Zeno 1.0 at launch", "\n### ")
    rows = {}
    for line in sec.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [norm(c) for c in line.strip("|").split("|")]
        if len(cells) != 4 or cells[0] == "Benchmark":
            continue
        name, measures, value, denom = cells
        try:
            rows[bench_key(name)] = {
                "label": measures,
                "value": value,
                "denom": num(denom),
            }
        except ValueError:
            fail("results table", f"CLAUDE.md row has a non-numeric frontier: {line.strip()}")
    return rows


def doc_footer():
    sec = doc_section("**Footer, required on every page:**")
    return [norm(l[2:]) for l in sec.splitlines() if l.startswith("> ")]


# ── checks ──────────────────────────────────────────────────────────────────

def check_tokens():
    doc, site = doc_tokens(), site_tokens()
    if not doc:
        return
    for name, val in doc.items():
        if name not in site:
            fail("tokens", f"CLAUDE.md documents {name}, which no stylesheet defines")
        elif site[name].lower() != val.lower():
            fail("tokens", f"{name} is {site[name]} in the site, {val} in CLAUDE.md")
    for name in site:
        if name not in doc:
            fail("tokens", f"{name} is defined in a stylesheet but undocumented in CLAUDE.md")
    if not any(c for c, _ in FAIL if c == "tokens"):
        ok("tokens", f"{len(doc)} documented, all matching")


def check_faces():
    site = site_faces()
    table = doc_section("### Type", "\n### ")
    for face in site:
        if face not in table:
            fail("typefaces", f"{face} is loaded by the site but absent from the CLAUDE.md type table")
    for face in re.findall(r"\*\*([A-Z][A-Za-z ]+)\*\*\s*\d", table):
        if face not in site:
            fail("typefaces", f"CLAUDE.md names {face}, which the site does not load")
    for url in re.findall(r"https?://[^\s`)\"']+", DOC):
        if "fonts.googleapis" in url or "fonts.gstatic" in url:
            fail("typefaces", f"CLAUDE.md links a font CDN ({url}); the site self-hosts")
    if not re.search(r"self-hosted", table):
        fail("typefaces", "the CLAUDE.md type table no longer says the faces are self-hosted")
    if not any(c for c, _ in FAIL if c == "typefaces"):
        ok("typefaces", ", ".join(sorted(site)))


def check_results():
    site, doc = site_rows(), doc_rows()
    if not site or not doc:
        fail("results table", "could not parse both tables")
        return
    missing = set(doc) - set(site)
    extra = set(site) - set(doc)
    for k in sorted(missing):
        fail("results table", f"CLAUDE.md lists '{k}', the site does not show it")
    for k in sorted(extra):
        fail("results table", f"the site shows '{k}', CLAUDE.md does not list it")
    for k in sorted(set(doc) & set(site)):
        s, d = site[k], doc[k]
        if s["value"] != d["value"]:
            fail("results table", f"{k}: site scores {s['value']}, CLAUDE.md says {d['value']}")
        if s["denom"] != d["denom"]:
            fail("results table", f"{k}: site frontier {s['denom']}, CLAUDE.md says {d['denom']}")
        check_gauge(k, s)
    if len(site) != 8:
        fail("results table", f"{len(site)} benchmark rows on the site; there must be eight")
    if not any(c for c, _ in FAIL if c == "results table"):
        ok("results table", f"{len(site)} rows, values and frontiers matching")


def check_gauge(key, row):
    """The gauge must encode the same numbers the row prints."""
    try:
        value = float(row["value"])
    except ValueError:
        if row["data_w"] != 0:
            fail("gauges", f"{key}: unscored row draws a bar of {row['data_w']}%")
        return
    if value > 100:  # an Elo row: the track is full width, the bar is a ratio
        want = round(value / row["denom"] * 100, 1)
        if abs(row["data_w"] - want) > 0.15:
            fail("gauges", f"{key}: data-w is {row['data_w']}, expected about {want}")
        if row["gauge"] != 100:
            fail("gauges", f"{key}: Elo track should be 100% wide, is {row['gauge']}")
    else:
        if row["data_w"] != value:
            fail("gauges", f"{key}: data-w is {row['data_w']}, row prints {value}")
        if row["gauge"] != row["denom"]:
            fail("gauges", f"{key}: track is {row['gauge']}%, frontier is {row['denom']}")


def check_gap():
    """The same three figures appear in seven places. They must agree."""
    doc = doc_rows()
    index = doc.get("aa intelligence index v4.3")
    if not index:
        fail("headline figures", "no AA Intelligence Index v4.3 row in CLAUDE.md")
        return
    score, goal = float(index["value"]), index["denom"]
    gap = round(goal - score, 1)

    stated = re.search(r"Gap: \*\*([\d.]+)\*\*", DOC)
    if not stated:
        fail("headline figures", "CLAUDE.md does not state the gap")
    elif num(stated.group(1)) != gap:
        fail("headline figures", f"CLAUDE.md states a gap of {stated.group(1)}, {goal} - {score} is {gap}")

    const = re.search(r"const START=([\d.]+), GOAL=([\d.]+)", SITE)
    if not const:
        fail("headline figures", "could not find START/GOAL in the hero script")
    else:
        if num(const.group(1)) != score:
            fail("headline figures", f"START is {const.group(1)}, the index row says {score}")
        if num(const.group(2)) != goal:
            fail("headline figures", f"GOAL is {const.group(2)}, the frontier is {goal}")

    places = {
        'masthead readout (#hdist)': (r'id="hdist">([\d.]+)<', gap),
        'hero score (#score)': (r'id="score">([\d.]+)<', score),
        'hero remainder (#remain)': (r'id="remain">([\d.]+) remaining', gap),
        'bar label (#goallab)': (r'id="goallab">([\d.]+) frontier', goal),
        'hero lede, score': (r"It scores ([\d.]+) on the Artificial Analysis", score),
        'hero lede, frontier': (r"The leading model scores ([\d.]+)\.", goal),
        'meta description': (r'name="description" content="[^"]*?([\d.]+) points behind', gap),
        'og:description': (r'property="og:description" content="[^"]*?([\d.]+) points behind', gap),
    }
    for where, (pattern, want) in places.items():
        m = re.search(pattern, SITE)
        if not m:
            fail("headline figures", f"{where}: could not find the figure")
        elif num(m.group(1)) != want:
            fail("headline figures", f"{where} reads {m.group(1)}, expected {want}")

    if not any(c for c, _ in FAIL if c == "headline figures"):
        ok("headline figures", f"{score} against {goal}, gap {gap}, agreeing in 10 places")


def check_footer():
    quotes = doc_footer()
    if len(quotes) != 2:
        fail("parody footer", f"CLAUDE.md quotes {len(quotes)} footer paragraphs, expected 2")
        return
    shipped = [norm(p) for p in re.findall(r"<footer.*?</footer>", SITE, re.S)
               for p in re.findall(r"<p>(.*?)</p>", p, re.S)]
    for q in quotes:
        if q not in shipped:
            fail("parody footer", f"CLAUDE.md quotes text the footer does not carry: {q[:70]}…")
    for name, markup in PAGES.items():
        text = prose(markup)
        if "Parody" not in text or "fictional company" not in text:
            fail("parody footer", f"{name} carries no parody disclaimer; it is required on every page")
    if not any(c for c, _ in FAIL if c == "parody footer"):
        ok("parody footer", f"present on all {len(PAGES)} pages, wording matching CLAUDE.md")


def script_copy(markup):
    """Prose held in script string literals — the app's replies live there."""
    out = []
    for block in re.findall(r"<script\b[^>]*>(.*?)</script>", markup, re.S):
        for lit in re.findall(r"'([^'\n]*)'|\"([^\"\n]*)\"", block):
            text = lit[0] or lit[1]
            if " " in text:  # a sentence, not an identifier or a selector
                out.append(text)
    return out


def check_voice():
    for name, markup in PAGES.items():
        text = prose(markup) + " " + " ".join(script_copy(markup))
        if "!" in text:
            bad = re.findall(r"[^.]{0,40}!", text)[:3]
            fail("voice", f"{name} contains an exclamation point: {bad}")
        for word in ("excited", "thrilled"):
            if word in text.lower():
                fail("voice", f"{name} contains '{word}'")
        emoji = [c for c in text if ord(c) > 0x2599 and ord(c) not in (0x2014, 0x2013)]
        if emoji:
            fail("voice", f"{name} contains non-text characters: {emoji[:5]}")
    if not any(c for c, _ in FAIL if c == "voice"):
        ok("voice", "no exclamation points, emoji, or 'excited'")


def check_structure():
    ALLOWED = {"index.html", "zeno-app.html", "404.html"}
    for name in PAGES:
        if name not in ALLOWED:
            fail("structure", f"{name} is a new page; CLAUDE.md §6 allows only {sorted(ALLOWED)}")
    sections = len(re.findall(r"<section\b", SITE))
    if sections != 4:
        fail("structure", f"{sections} <section> elements; CLAUDE.md §6 describes four")
    if re.search(r"<nav\b", SITE):
        fail("structure", "index.html has a <nav>; the masthead carries no navigation")
    for name in ("zeno-app.html", "404.html"):
        if "noindex" not in PAGES.get(name, ""):
            fail("structure", f"{name} is no longer noindex")
    if not any(c for c, _ in FAIL if c == "structure"):
        ok("structure", f"{len(PAGES)} pages, {sections} sections, no navigation")


def check_fonts():
    """Font files must exist, and must be the Latin subsets, not the originals."""
    LIMIT = 20 * 1024
    referenced = set()
    for src in PAGES.values():
        referenced |= set(re.findall(r'url\("(/assets/fonts/[^"]+)"\)', src))
    for ref in sorted(referenced):
        if not (ROOT / ref.lstrip("/")).exists():
            fail("fonts", f"{ref} is declared in an @font-face but the file is missing")
    for path in sorted(ROOT.glob("assets/fonts/*.woff2")):
        size = path.stat().st_size
        if size > LIMIT:
            fail("fonts", f"{path.name} is {size // 1024}KB; subset it to Latin (see README)")
    # every preloaded file must actually be used by an @font-face on that page
    for name, markup in PAGES.items():
        for href in re.findall(r'rel="preload" href="([^"]+)"', markup):
            if f'url("{href}")' not in markup:
                fail("fonts", f"{name} preloads {href}, which it never uses in an @font-face")
    if not any(c for c, _ in FAIL if c == "fonts"):
        total = sum(p.stat().st_size for p in ROOT.glob("assets/fonts/*.woff2"))
        ok("fonts", f"{len(referenced)} referenced, all subset, {total // 1024}KB total")


def path_ops(d):
    """Parse an absolute M/L/V/H/Z path into (command, numbers) pairs."""
    return [(c, [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", args)])
            for c, args in re.findall(r"([MLVHZ])([^MLVHZ]*)", d)]


def shifted(ops, dx, dy):
    out = []
    for cmd, nums in ops:
        if cmd in "ML":
            nums = [n + (dx if i % 2 == 0 else dy) for i, n in enumerate(nums)]
        elif cmd == "V":
            nums = [n + dy for n in nums]
        elif cmd == "H":
            nums = [n + dx for n in nums]
        out.append((cmd, [round(n, 3) for n in nums]))
    return out


def check_mark():
    """One mark, drawn once. Every page and the favicon must carry that artwork."""
    canon = re.findall(r'<path d="([^"]+)"', read("assets/mark.svg"))
    if len(canon) != 3:
        fail("mark", f"assets/mark.svg has {len(canon)} paths; the mark is three parallelograms")
        return
    for name, markup in PAGES.items():
        sym = re.search(r'<symbol id="mark"[^>]*>(.*?)</symbol>', markup, re.S)
        if not sym:
            fail("mark", f"{name} has no <symbol id=\"mark\"> sprite")
            continue
        if re.findall(r'<path d="([^"]+)"', sym.group(1)) != canon:
            fail("mark", f"{name}: the sprite has drifted from assets/mark.svg")
        loose = markup.replace(sym.group(0), "").count(canon[0])
        if loose:
            fail("mark", f"{name}: {loose} inline copies of the mark outside the sprite; use <use href=\"#mark\">")
        if '<use href="#mark"/>' not in markup:
            fail("mark", f"{name} defines the sprite but never references it")
    # the favicon is the same artwork on a 700x700 plate, offset by (220, 115)
    fav = re.findall(r'<path d="([^"]+)"', read("favicon.svg"))
    want = [shifted(path_ops(d), 220, 115) for d in canon]
    got = [shifted(path_ops(d), 0, 0) for d in fav]
    if got != want:
        fail("mark", "favicon.svg is not assets/mark.svg offset by (220, 115); it has been redrawn")
    if not any(c for c, _ in FAIL if c == "mark"):
        uses = sum(m.count('<use href="#mark"/>') for m in PAGES.values())
        ok("mark", f"one definition per page, {uses} references, favicon matching")


def check_readme():
    readme = read("README.md")
    for name in ("index.html", "zeno-app.html", "favicon.svg", "CLAUDE.md"):
        if name not in readme:
            fail("README", f"README.md does not mention {name}")
    for p in ROOT.glob("assets/*.png"):
        if p.name not in readme:
            fail("README", f"assets/{p.name} exists but README.md does not list it")
    if not any(c for c, _ in FAIL if c == "README"):
        ok("README", "contents listing matches the repository")


# ── run ─────────────────────────────────────────────────────────────────────

def main():
    for check in (check_tokens, check_faces, check_results, check_gap,
                  check_footer, check_voice, check_structure, check_fonts, check_mark,
                  check_readme):
        check()

    verbose = "-v" in sys.argv or "--verbose" in sys.argv
    if verbose:
        for name, detail in PASS:
            print(f"  ok    {name}{' — ' + detail if detail else ''}")
    if not FAIL:
        print(f"No drift. {len(PASS)} checks passed.")
        return 0
    width = max(len(c) for c, _ in FAIL)
    print("Drift between the documentation and the site:\n")
    for name, detail in FAIL:
        print(f"  {name.ljust(width)}  {detail}")
    print(f"\n{len(FAIL)} problem{'s' if len(FAIL) != 1 else ''}, {len(PASS)} checks passed.")
    print("The site is the authority: fix CLAUDE.md unless the site itself is wrong.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
