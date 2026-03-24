#!/usr/bin/env python3
"""
Howest CTF - Douwe's bedtime story
Extracts the "side view" of a folded PDF bundle.

Each page has diagonal lines forming a V pointing right.
The lines cross the right edge at y1 (top) and y2 (bottom).
Looking at the right edge of the stacked bundle = the flag.

Usage:
    pip install pymupdf pillow numpy
    python solve_bedtime.py FortiWeb_8.0.3_Administration_Guide.pdf
"""

import sys
import numpy as np
from PIL import Image
import fitz  # PyMuPDF

PDF_PATH = sys.argv[1] if len(sys.argv) > 1 else "FortiWeb_8.0.3_Administration_Guide.pdf"

# Resolution to render pages at (low = fast)
DPI = 72
SCALE = DPI / 72.0  # matrix scale factor

# How many pixels from the right edge to scan for the line
SCAN_WIDTH = 30

# Darkness threshold (0=black, 255=white) — line pixels are dark
LINE_THRESHOLD = 100

print(f"[*] Opening {PDF_PATH}...")
doc = fitz.open(PDF_PATH)
total_pages = len(doc)
print(f"[*] Total pages: {total_pages}")

# We'll store (y1, y2) per page — the two y-crossings on the right edge
# If no line found on a page, we store None
crossings = []

for page_num in range(total_pages):
    page = doc[page_num]
    mat = fitz.Matrix(SCALE, SCALE)
    pix = page.get_pixmap(matrix=mat, colorspace=fitz.csGRAY)
    
    img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w)
    
    # Scan the rightmost SCAN_WIDTH columns
    right_strip = img_array[:, max(0, pix.w - SCAN_WIDTH):]
    
    # Find rows where any pixel is dark (= line crossing right edge)
    min_per_row = right_strip.min(axis=1)
    dark_rows = np.where(min_per_row < LINE_THRESHOLD)[0]
    
    if len(dark_rows) == 0:
        crossings.append(None)
    else:
        y1 = int(dark_rows.min())
        y2 = int(dark_rows.max())
        crossings.append((y1, y2, pix.h))
    
    if (page_num + 1) % 50 == 0:
        print(f"  [{page_num+1}/{total_pages}] processed...")

print(f"[*] Pages with line detected: {sum(1 for c in crossings if c is not None)}")

# --- Build the side-view image ---
# x-axis = page number, y-axis = normalized height
# For each page: fill between y1 and y2 with black (paper visible from side)

# Use a fixed output height (normalize all pages to same height)
OUT_HEIGHT = 300
OUT_WIDTH = total_pages  # 1 pixel per page

side_view = np.ones((OUT_HEIGHT, OUT_WIDTH), dtype=np.uint8) * 255  # white background

for i, c in enumerate(crossings):
    if c is None:
        continue
    y1, y2, page_h = c
    # Normalize to output height
    ny1 = int(y1 / page_h * OUT_HEIGHT)
    ny2 = int(y2 / page_h * OUT_HEIGHT)
    # Fill the column between ny1 and ny2 with black
    side_view[ny1:ny2+1, i] = 0

# Save raw side view
out_img = Image.fromarray(side_view, mode='L')
out_img.save("side_view_raw.png")
print("[*] Saved raw side view to /side_view_raw.png")

# Also save a scaled-up version for readability
scale_x = max(1, 800 // OUT_WIDTH)
scale_y = 3
big = out_img.resize((OUT_WIDTH * scale_x, OUT_HEIGHT * scale_y), Image.NEAREST)
big.save("side_view_big.png")
print("[*] Saved scaled side view to /side_view_big.png")

# Try inverting too (in case flag is white-on-black)
inv = Image.fromarray(255 - np.array(out_img), mode='L')
inv_big = inv.resize((OUT_WIDTH * scale_x, OUT_HEIGHT * scale_y), Image.NEAREST)
inv_big.save("side_view_inverted.png")
print("[*] Saved inverted side view to side_view_inverted.png")

print("\n[*] Done! Check:")
print("side_view_big.png")
print("side_view_inverted.png")

# Print some stats for debugging
found = [(i, c) for i, c in enumerate(crossings) if c is not None]
if found:
    print(f"\n[*] First 10 crossings (page, y1, y2):")
    for i, c in found[:10]:
        print(f"    Page {i+1}: y1={c[0]}, y2={c[1]}, page_h={c[2]}")
