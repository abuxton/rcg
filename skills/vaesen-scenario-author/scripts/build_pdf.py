#!/usr/bin/env python3
"""Render a scenario Markdown file to PDF using markdown-it-py and WeasyPrint.

Usage: build_pdf.py <scenario.md> <output.pdf> [--site-root DIR]

Root-relative image paths such as /assets/scenarios/banner.jpg are resolved
against --site-root (default: the current directory).
Requires: pip install markdown-it-py weasyprint
"""
import argparse
import pathlib

from markdown_it import MarkdownIt
from weasyprint import HTML

parser = argparse.ArgumentParser()
parser.add_argument("source", type=pathlib.Path)
parser.add_argument("output", type=pathlib.Path)
parser.add_argument("--site-root", type=pathlib.Path, default=pathlib.Path.cwd())
args = parser.parse_args()

root = args.site_root.resolve()
body = MarkdownIt("commonmark", {"html": True}).render(args.source.read_text())
body = body.replace('src="/', f'src="{root.as_uri()}/')
page = (
    '<!doctype html><html lang="en"><meta charset="utf-8">'
    f"<title>{args.source.stem}</title>"
    "<style>img{width:100%;max-height:70mm;object-fit:cover}</style>"
    f"<body>{body}</body></html>"
)
HTML(string=page, base_url=root.as_uri() + "/").write_pdf(args.output)
