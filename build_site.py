#!/usr/bin/env python3
"""Build a readable static website from the repository's Markdown sources."""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
SITE = ROOT / "_site"
PAGE_CSS = """
:root{color-scheme:light;--paper:#f5f4ef;--surface:#fffefa;--ink:#172a2d;--muted:#526365;--line:#d5ddda;--green:#176b58;--green-dark:#0e4b3e;--width:900px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.72 Arial,Helvetica,sans-serif}
a{color:var(--green-dark);text-underline-offset:.18em}a:hover{color:var(--green)}a:focus-visible{outline:3px solid #d49222;outline-offset:3px}
.shell{width:min(var(--width),calc(100% - 2.5rem));margin-inline:auto}.top{border-bottom:1px solid var(--line);background:var(--surface)}.topin{min-height:64px;display:flex;align-items:center;justify-content:space-between;gap:1rem}.brand{font-weight:700;color:var(--ink);text-decoration:none}.back{font-size:.94rem}.print{padding:.45rem .7rem;border:1px solid var(--green);border-radius:4px;background:white;color:var(--green-dark);font:inherit;cursor:pointer}
main{padding:clamp(2rem,6vw,4.5rem) 0 5rem}article{padding:clamp(1.4rem,4vw,3rem);background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--green)}h1,h2,h3{line-height:1.22;letter-spacing:-.025em}h1{margin:0 0 1.8rem;font-size:clamp(2rem,5vw,3.2rem)}h2{margin:2.3rem 0 .8rem;padding-top:1.1rem;border-top:1px solid var(--line);font-size:clamp(1.45rem,3vw,2rem)}h3{margin:1.5rem 0 .5rem;font-size:1.2rem}p{margin:.8rem 0}li{margin:.5rem 0}blockquote{margin:1.3rem 0;padding:.8rem 1.2rem;border-left:3px solid var(--green);background:#f3f6f2}table{width:100%;border-collapse:collapse;display:block;overflow-x:auto}th,td{padding:.65rem .75rem;border:1px solid var(--line);text-align:left;vertical-align:top}th{background:#eef2ee}pre{overflow:auto;padding:1rem;background:#edf0ed;border-radius:4px}code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.92em}.task-box{width:1.1rem;height:1.1rem;margin:0 .55rem 0 0;accent-color:var(--green);vertical-align:-.16em;cursor:pointer}li:has(>.task-box){list-style:none;margin-left:-1.2rem}footer{padding:1.4rem 0 2.5rem;border-top:1px solid var(--line);color:var(--muted);font-size:.9rem}
@media(max-width:650px){body{font-size:16px}.shell{width:calc(100% - 1.2rem)}.topin{align-items:flex-start;flex-direction:column;justify-content:center;padding:.8rem 0}article{padding:1.1rem}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{body{background:white;font-size:11pt}.top,footer,.print{display:none}.shell{width:100%}main{padding:0}article{padding:0;border:0}h2{break-after:avoid}li{break-inside:avoid}a{color:inherit;text-decoration:none}}
"""


def readable_title(source: str, fallback: str) -> str:
    for line in source.splitlines():
        match = re.match(r"^#\s+(.+?)\s*#*\s*$", line)
        if match:
            return re.sub(r"[`*_]", "", match.group(1)).strip()
    return fallback.replace("-", " ").replace("_", " ").title()


def task_list_html(body: str) -> str:
    task_number = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal task_number
        task_number += 1
        checked = match.group("mark").lower() == "x"
        state = " checked" if checked else ""
        return f'{match.group("prefix")}<input class="task-box" type="checkbox" data-task="{task_number}" aria-label="Oznacz zadanie"{state}>'

    pattern = re.compile(r'(?P<prefix><li(?:\s[^>]*)?>\s*(?:<p>)?)\[(?P<mark> |x|X)\]\s*')
    body = pattern.sub(replace, body)
    return body.replace("<li><p><input", '<li class="task-item"><p><input').replace("<li><input", '<li class="task-item"><input')


def render_markdown(source_path: Path) -> str:
    source = source_path.read_text(encoding="utf-8")
    title = readable_title(source, source_path.stem)
    body = markdown.markdown(source, extensions=["extra", "sane_lists", "toc"])
    body = task_list_html(body)
    body = re.sub(r'(href="[^"]+?)\.md(?=([?#][^"]*)?")', r"\1.html", body)
    relative_root = Path(".") if source_path.parent == ROOT else Path("../")
    home_href = (relative_root / "index.html").as_posix()
    plan_href = (relative_root / "PLAN-POSTEPOWANIA.html").as_posix()
    guide_href = (relative_root / "poradnik-sprawy.html").as_posix()
    title_text = html.escape(title)
    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f5f4ef">
  <title>{title_text}</title>
  <style>{PAGE_CSS}</style>
</head>
<body>
  <header class="top"><div class="shell topin"><a class="brand" href="{home_href}">Dokumenty i plan sprawy</a><nav class="back" aria-label="Nawigacja"><a href="{guide_href}">Poradnik</a> · <a href="{plan_href}">Plan działań</a> · <a href="{home_href}">Strona główna</a></nav><button class="print" type="button" onclick="window.print()">Drukuj / zapisz jako PDF</button></div></header>
  <main class="shell"><article><h1>{title_text}</h1>{body}</article></main>
  <footer><div class="shell"><p>Treść wygenerowana z pliku źródłowego Markdown w repozytorium. Odznaczanie zadań zapisuje się tylko w tej przeglądarce; trwałą zmianę w planie wprowadź w repozytorium.</p><p><a href="{home_href}">Wróć na stronę główną</a></p></div></footer>
  <script>
    const key = `dentysta-tasks:${{location.pathname}}`;
    const saved = JSON.parse(localStorage.getItem(key) || "{{}}");
    document.querySelectorAll(".task-box").forEach((box) => {{
      const id = box.dataset.task;
      if (Object.hasOwn(saved, id)) box.checked = saved[id];
      box.addEventListener("change", () => {{
        saved[id] = box.checked;
        localStorage.setItem(key, JSON.stringify(saved));
      }});
    }});
  </script>
</body>
</html>
"""


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    for page in ROOT.glob("*.html"):
        shutil.copy2(page, SITE / page.name)

    for source in ROOT.glob("*.md"):
        (SITE / f"{source.stem}.html").write_text(render_markdown(source), encoding="utf-8")

    laws = ROOT / "ustawy"
    if laws.exists():
        shutil.copytree(laws, SITE / "ustawy", ignore=shutil.ignore_patterns("*.md"))
        for original in laws.glob("*.md"):
            (SITE / "ustawy" / f"{original.stem}.html").write_text(render_markdown(original), encoding="utf-8")

    shutil.copytree(ROOT / "dist", SITE / "dist")
    (SITE / "404.html").write_text("""<!doctype html>
<html lang="pl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Przekierowanie do czytelnej strony</title>
<body style="font:17px/1.6 Arial,sans-serif;max-width:680px;margin:12vh auto;padding:0 1rem;color:#172a2d"><h1>Otwieram czytelną wersję dokumentu…</h1><p>Pliki Markdown mają na stronie osobne wersje HTML.</p><p><a href="./index.html">Wróć na stronę główną</a></p><script>const path=location.pathname;const target=path.replace(/\\.md$/i,".html");if(target!==path)location.replace(target+location.search+location.hash);</script></body></html>""", encoding="utf-8")
    print(f"Pages site built in {SITE} with {len(list(SITE.rglob('*.html')))} HTML pages.")


if __name__ == "__main__":
    main()
