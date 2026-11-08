"""Inline shell + page fragments into self-contained HTML files one level up.

Usage: python build.py
Each output works alone, so a single page can be forwarded without its siblings.
Fails if a page's specimen count drifts from the counts in PAGES.
"""
import re
import sys
from pathlib import Path

from extract import build_snippets

SRC = Path(__file__).parent
OUT = SRC.parent

# slug, tab label, heading, English label, intro, specimen count, index icon class
PAGES = [
    ("01-buttons", "按钮与开关", "按钮与开关", "Buttons & Switches",
     "按钮、按钮的各种状态，还有开关这类选择控件。知道它们各自叫什么，跟 AI 才说得清。", 27, "ic-sw"),
    ("02-modals", "弹窗", "弹窗", "Overlays",
     "同样盖在页面上，有的逼用户马上处理，有的看一眼就没了。按打断程度来选。", 11, "ic-md"),
    ("03-motion", "动效", "动效", "Motion",
     "每种都标了时长或关键参数。跟 AI 说这些，比说「丝滑一点」有用。", 26, "ic-ball"),
    ("04-forms", "表单", "表单", "Form Controls",
     "常用的表单控件，都能直接操作。先试手感，再决定让 AI 做哪一种。", 17, "ic-in"),
    ("05-loading", "加载与错误页", "加载与错误页", "Loading & Error States",
     "等待和出错时，用户最想知道两件事：现在怎么了，接下来能做什么。这里按场景分组。", 30, "ic-sp"),
    ("06-cards", "卡片与列表", "卡片与列表", "Cards & Lists",
     "卡片、列表和表格的常见做法。按要展示的内容来选。", 23, "ic-cd"),
]

NOTE = "提示词里的时长等具体参数是建议值，可以按需调整。演示里的课程、人名、价格和文件都是虚构示例。"

STYLE_RE = re.compile(r"<style>(.*?)</style>", re.S)
SCRIPT_RE = re.compile(r"<script>(.*?)</script>", re.S)
NAME_RE = re.compile(r'class="sp" data-name="([^"]+)"')
# Shared spring helper: prepended to any page whose script calls spring.*, so every snippet that
# uses it carries its own copy (extract.py pulls helpers in by name).
SPRING_JS = (SRC / "spring.js").read_text(encoding="utf-8")
SPRING_USE_RE = re.compile(r"\bspring\.")


def split_fragment(text: str) -> tuple[str, str, str]:
    css = "\n".join(STYLE_RE.findall(text))
    js = "\n".join(SCRIPT_RE.findall(text))
    if SPRING_USE_RE.search(js):
        js = SPRING_JS + "\n" + js
    body = SCRIPT_RE.sub("", STYLE_RE.sub("", text)).strip()
    return css, js, body


def top_bar(current: str) -> str:
    tabs = "".join(
        f'<a href="{p[0]}.html"{" aria-current=page" if p[0] == current else ""}>{p[1]}</a>'
        for p in PAGES)
    return (f'<header class="top"><a class="home" href="index.html">UI 动效库</a>'
            f'<nav class="tabs" aria-label="主题">{tabs}</nav>'
            f'<button class="pause" id="pauseAll" type="button" aria-pressed="false">暂停动效</button></header>')


def document(title: str, css: str, body: str, js: str) -> str:
    return ('<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<meta name="claude:viewport-fit-sides" content="cover">'
            f'<title>{title}</title><style>{css}</style></head>\n<body>{body}{js}</body></html>\n')


def build_page(i: int, page: tuple, shell_css: str, shell_js: str) -> list[str]:
    slug, _, heading, english, intro, expected, _ = page
    css, js, body = split_fragment((SRC / "pages" / f"{slug}.html").read_text(encoding="utf-8"))
    names = NAME_RE.findall(body)
    if len(names) != expected:
        sys.exit(f"{slug}: expected {expected} specimens, found {len(names)}")
    prev_link = f'<a href="{PAGES[i-1][0]}.html">← {PAGES[i-1][1]}</a>' if i else '<a href="index.html">← 目录</a>'
    next_link = (f'<a href="{PAGES[i+1][0]}.html">{PAGES[i+1][1]} →</a>'
                 if i + 1 < len(PAGES) else '<a href="index.html">回目录 →</a>')
    html_body = (f'{top_bar(slug)}<main class="wrap"><section class="hero">'
                 f'<h1>{heading}<small>{english} · {expected} 种</small></h1><p>{intro}</p>'
                 f'<nav class="toc" aria-label="本页条目"></nav></section>'
                 f'<div class="grid">{body}</div><p class="note">{NOTE}</p>'
                 f'<div class="pager">{prev_link}{next_link}</div></main>')
    scripts = f'<script>window.demo={{}};{js}</script><script>{shell_js}</script>'
    out = document(f"{heading}动效库", shell_css + css, html_body, scripts)
    (OUT / f"{slug}.html").write_text(out, encoding="utf-8")
    return names


def build_index(all_names: list[list[str]], shell_css: str) -> None:
    rows = "".join(
        f'<a class="row" href="{p[0]}.html"><span class="ic"><span class="{p[6]}"></span></span>'
        f'<span><h2>{p[2]}<small>{p[3]} · {p[5]} 种</small></h2><p>{"、".join(names)}</p></span></a>'
        for p, names in zip(PAGES, all_names))
    total = sum(p[5] for p in PAGES)
    body = (f'{top_bar("")}<main class="wrap"><section class="hero">'
            f'<h1>UI 动效库<small>{total} 种</small></h1>'
            '<p>给不写代码的人用的界面元素名词表。先看它动起来是什么样，记住它叫什么，再复制那句提示词交给 AI。</p>'
            f'</section><div class="rows">{rows}</div><p class="note">{NOTE}</p></main>')
    pause_js = ("<script>(function(){var b=document.getElementById('pauseAll');"
                "b.addEventListener('click',function(){var v=document.body.classList.toggle('paused');"
                "document.querySelectorAll('.ic *').forEach(function(e){e.style.animationPlayState=v?'paused':''});"
                "b.textContent=v?'继续动效':'暂停动效';b.setAttribute('aria-pressed',String(v));});"
                "if(matchMedia('(prefers-reduced-motion: reduce)').matches)b.click();})();</script>")
    out = document("UI 动效库", shell_css, body, pause_js)
    (OUT / "index.html").write_text(out, encoding="utf-8")


def main() -> None:
    shell_css = (SRC / "shell.css").read_text(encoding="utf-8")
    shell_js = (SRC / "shell.js").read_text(encoding="utf-8")
    all_names = [build_page(i, p, shell_css, shell_js) for i, p in enumerate(PAGES)]
    build_index(all_names, shell_css)
    print("built", len(PAGES) + 1, "pages,", sum(map(len, all_names)), "specimens")
    print("wrote", build_snippets(PAGES, SRC, OUT, split_fragment), "snippets + catalog.md")


if __name__ == "__main__":
    main()
