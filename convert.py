#!/usr/bin/env python3
import os
import re
import subprocess
import tempfile
import markdown

SOURCE_FILES = [
    ("wniosek-dokumentacja-papierowa.md", "Wniosek o dokumentację medyczną i polisę OC"),
    ("wniosek-odszkodowanie-OC-dentysty.md", "Zgłoszenie szkody i wezwanie do zapłaty OC"),
    ("research-OC-dentysty.md", "Poradnik błąd diagnostyczny RTG i procedura OC")
]

CSS = """
@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
}
body {
    font-family: 'Liberation Sans', 'DejaVu Sans', Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #111;
    margin: 0;
    padding: 0;
}
h1 {
    font-size: 15pt;
    text-align: center;
    text-transform: uppercase;
    margin-top: 0;
    margin-bottom: 16px;
    line-height: 1.3;
    border-bottom: 1.5px solid #333;
    padding-bottom: 8px;
}
h2 {
    font-size: 12pt;
    margin-top: 18px;
    margin-bottom: 8px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
    text-align: left;
}
h3 {
    font-size: 11pt;
    margin-top: 14px;
    margin-bottom: 6px;
    text-align: left;
}
p {
    margin-top: 6px;
    margin-bottom: 6px;
    text-align: justify;
    text-align-last: left;
    hyphens: auto;
    -webkit-hyphens: auto;
}
li {
    margin-bottom: 4px;
    text-align: left;
}
hr {
    border: 0;
    border-top: 1px dashed #aaa;
    margin: 14px 0;
}
ul, ol {
    margin-top: 6px;
    margin-bottom: 6px;
    padding-left: 22px;
}
li {
    margin-bottom: 4px;
}
strong {
    color: #000;
}
em {
    color: #555;
}
"""

def md_to_html(md_path, title):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert markdown to html with extra extensions
    body_html = markdown.markdown(md_text, extensions=['extra', 'sane_lists'])

    html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
{CSS}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""
    return html

def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(repo_dir, "dist")
    os.makedirs(build_dir, exist_ok=True)
    temp_dir = os.path.join(tempfile.gettempdir(), "dentysta_build")
    os.makedirs(temp_dir, exist_ok=True)

    for md_filename, title in SOURCE_FILES:
        base_name = os.path.splitext(md_filename)[0]
        md_file = os.path.join(repo_dir, md_filename)
        html_file = os.path.join(temp_dir, f"{base_name}.html")
        
        print(f"Generating HTML for {md_filename}...")
        html_content = md_to_html(md_file, title)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Convert to PDF
        print(f"Converting {base_name} to PDF...")
        subprocess.run([
            "libreoffice", "--headless",
            "--convert-to", "pdf",
            html_file,
            "--outdir", build_dir
        ], check=True)

        # Convert to DOCX
        print(f"Converting {base_name} to DOCX...")
        subprocess.run([
            "libreoffice", "--headless",
            "--convert-to", "docx:Office Open XML Text",
            html_file,
            "--outdir", build_dir
        ], check=True)

    print("All conversions completed successfully.")
    print("Files in dist:")
    for f in os.listdir(build_dir):
        print(f" - {f}")

if __name__ == "__main__":
    main()
