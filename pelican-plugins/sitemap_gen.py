"""
Pelican plugin that generates a sitemap.xml from all pages and the index.
"""

import os
from datetime import datetime
from pelican import signals


def generate_sitemap(generator):
    site_url = generator.settings.get("SITEURL", "").rstrip("/")
    output_path = generator.settings.get("OUTPUT_PATH", "output")

    pages = list(generator.pages) if hasattr(generator, "pages") else []
    urls = [("index.html", None)]

    for page in pages:
        if getattr(page, "status", "published") == "published":
            urls.append((page.save_as, getattr(page, "date", None)))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, date in urls:
        loc = f"{site_url}/{path}"
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        if date:
            lines.append(f"    <lastmod>{date.strftime('%Y-%m-%d')}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")

    sitemap_path = os.path.join(output_path, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def register():
    signals.page_generator_finalized.connect(generate_sitemap)
