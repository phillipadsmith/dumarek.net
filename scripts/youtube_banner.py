#!/usr/bin/env python3
"""
Dumarek — YouTube channel banner generator.

Renders the 2560x1440 channel art from the site's own design tokens
(src/styles/global.css): vinyl black ground, the 70s record-sleeve
sunburst from the hero, and the gold -> tangerine -> magenta disco
gradient on the wordmark.

Everything that must be readable lives inside YouTube's 1546x423
"safe area", the only region every device shows.

    python3 scripts/youtube_banner.py            # -> public/youtube-banner.png
    python3 scripts/youtube_banner.py --guides   # + a safe-area overlay proof

Requires: pillow, fonttools[woff], and `npm install` (fonts come from
node_modules/@fontsource-variable).
"""

import argparse
import io
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent

# ---- design tokens (mirror of src/styles/global.css) -----------------
VINYL = (0x14, 0x10, 0x10)
CREAM = (0xF5, 0xED, 0xDF)
HAZE = (0xA9, 0x9B, 0x8C)
GOLD = (0xE8, 0xB8, 0x4B)
TANGERINE = (0xE8, 0x68, 0x3A)
MAGENTA = (0xD9, 0x4A, 0x8C)

# ---- YouTube channel art geometry ------------------------------------
W, H = 2560, 1440
SAFE_W, SAFE_H = 1546, 423          # visible on every device
TABLET_W = 1855                      # visible on tablet and up
SAFE_L = (W - SAFE_W) // 2           # 507
SAFE_T = (H - SAFE_H) // 2           # 508

SS = 4  # supersampling factor for the sunburst


def load_font(family: str, weight: int, size: int) -> ImageFont.FreeTypeFont:
    """Load a @fontsource-variable woff2 as a TTF at a given weight."""
    src = ROOT / "node_modules" / "@fontsource-variable" / family / "files"
    woff2 = src / f"{family}-latin-wght-normal.woff2"
    if not woff2.exists():
        sys.exit(f"missing font {woff2} — run `npm install` first")
    tt = TTFont(woff2)
    buf = io.BytesIO()
    tt.flavor = None
    tt.save(buf)
    buf.seek(0)
    font = ImageFont.truetype(buf, size)
    try:
        font.set_variation_by_axes([weight])
    except OSError:
        pass  # FreeType without variable support: static default weight
    return font


def tracked_width(font, text, tracking):
    return sum(font.getlength(c) for c in text) + tracking * max(len(text) - 1, 0)


def draw_tracked(draw, xy, text, font, fill, tracking):
    """Pillow has no letter-spacing; step per glyph."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + tracking
    return x - tracking


def disco_gradient(size, angle_bias=0.30):
    """linear-gradient(100deg, gold, tangerine 52%, magenta) as an image."""
    w, h = size
    img = Image.new("RGB", (w, h))
    px = img.load()
    stops = [(0.0, GOLD), (0.52, TANGERINE), (1.0, MAGENTA)]
    for x in range(w):
        for y in range(h):
            # 100deg in CSS is ~10deg past horizontal: nudge with y
            t = (x + (h - y) * angle_bias) / (w + h * angle_bias)
            t = min(max(t, 0.0), 1.0)
            for i in range(len(stops) - 1):
                p0, c0 = stops[i]
                p1, c1 = stops[i + 1]
                if p0 <= t <= p1:
                    k = 0 if p1 == p0 else (t - p0) / (p1 - p0)
                    px[x, y] = tuple(round(c0[j] + (c1[j] - c0[j]) * k) for j in range(3))
                    break
    return img


def gradient_text(base, xy, text, font, tracking=0):
    """Paint text with the disco gradient by using the glyphs as a mask."""
    w = int(tracked_width(font, text, tracking)) + 8
    asc, desc = font.getmetrics()
    h = asc + desc + 8
    mask = Image.new("L", (w, h), 0)
    draw_tracked(ImageDraw.Draw(mask), (0, 0), text, font, 255, tracking)
    base.paste(disco_gradient((w, h)), xy, mask)
    return xy[0] + w - 8


def sunburst(box_w, fade_top=0.25, opacity=0.95):
    """The hero's repeating-radial sunburst: concentric warm half-discs."""
    box_h = box_w // 2
    w, h = box_w * SS, box_h * SS
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx, cy = w / 2, h  # circle at 50% 100%
    R = ((w / 2) ** 2 + h ** 2) ** 0.5  # farthest-corner radius

    # outer -> inner, matching the CSS band stops
    for frac, color in [
        (0.61, GOLD + (255,)),
        (0.44, (0, 0, 0, 0)),
        (0.39, TANGERINE + (255,)),
        (0.22, (0, 0, 0, 0)),
        (0.17, MAGENTA + (255,)),
    ]:
        r = R * frac
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

    layer = layer.resize((box_w, box_h), Image.LANCZOS)

    # mask-image: linear-gradient(to top, black, transparent) — the hero's
    # dreamy top fade, tightened so the bands still read inside the 423px strip
    fade = Image.new("L", (box_w, box_h), 255)
    fp = fade.load()
    for y in range(box_h):
        pos = y / box_h            # 0 = top of box
        v = 255 if pos >= fade_top else int(255 * (pos / fade_top))
        for x in range(box_w):
            fp[x, y] = v
    alpha = layer.getchannel("A").point(lambda a: int(a * opacity))
    alpha = Image.composite(alpha, Image.new("L", alpha.size, 0), fade)
    layer.putalpha(alpha)
    return layer


def build(guides=False):
    img = Image.new("RGB", (W, H), VINYL)

    # a faint lift from the bottom so the black is not dead flat
    lift = Image.new("RGB", (1, H))
    lp = lift.load()
    for y in range(H):
        k = max(0.0, (y - H * 0.45) / (H * 0.55)) ** 2
        lp[0, y] = tuple(round(VINYL[i] + (0x1E - VINYL[i] + 6) * k) for i in range(3))
    img.paste(lift.resize((W, H)), (0, 0))

    # Sunburst. YouTube only ever shows the centred 423px-tall strip on
    # desktop, tablet and mobile — the full 1440 is TV only. So the sun is
    # sized and placed so its gold and tangerine bands sweep the right of
    # that strip, while the whole form still reads as a rising sun on TV.
    # It bleeds off the right edge exactly as the hero's does.
    burst_w = 2200
    burst = sunburst(burst_w)
    burst_cx = 2100
    img.paste(burst, (burst_cx - burst_w // 2, H - burst.height), burst)

    # ---- type, all inside the 1546x423 safe area ---------------------
    d = ImageDraw.Draw(img)
    x = SAFE_L + 40

    f_mark = load_font("bricolage-grotesque", 700, 152)
    f_tag = load_font("instrument-sans", 400, 46)
    f_meta = load_font("instrument-sans", 500, 25)

    edges = []

    # wordmark — uppercase and letterspaced like the site's .wordmark,
    # but carrying the disco gradient instead of sitting in haze
    y = SAFE_T + 48
    edges.append(gradient_text(img, (x, y), "DUMAREK", f_mark, tracking=8))

    # tagline, with "disco soul" taking the site's gradient accent
    y += 196
    head = "Producing pop records with a "
    d.text((x, y), head, font=f_tag, fill=CREAM)
    xt = x + f_tag.getlength(head)
    xt = gradient_text(img, (int(xt), y), "disco soul", f_tag)
    d.text((xt, y), ".", font=f_tag, fill=CREAM)
    edges.append(xt + f_tag.getlength("."))

    # microline, echoing the site's .eyebrow — its ● bullet is drawn, not
    # typed, because Instrument Sans has no glyph for it
    y += 88
    r = 6
    cy = y + f_meta.getmetrics()[0] * 0.55
    d.ellipse([x, cy - r, x + 2 * r, cy + r], fill=TANGERINE)
    edges.append(draw_tracked(
        d, (x + 2 * r + 18, y),
        "NAPA, CALIFORNIA  ·  DUMAREK.NET",
        f_meta, HAZE, 4.2,
    ))

    print(f"  text right edge: {max(edges):.0f}px  (sun left flank clears it)")

    if guides:
        g = img.copy()
        gd = ImageDraw.Draw(g)
        gd.rectangle([SAFE_L, SAFE_T, SAFE_L + SAFE_W, SAFE_T + SAFE_H],
                     outline=(0, 255, 128), width=4)
        gd.rectangle([(W - TABLET_W) // 2, SAFE_T,
                      (W + TABLET_W) // 2, SAFE_T + SAFE_H],
                     outline=(0, 180, 255), width=3)
        gd.rectangle([0, SAFE_T, W, SAFE_T + SAFE_H], outline=(255, 200, 0), width=3)
        return img, g
    return img, None


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--guides", action="store_true",
                    help="also write a proof with the safe-area boxes drawn on")
    ap.add_argument("-o", "--out", default=str(ROOT / "public" / "youtube-banner.png"))
    args = ap.parse_args()

    banner, proof = build(guides=args.guides)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    banner.save(out)
    print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KB)")
    if proof:
        p = out.with_name(out.stem + "-guides.png")
        proof.save(p)
        print(f"wrote {p}")
