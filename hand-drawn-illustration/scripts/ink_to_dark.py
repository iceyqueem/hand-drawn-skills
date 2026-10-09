"""Turn a black-ink sketch on white into transparent light lines for a dark page.

Ink becomes a light line colour (default warm cream); the one accent colour is kept;
white paper becomes fully transparent. The result sits directly on any dark background.

Usage:
  python ink_to_dark.py in.png out.png [--width 1200] [--line 239,230,210] [--accent 234,169,0]
       [--glow X,Y,RADIUS]

--glow replaces a small hard accent dot at X,Y (in output pixels) with a soft light:
warm white core, accent halo, fading out over RADIUS pixels.
Requires Pillow (pip install pillow).
"""
import argparse
import math
from PIL import Image


def rgb(s):
    return tuple(int(v) for v in s.split(','))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src')
    ap.add_argument('dst')
    ap.add_argument('--width', type=int, default=1200)
    ap.add_argument('--line', type=rgb, default=(239, 230, 210))
    ap.add_argument('--accent', type=rgb, default=(234, 169, 0))
    ap.add_argument('--floor', type=float, default=0.08, help='paper tone treated as fully transparent (0..1)')
    ap.add_argument('--glow', type=str, default=None)
    a = ap.parse_args()

    im = Image.open(a.src).convert('RGB')
    if a.width and im.width != a.width:
        im = im.resize((a.width, round(im.height * a.width / im.width)), Image.LANCZOS)
    out = Image.new('RGBA', im.size)
    src, dst = im.load(), out.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = src[x, y]
            sat = max(r, g, b) - min(r, g, b)
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            if sat > 40 and r > b:  # the accent light
                dst[x, y] = (*a.accent, min(255, int(sat * 1.6)))
            else:  # ink: darker means more opaque; paper tone drops to zero
                alpha = (1 - lum - a.floor) / (1 - a.floor) * 255 * 1.3
                dst[x, y] = (*a.line, max(0, min(255, int(alpha))))

    if a.glow:
        cx, cy, R = (float(v) for v in a.glow.split(','))
        px = out.load()
        for y in range(int(cy - 14), int(cy + 15)):  # clear the hard dot
            for x in range(int(cx - 14), int(cx + 15)):
                if 0 <= x < out.width and 0 <= y < out.height and math.hypot(x - cx, y - cy) <= 12:
                    px[x, y] = (0, 0, 0, 0)
        glow = Image.new('RGBA', out.size, (0, 0, 0, 0))
        g = glow.load()
        for y in range(int(cy - R), int(cy + R) + 1):
            for x in range(int(cx - R), int(cx + R) + 1):
                if not (0 <= x < out.width and 0 <= y < out.height):
                    continue
                d = math.hypot(x - cx, y - cy)
                if d > R:
                    continue
                core = max(0.0, 1 - d / 7) ** 1.5
                halo = math.exp(-(d / 16) ** 2) * 0.85
                haze = (1 - d / R) ** 2.2 * 0.35
                w = min(1.0, core * 1.2)
                col = tuple(int(c + (t - c) * w) for c, t in zip(a.accent, (255, 244, 200)))
                g[x, y] = (*col, int(min(1.0, core + halo + haze) * 255))
        out = Image.alpha_composite(out, glow)

    out.save(a.dst, optimize=True)


if __name__ == '__main__':
    main()
