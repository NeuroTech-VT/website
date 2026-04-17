"""
crop_svg.py – Remove trailing blank space from an SVG by tightening viewBox.

Strategy 1 (preferred): Inkscape CLI  — no pip installs needed
Strategy 2 (fallback):  svgpathtools  — pip install svgpathtools
"""

import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

SVG_NS = "http://www.w3.org/2000/svg"

# ── Transform helpers ─────────────────────────────────────────────────────────

def parse_transform(transform_str):
    """Return (tx, ty, sx, sy) for translate/matrix/scale transforms."""
    tx = ty = 0.0
    sx = sy = 1.0
    if not transform_str:
        return tx, ty, sx, sy

    m = re.match(r'translate\(\s*([^\s,]+)[\s,]+([^\s,)]+)', transform_str)
    if m:
        tx, ty = float(m.group(1)), float(m.group(2))
        return tx, ty, sx, sy

    m = re.match(r'matrix\(\s*([^\s,]+)[\s,]+([^\s,]+)[\s,]+([^\s,]+)[\s,]+([^\s,]+)[\s,]+([^\s,]+)[\s,]+([^\s,)]+)', transform_str)
    if m:
        a, b, c, d, e, f = (float(m.group(i)) for i in range(1, 7))
        # matrix(a,b,c,d,e,f) → scale x by sqrt(a²+b²), scale y by sqrt(c²+d²)
        import math
        sx = math.hypot(a, b)
        sy = math.hypot(c, d)
        tx, ty = e, f
        return tx, ty, sx, sy

    m = re.match(r'scale\(\s*([^\s,)]+)(?:[\s,]+([^\s,)]+))?', transform_str)
    if m:
        sx = float(m.group(1))
        sy = float(m.group(2)) if m.group(2) else sx
        return tx, ty, sx, sy

    return tx, ty, sx, sy


def collect_transforms(root):
    """Walk the tree and return a list of (tx, ty, sx, sy) per ancestor group."""
    transforms = []
    for elem in root.iter():
        t = elem.get("transform", "")
        if t:
            transforms.append(parse_transform(t))
    return transforms


def apply_transforms(xmin, ymin, xmax, ymax, transforms):
    """Apply a stack of transforms (innermost last → apply in order) to a bbox."""
    for tx, ty, sx, sy in transforms:
        xmin = xmin * sx + tx
        ymin = ymin * sy + ty
        xmax = xmax * sx + tx
        ymax = ymax * sy + ty
    return xmin, ymin, xmax, ymax

# ── Strategy 1: Inkscape CLI ──────────────────────────────────────────────────

INKSCAPE_CANDIDATES = [
    "inkscape",
    r"C:\Program Files\Inkscape\bin\inkscape.exe",
    r"C:\Program Files (x86)\Inkscape\bin\inkscape.exe",
]

def find_inkscape():
    for candidate in INKSCAPE_CANDIDATES:
        path = shutil.which(candidate) or (candidate if os.path.isfile(candidate) else None)
        if path:
            return path
    return None

def crop_with_inkscape(input_path, output_path):
    inkscape = find_inkscape()
    if not inkscape:
        return False
    subprocess.run(
        [inkscape, "--export-area-drawing", "--export-plain-svg", "-o", output_path, input_path],
        check=True, capture_output=True,
    )
    print(f"[inkscape] Saved: {output_path}")
    return True

# ── Strategy 2: pure-Python via svgpathtools ──────────────────────────────────

def crop_with_svgpathtools(input_path, output_path, padding=0.0):
    from svgpathtools import svg2paths2

    paths, _, _ = svg2paths2(input_path)
    if not paths:
        raise ValueError("No paths found in SVG")

    # Build accumulated transform stack from ancestor groups
    tree = ET.parse(input_path)
    root = tree.getroot()
    transform_stack = []
    for elem in root.iter():
        t = elem.get("transform", "")
        if t:
            transform_stack.append(parse_transform(t))

    all_xmin, all_ymin, all_xmax, all_ymax = [], [], [], []
    for path in paths:
        try:
            xmin, xmax, ymin, ymax = path.bbox()
            # Apply each group's transform to convert local → document coords
            x0, y0, x1, y1 = apply_transforms(xmin, ymin, xmax, ymax, transform_stack)
            all_xmin.append(min(x0, x1)); all_xmax.append(max(x0, x1))
            all_ymin.append(min(y0, y1)); all_ymax.append(max(y0, y1))
        except Exception:
            pass

    if not all_xmin:
        raise ValueError("Could not compute bounding box")

    x = min(all_xmin) - padding
    y = min(all_ymin) - padding
    w = max(all_xmax) - min(all_xmin) + 2 * padding
    h = max(all_ymax) - min(all_ymin) + 2 * padding

    for prefix, uri in [
        ("", SVG_NS), ("xlink", "http://www.w3.org/1999/xlink"),
        ("dc", "http://purl.org/dc/elements/1.1/"),
        ("cc", "http://creativecommons.org/ns#"),
        ("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
        ("sodipodi", "http://sodipodi.sourceforge.net/DTD/sodipodi-0.0.dtd"),
        ("inkscape", "http://www.inkscape.org/namespaces/inkscape"),
    ]:
        ET.register_namespace(prefix, uri)

    root.set("viewBox", f"{x:.4f} {y:.4f} {w:.4f} {h:.4f}")
    root.set("width",  f"{w:.4f}mm")
    root.set("height", f"{h:.4f}mm")
    tree.write(output_path, xml_declaration=True, encoding="UTF-8")
    print(f"[svgpathtools] Saved: {output_path}  (viewBox {x:.2f} {y:.2f} {w:.2f} {h:.2f})")

# ── Entry point ───────────────────────────────────────────────────────────────

def crop_svg(input_path, output_path):
    if crop_with_inkscape(input_path, output_path):
        return
    print("Inkscape not found, falling back to svgpathtools…")
    try:
        crop_with_svgpathtools(input_path, output_path)
    except ImportError:
        print("svgpathtools not installed. Run:  pip install svgpathtools")
        sys.exit(1)

if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "NeuroTech_VT.svg"
    out = sys.argv[2] if len(sys.argv) > 2 else inp.replace(".svg", "_cropped.svg")
    crop_svg(inp, out)
