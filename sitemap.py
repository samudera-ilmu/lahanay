"""
sitemap.py — Generate sitemap.xml + robots.txt untuk Lahanay
Adaptasi dari skrip yang sama di proyek Bacaan Terpilih.

Cara pakai:
    python sitemap.py

Skrip ini akan scan semua file .html di project (kecuali template-artikel.html),
lalu generate sitemap.xml dan robots.txt otomatis.
"""

import os
from datetime import date

# ── Konfigurasi ──────────────────────────────────────────────
SITE_URL = "https://lahanay.pages.dev"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_SITEMAP = os.path.join(ROOT_DIR, "sitemap.xml")
OUTPUT_ROBOTS = os.path.join(ROOT_DIR, "robots.txt")

# File/folder yang di-skip saat scan
EXCLUDE_FILES = {"template-artikel.html"}
EXCLUDE_DIRS = {".git", "assets", "data", "images", "node_modules", "sumber"}

# Set True kalau baru ganti desain besar-besaran dan mau semua
# tanggal lastmod di-reset ke hari ini
FORCE_RESET = False

# Prioritas per jenis halaman (opsional, membantu crawler)
PRIORITY_HOME = "1.0"
PRIORITY_ARTIKEL_INDEX = "0.8"
PRIORITY_ARTIKEL = "0.7"
PRIORITY_DEFAULT = "0.5"


def find_html_files():
    html_files = []
    for current_root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if f.endswith(".html") and f not in EXCLUDE_FILES:
                full_path = os.path.join(current_root, f)
                rel_path = os.path.relpath(full_path, ROOT_DIR).replace(os.sep, "/")
                html_files.append(rel_path)
    return sorted(html_files)


def path_to_url(rel_path):
    if rel_path == "index.html":
        return f"{SITE_URL}/"
    if rel_path.endswith("/index.html"):
        return f"{SITE_URL}/{rel_path[:-len('index.html')]}"
    return f"{SITE_URL}/{rel_path}"


def priority_for(rel_path):
    if rel_path == "index.html":
        return PRIORITY_HOME
    if rel_path == "artikel/index.html":
        return PRIORITY_ARTIKEL_INDEX
    if rel_path.startswith("artikel/"):
        return PRIORITY_ARTIKEL
    return PRIORITY_DEFAULT


def build_sitemap(html_files):
    today = date.today().isoformat()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for rel_path in html_files:
        url = path_to_url(rel_path)
        priority = priority_for(rel_path)
        lastmod = today  # sederhana: selalu pakai tanggal run terakhir
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")

    lines.append("</urlset>")
    return "\n".join(lines)


def build_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def main():
    html_files = find_html_files()
    if not html_files:
        print("Tidak ada file .html ditemukan. Cek ROOT_DIR.")
        return

    sitemap_xml = build_sitemap(html_files)
    with open(OUTPUT_SITEMAP, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)

    robots_txt = build_robots()
    with open(OUTPUT_ROBOTS, "w", encoding="utf-8") as f:
        f.write(robots_txt)

    print(f"✅ sitemap.xml dibuat ({len(html_files)} halaman):")
    for rel_path in html_files:
        print(f"   - {path_to_url(rel_path)}")
    print(f"✅ robots.txt dibuat di {OUTPUT_ROBOTS}")


if __name__ == "__main__":
    main()
