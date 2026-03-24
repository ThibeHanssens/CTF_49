#!/usr/bin/env python3
"""
Howest CTF - Douwe's bedtime story v2
Improved: tighter edge scan, two-cluster detection, wider columns, smoother output.
"""

import sys
import numpy as np
from PIL import Image, ImageFilter
import fitz  # PyMuPDF

PDF_PATH = sys.argv[1] if len(sys.argv) > 1 else "FortiWeb_8.0.3_Administration_Guide.pdf"

DPI = 150
SCALE = DPI / 72.0

# Only scan the very last few pixels — avoids text/content noise
SCAN_WIDTH = 5

# Strict darkness threshold
LINE_THRESHOLD = 80

# Pixels per page column in output (wider = more readable)
COL_WIDTH = 2

OUT_HEIGHT = 400

print(f"[*] Opening {PDF_PATH}...")
doc = fitz.open(PDF_PATH)
total_pages = len(doc)
print(f"[*] Total pages: {total_pages}")

crossings = []

for page_num in range(total_pages):
    page = doc[page_num]
    mat = fitz.Matrix(SCALE, SCALE)
    pix = page.get_pixmap(matrix=mat, colorspace=fitz.csGRAY)

    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w)

    # Only look at the rightmost SCAN_WIDTH pixels
    right_strip = img[:, max(0, pix.w - SCAN_WIDTH):]
    min_per_row = right_strip.min(axis=1)
    dark_rows = np.where(min_per_row < LINE_THRESHOLD)[0]

    if len(dark_rows) < 2:
        crossings.append(None)
        continue

    # Split dark rows into two clusters: top half and bottom half of page
    mid = pix.h // 2
    top_rows = dark_rows[dark_rows < mid]
    bot_rows = dark_rows[dark_rows >= mid]

    if len(top_rows) == 0 or len(bot_rows) == 0:
        # Fallback: just use min/max
        crossings.append((int(dark_rows.min()), int(dark_rows.max()), pix.h))
    else:
        # Use median of each cluster for robustness against noise
        y1 = int(np.median(top_rows))
        y2 = int(np.median(bot_rows))
        crossings.append((y1, y2, pix.h))

    if (page_num + 1) % 100 == 0:
        print(f"  [{page_num+1}/{total_pages}]...")

print(f"[*] Pages with crossings: {sum(1 for c in crossings if c is not None)}")

# --- Build side view ---
OUT_WIDTH = total_pages * COL_WIDTH
side_view = np.ones((OUT_HEIGHT, OUT_WIDTH), dtype=np.uint8) * 255

for i, c in enumerate(crossings):
    if c is None:
        continue
    y1, y2, page_h = c
    ny1 = int(y1 / page_h * OUT_HEIGHT)
    ny2 = int(y2 / page_h * OUT_HEIGHT)
    col_start = i * COL_WIDTH
    col_end = col_start + COL_WIDTH
    side_view[ny1:ny2+1, col_start:col_end] = 0

out_img = Image.fromarray(side_view, mode='L')

# Light smoothing to reduce jaggedness while keeping letter shapes
smoothed = out_img.filter(ImageFilter.MedianFilter(size=3))
smoothed.save("side_view_v2.png")
print("[*] Saved: side_view_v2.png")

# Also save inverted
inv = Image.fromarray(255 - np.array(smoothed), mode='L')
inv.save("side_view_v2_inverted.png")
print("[*] Saved: side_view_v2_inverted.png")

# Debug: print first 20 crossings
found = [(i, c) for i, c in enumerate(crossings) if c is not None]
print(f"\n[*] First 20 crossings (page, y1, y2, page_h):")
for i, c in found[:20]:
    print(f"    Page {i+1:4d}: y1={c[0]:4d}, y2={c[1]:4d}, h={c[2]}")
