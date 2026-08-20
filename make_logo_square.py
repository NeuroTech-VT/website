#!/usr/bin/env python3
"""Make the cropped NeuroTech_VT logo square by adding transparent padding."""
from PIL import Image

SOURCE = "NeuroTech_VT_cropped.png"
OUTPUT = "NeuroTech_VT_square.png"

im = Image.open(SOURCE).convert("RGBA")
w, h = im.size
size = max(w, h)  # square canvas, no upscaling

canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
canvas.paste(im, ((size - w) // 2, (size - h) // 2), im)

canvas.save(OUTPUT)
print(f"Wrote {OUTPUT}: {canvas.size[0]}x{canvas.size[1]}")
