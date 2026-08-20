#!/usr/bin/env python3
"""Convert the NeuroTech_VT SVG logo to a PNG using the project venv."""
import cairosvg

SOURCE = "NeuroTech_VT_cropped.svg"
OUTPUT = "NeuroTech_VT_cropped.png"
# Render at 2x the SVG's intrinsic size (700.13 x 198.905 mm @ 96dpi = 2645 x 751)
SCALE = 2.0

cairosvg.svg2png(
    url=SOURCE,
    write_to=OUTPUT,
    scale=SCALE,
)

print(f"Wrote {OUTPUT}")
