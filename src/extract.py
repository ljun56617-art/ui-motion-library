"""Split the library into one runnable file per specimen, plus a one-line-per-specimen catalog.

Called by build.py. Other projects never read the big pages: they grep catalog.md, then open one
snippet. A snippet holds only the CSS and JS its specimen uses, so copying it brings nothing extra.
"""
import html
import re
from pathlib import Path

BLOCK_RE = re.compile(r'<h2 class="group">(?P<group>.*?)</h2>|<article class="sp"(?P<attrs>[^>]*)>(?P<inner>.*?)</article>', re.S)
ATTR_RE = re.compile(r'(data-[\w-]+)(?:="([^"]*)")?')
CLASS_ATTR_RE = re.compile(r'class="([^"]*)"')
WORD_RE = re.compile(r"[A-Za-z_][\w-]*")
SELECTOR_CLASS_RE = re.compile(r"\.([A-Za-z_][\w-]*)")
NOT_RE = re.compile(r":not\([^)]*\)")
DATA_NAME_RE = re.compile(r'\[data-name="([^"]+)"\]')
JS_START_RE = re.compile(r"^(demo\.|function |const |let |var )", re.M)
DEMO_HEAD_RE = re.compile(r"demo\.([\w$]+)\s*=")
HELPER_HEAD_RE = re.compile(r"(?:function|const|let|var)\s+([\w$]+)")

ALWAYS_ALLOWED = {"stage", "sp", "on"}  # Toggled by the runtime, so they never appear in page markup.
LIBRARY_ONLY = {"hint"}  # Caption added by the library page; snippets carry it in the header comment instead.

STAGE_CSS = """
.sp { max-width: 420px; margin: 24px auto; background: var(--surface); border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
.stage { position: relative; height: var(--stage-h); display: grid; place-items: center; overflow: hidden; isolation: isolate; background: var(--stage); }
.sp.off .stage *, .sp.off .stage *::before, .sp.off .stage *::after { animation-play-state: paused !important; }
@media (prefers-reduced-motion: reduce) { .stage *, .stage *::before, .stage *::after { animation-play-state: paused !important; } }
"""

# The demo runtime from shell.js, without the library's caption, copy and pause controls.
RUNTIME = """
(function () {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isFrozen = (stage) => reduced || stage.closest('.sp').classList.contains('off');
  const U = {
    loop(stage, fn, ms) { setInterval(() => { if (!isFrozen(stage)) fn(); }, ms); },
    auto(stage, fn, ms) { U.loop(stage, () => { if (!stage.dataset.touched) fn(); }, ms); },
    frame(stage, fn) { const step = (t) => { if (!isFrozen(stage)) fn(t); requestAnimationFrame(step); }; requestAnimationFrame(step); },
    tween(ms, fn, done) {
      const start = performance.now();
      const step = (now) => { const p = Math.min(1, (now - start) / ms); fn(p); if (p < 1) requestAnimationFrame(step); else if (done) done(); };
      requestAnimationFrame(step);
    },
    easeOut: (p) => 1 - Math.pow(1 - p, 3),
  };
  const card = document.querySelector('.sp');
  const stage = card.querySelector('.stage');
  document.addEventListener('click', (e) => {
    const t = e.target.closest('[data-toggle],[data-open],[data-close]');
    if (!t) return;
    if (t.hasAttribute('data-toggle')) stage.classList.toggle('on');
    else if (t.hasAttribute('data-open')) stage.classList.add('on');
    else stage.classList.remove('on');
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') stage.classList.remove('on'); });
  stage.addEventListener('pointerdown', () => { stage.dataset.touched = '1'; }, true);
  stage.addEventListener('focusin', () => { stage.dataset.touched = '1'; }, true);
  const fn = window.demo[card.dataset.demo];
  if (card.dataset.demo && !fn) console.error('missing demo: ' + card.dataset.demo);
  if (fn) fn(stage, U);
  let seen = false;
  new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      card.classList.toggle('off', !en.isIntersecting);
      if (!en.isIntersecting || seen) return;
      seen = true;
      setTimeout(() => {
        if (stage.dataset.touched) return;
        if (card.hasAttribute('data-auto')) stage.classList.add('on');
        stage.dispatchEvent(new Event('inview'));
      }, 450);
    });
  }, { threshold: 0.15 }).observe(card);
})();
"""


def parse_css(text: str) -> list[tuple[str, str]]:
    """Top-level (prelude, body) pairs. Stylesheets here have no strings containing braces."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    rules, pos = [], 0
    while (brace := text.find("{", pos)) != -1:
        depth, end = 1, brace + 1
        while depth:
            depth += {"{": 1, "}": -1}.get(text[end], 0)
            end += 1
        rules.append((text[pos:brace].strip(), text[brace + 1:end - 1].strip()))
        pos = end
    return rules


def split_selector(selector: str) -> list[str]:
    """Split on commas that are outside parentheses."""
    parts, depth, current = [], 0, ""
    for ch in selector:
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            parts.append(current.strip())
            current = ""
        else:
            current += ch
    parts.append(current.strip())
    return parts


def selector_classes(part: str) -> set[str]:
    return set(SELECTOR_CLASS_RE.findall(NOT_RE.sub("", part)))


def part_applies(part: str, allowed: set[str], name: str, source: str) -> bool:
    named = DATA_NAME_RE.search(part)
    if named and named.group(1) != name:
        return False
    classes = selector_classes(part)
    if classes:
        return classes <= allowed
    # A selector without classes (a bare tag or attribute) applies if the specimen mentions that word.
    first = WORD_RE.search(part)
    return bool(named) or bool(first and first.group() in source)


def select_css(rules: list[tuple[str, str]], allowed: set[str], name: str, source: str, used: set[str]) -> str:
    """Keep the rules this specimen can reach, then the keyframes those rules or its script name."""
    kept, frames = [], []
    for prelude, body in rules:
        if prelude.startswith("@keyframes"):
            frames.append((prelude.split()[1], f"{prelude} {{ {body} }}"))
        elif prelude.startswith("@"):
            inner = select_css(parse_css(body), allowed, name, source, used)
            if inner:
                kept.append(f"{prelude} {{\n{inner}\n}}")
        else:
            parts = [p for p in split_selector(prelude) if part_applies(p, allowed, name, source)]
            if parts:
                kept.append(f"{', '.join(parts)} {{ {body} }}")
                used.update(c for p in parts for c in selector_classes(p))
    words = set(WORD_RE.findall("\n".join(kept) + source))
    kept.extend(text for frame, text in frames if frame in words)
    return "\n".join(kept)


def split_js(js: str) -> tuple[dict[str, str], dict[str, str]]:
    """Fragments are formatted so every top-level statement starts at column 0."""
    starts = [m.start() for m in JS_START_RE.finditer(js)]
    demos, helpers = {}, {}
    for start, end in zip(starts, starts[1:] + [len(js)]):
        chunk = js[start:end].rstrip()
        if head := DEMO_HEAD_RE.match(chunk):
            demos[head.group(1)] = chunk
        elif head := HELPER_HEAD_RE.match(chunk):
            helpers[head.group(1)] = chunk
    return demos, helpers


def specimen_js(demo: str, demos: dict[str, str], helpers: dict[str, str]) -> str:
    """The demo plus any helper or other demo it reaches, dependencies first."""
    if not demo:
        return ""
    chunks, pending = [demos[demo]], [demos[demo]]
    seen: set[str] = set()
    while pending:
        text = pending.pop()
        words = set(WORD_RE.findall(text))
        reached = [helpers[name] for name in helpers.keys() - seen if name in words]
        reached_demos = [demos[name] for name in demos.keys() - seen - {demo} if f"demo.{name}" in text]
        seen.update(name for name in helpers if name in words)
        seen.update(name for name in demos if f"demo.{name}" in text)
        for chunk in reached + reached_demos:
            chunks.insert(0, chunk)
            pending.append(chunk)
    return "\n".join(chunks)


def parse_specimens(body: str) -> list[dict]:
    """Specimens in page order, each tagged with the scenario heading above it."""
    specimens, group = [], ""
    for match in BLOCK_RE.finditer(body):
        if match.group("group") is not None:
            group = html.unescape(match.group("group"))
            continue
        attrs = match.group("attrs")
        data = {k.removeprefix("data-"): html.unescape(v) for k, v in ATTR_RE.findall(attrs)}
        no = f"{len(specimens) + 1:02d}"
        specimens.append({**data, "no": no, "group": group, "attrs": attrs.strip(), "stage": match.group("inner").strip()})
    return specimens


def header_comment(sp: dict, slug: str) -> str:
    lines = [f"名称：{sp['name']}（{sp.get('en', '')}）", f"编号：{slug}/{sp['no']}", f"什么时候用：{sp.get('use', '')}"]
    if sp.get("params"):
        lines.append(f"关键参数：{sp['params']}")
    lines.append(f"一句话提示词：{sp.get('prompt', '')}")
    if sp.get("hint"):
        lines.append(f"操作提示：{sp['hint']}")
    lines.append("移植：只搬「标本」部分的 CSS、.stage 内的结构和 demo 函数；颜色全是 CSS 变量，映射到目标项目的颜色；")
    lines.append("      演示里的定时循环和假数据要换成真实状态；.stage、.sp、U.* 只是演示外壳。")
    return "<!--\n" + "\n".join(lines).replace("--", "- -") + "\n-->"


def render_snippet(sp: dict, slug: str, tokens_css: str, specimen_css: str, js: str) -> str:
    scripts = ""
    if sp.get("demo") or re.search(r"data-(toggle|open|close)\b", sp["stage"]) or "auto" in sp:
        scripts = f"<script>window.demo = {{}};\n{js}\n</script>\n<script>{RUNTIME}</script>\n"
    return (f'<!doctype html>\n{header_comment(sp, slug)}\n<html lang="zh-CN"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(sp["name"])}</title>\n'
            f"<style>\n/* 颜色变量和基础样式 */\n{tokens_css}\n/* 演示外壳 */{STAGE_CSS}"
            f"/* 标本 */\n{specimen_css}\n</style></head>\n"
            f'<body><article class="sp" {sp["attrs"]}>{sp["stage"]}</article>\n{scripts}</body></html>\n')


def safe_filename(no: str, name: str) -> str:
    return f"{no}-" + re.sub(r'[\\/:*?"<>|\s]+', "-", name) + ".html"


def cell(text: str) -> str:
    return text.replace("|", "／").replace("\n", " ")


def write_catalog(out: Path, rows: list[str], total: int) -> None:
    head = ("# UI 动效库目录\n\n"
            f"共 {total} 种效果，每行一种。第一列是「页面/编号」，最后一列是可以直接打开运行的单文件，相对本目录。\n\n"
            "这个文件由 src/build.py 生成，不要手改。\n\n"
            "| 编号 | 场景 | 名称 | 英文 | 什么时候用 | 关键参数 | 代码 |\n|---|---|---|---|---|---|---|\n")
    (out / "catalog.md").write_text(head + "\n".join(rows) + "\n", encoding="utf-8")


def build_snippets(pages: list, src: Path, out: Path, split_fragment) -> int:
    """Write snippets/ and catalog.md; returns the specimen count. Stops if a rule or demo goes unused."""
    shell = (src / "shell.css").read_text(encoding="utf-8")
    tokens_css = shell[:shell.index(".top {")].split("*/", 1)[1].strip()
    shared_css = shell[shell.index("/* 演示共用的小零件 */"):shell.index("body.paused .stage *")]
    written, rows, problems = set(), [], []
    for page in pages:
        slug = page[0]
        css, js, body = split_fragment((src / "pages" / f"{slug}.html").read_text(encoding="utf-8"))
        rules = parse_css(shared_css + css)
        page_classes = {c for prelude, _ in parse_css(css) if not prelude.startswith("@")
                        for c in selector_classes(prelude)}
        demos, helpers = split_js(js)
        used: set[str] = set()
        used_demos: set[str] = set()
        (out / "snippets" / slug).mkdir(parents=True, exist_ok=True)
        for sp in parse_specimens(body):
            demo = sp.get("demo", "")
            if demo and demo not in demos:
                problems.append(f"{slug}/{sp['no']}: demo {demo} not found")
                continue
            source_js = specimen_js(demo, demos, helpers)
            used_demos.update({demo} | {d for d in demos if f"demo.{d}" in source_js})
            source = sp["stage"] + "\n" + source_js
            markup = {c for attr in CLASS_ATTR_RE.findall(sp["stage"]) for c in attr.split()}
            all_classes = {c for prelude, _ in rules if not prelude.startswith("@") for c in selector_classes(prelude)}
            allowed = markup | ALWAYS_ALLOWED | (set(WORD_RE.findall(source_js)) & all_classes)
            specimen_css = select_css(rules, allowed, sp["name"], source, used)
            path = out / "snippets" / slug / safe_filename(sp["no"], sp["name"])
            path.write_text(render_snippet(sp, slug, tokens_css, specimen_css, source_js), encoding="utf-8")
            written.add(path)
            rel = path.relative_to(out).as_posix()
            rows.append(f"| {slug}/{sp['no']} | {cell(sp['group'])} | {cell(sp['name'])} | {cell(sp.get('en', ''))} | {cell(sp.get('use', ''))} "
                        f"| {cell(sp.get('params', ''))} | {rel} |")
        problems += [f"{slug}: CSS class .{c} reached by no specimen" for c in sorted(page_classes - used - ALWAYS_ALLOWED - LIBRARY_ONLY)]
        problems += [f"{slug}: demo {d} used by no specimen" for d in sorted(demos.keys() - used_demos)]
    for stale in (out / "snippets").rglob("*.html"):
        if stale not in written:
            stale.unlink()
    if problems:
        raise SystemExit("snippet extraction problems:\n  " + "\n  ".join(problems))
    write_catalog(out, rows, len(rows))
    return len(rows)
