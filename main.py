"""Draw the world news of Tuesday, 24 November 2026 as one clean,
dense newspaper front page — built to beat the previous day's
winning entries on hierarchy, legibility and date discipline.

Deterministic: no network, no clock, no randomness. Every run draws
the same pixels and writes the same PNG bytes to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png when that is set).
Standard library + Pillow only. All drawings are original; no photos.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (250, 246, 236)
INK = (26, 26, 26)
MUTED = (74, 74, 74)
RED = (166, 30, 30)
NAVY = (31, 56, 100)
GOLD = (176, 124, 0)
CARD = (255, 255, 255)
BORDER = (205, 198, 180)
WHITE = (255, 255, 255)

BADGE = {
    "CONFIRMED": (27, 122, 63),
    "REPORTED": (29, 78, 158),
    "CLAIM": (176, 124, 0),
    "OFFICIAL": (90, 90, 90),
}

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF = font("DejaVuSerif-Bold.ttf", 54)
F_SERIF_LEAD = font("DejaVuSerif-Bold.ttf", 22)
F_KICK = font("DejaVuSans-Bold.ttf", 15)
F_SUB = font("DejaVuSans.ttf", 17)
F_NUM = font("DejaVuSans-Bold.ttf", 30)
F_NUMLAB = font("DejaVuSans.ttf", 11)
F_REG = font("DejaVuSans-Bold.ttf", 10)
F_TL = font("DejaVuSans.ttf", 12)
F_LKICK = font("DejaVuSans-Bold.ttf", 14)
F_LSUM = font("DejaVuSans.ttf", 13)
F_GTAG = font("DejaVuSans-Bold.ttf", 11)
F_GHEAD = font("DejaVuSans-Bold.ttf", 16)
F_GSUM = font("DejaVuSans.ttf", 12)
F_BADGE = font("DejaVuSans-Bold.ttf", 10)
F_SRC = font("DejaVuSans.ttf", 10)
F_ALSO = font("DejaVuSans.ttf", 13)
F_ALSON = font("DejaVuSans-Bold.ttf", 13)
F_SECT = font("DejaVuSans-Bold.ttf", 14)
F_DC = font("DejaVuSans-Bold.ttf", 13)
F_DCT = font("DejaVuSans.ttf", 11)
F_FOOT = font("DejaVuSans.ttf", 10)

NUMBERS = [
    ("50+", "COP31 overtime hours"),
    ("7", "sea drones sank Merkury"),
    ("25", "Russian airspace violations"),
    ("$290bn", "Iran's damages demand"),
    ("+31.5%", "Nvidia shares jump"),
    ("96", "drones fired at Ukraine"),
]

REGIONS = [
    ("EUROPE", 3, (31, 56, 100)),
    ("MIDEAST", 5, (166, 30, 30)),
    ("ASIA-PAC", 5, (14, 122, 95)),
    ("AMERICAS", 2, (109, 40, 217)),
    ("AFRICA", 1, (194, 65, 12)),
    ("WORLD", 2, (90, 90, 90)),
]

TIMELINE = [
    ("01:32 GMT", "Nepal quake 5.3"),
    ("OVERNIGHT", "96 drones hit Ukraine"),
    ("07:52 GMT", "Hanoi blast kills 6"),
    ("TUESDAY", "Gaza plea; ICJ backed"),
]

# (num, tag, colour, headline, summary, badge, source)
LEADS = [
    (1, "ANTALYA  •  CLIMATE", (14, 122, 95),
     "COP31 COLLAPSES: NO DEAL, NO FOSSIL FUELS",
     "UN climate talks end with no deal after 50+ hours "
     "overtime — first collapse since 2009.",
     "CONFIRMED", "CNN · WSJ · Reuters"),
    (2, "OFF LIBYA  •  WAR", (29, 78, 158),
     "UKRAINE SINKS WARSHIP OFF LIBYA",
     "Seven sea drones sink corvette Merkury at Benghazi; "
     "cargo ship Angara struck too.",
     "CONFIRMED", "CNN · WSJ · Al Jazeera"),
    (3, "WASHINGTON  •  THE GULF", (166, 30, 30),
     "GULF STANDOFF DEEPENS",
     "Trump warns Iran of a \u201cvery traumatic\u201d outcome "
     "if no deal. US tightens its blockade.",
     "CONFIRMED", "Gulf News · Al Jazeera"),
]

GRID = [
    (4, "POLAND  •  NATO", (166, 30, 30),
     "Russia tests NATO skies",
     "25 violations in 2026. Missiles and a drone fell in "
     "Poland on 20 Nov; NATO met Mon.",
     "CONFIRMED", "Al Jazeera · ISW"),
    (5, "TECH  •  NVIDIA", (109, 40, 217),
     "Huang is back at Nvidia",
     "Reinstated 11 days after resigning, after Trump "
     "intervened. The US blacklists Megaspeed.",
     "CONFIRMED", "Al Jazeera · Reuters"),
    (6, "JUSTICE  •  MYANMAR", (55, 48, 163),
     "14 nations back Rohingya genocide ruling",
     "UK and 13 nations back the ICJ ruling on Myanmar's "
     "genocide. UK adds sanctions.",
     "CONFIRMED", "AFP · Daily Star"),
    (7, "NEPAL  •  QUAKE", (194, 65, 12),
     "Quake shakes Nepal",
     "Magnitude 5.3 near the Tibet border (Nepal: 5.6). "
     "Tremors felt in India, Bhutan, China.",
     "CONFIRMED", "Reuters · Kathmandu Post"),
    (8, "KYIV  •  WAR", (29, 78, 158),
     "Russia fires 96 drones overnight",
     "Ukraine's air force says 73 were downed or jammed, "
     "45 jet-powered. Hits at 13 sites.",
     "REPORTED", "Ukr. Pravda · Censor"),
    (9, "GAZA  •  AID", (166, 30, 30),
     "Gaza winter aid plea",
     "US senators urge Rubio to press Israel after rain "
     "flooded 70,000 tents, killing 4.",
     "CONFIRMED", "Anadolu · Roya News"),
    (10, "U.S.  •  TECH LAW", (109, 40, 217),
     "First states sue over Grok images",
     "Virginia and Oregon sue SpaceX, alleging Grok made "
     "sexual abuse images of children.",
     "CONFIRMED", "Reuters · Al Jazeera"),
    (11, "HANOI  •  BLAST", (194, 65, 12),
     "Hanoi blast kills 6",
     "Explosion in a crowded residential area of Vietnam's "
     "capital. 10 more are injured.",
     "REPORTED", "Reuters"),
    (12, "DHAKA  •  POLITICS", (55, 48, 163),
     "Hasina plans return",
     "Ousted Bangladesh PM Sheikh Hasina plans to return "
     "from exile in India on 16 Dec.",
     "REPORTED", "Reuters"),
]

# (num, place, text) — each fits one line
ALSO = [
    (13, "Zaporizhzhia", "Russian attack kills 2, wounds 22."),
    (14, "The Gulf", "At least 12 vessels struck in Nov."),
    (15, "Oil", "Brent $89.33, down 24% from $118 high."),
    (16, "New Delhi", "India pledges $1.62bn for Nepal."),
    (17, "Damascus", "US in talks to train Syrian forces."),
    (22, "Gaza", "100,000 tents in; 67,000 still waiting."),
]

# map pins: big numbered pins for the 3 leads, dots for the rest
LEAD_PINS = [(255, 40, 1), (250, 62, 2), (286, 62, 3)]
DOT_PINS = [
    (248, 26), (350, 50), (258, 30), (263, 58), (368, 62), (388, 70),
    (356, 56), (60, 30), (78, 40),
]
PIN_LABELS = [
    ("ANTALYA", 232, 26), ("BENGHAZI", 224, 74), ("GULF", 292, 74),
    ("KYIV", 240, 16), ("NEPAL", 336, 38), ("HANOI", 372, 82),
]

CONTINENTS = [
    [(18, 18), (95, 10), (135, 28), (120, 55), (95, 48), (80, 70),
     (55, 78), (30, 55), (12, 35)],
    [(95, 85), (125, 82), (140, 105), (125, 140), (105, 138), (92, 108)],
    [(215, 18), (250, 12), (265, 30), (245, 45), (220, 40)],
    [(225, 55), (260, 52), (275, 75), (260, 110), (235, 105), (222, 78)],
    [(270, 12), (360, 8), (420, 25), (450, 50), (410, 75), (370, 70),
     (330, 85), (300, 60), (275, 35)],
    [(390, 105), (430, 100), (445, 120), (415, 135), (390, 125)],
]


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def badge(draw, x, y, text, fnt=F_BADGE, h=15):
    col = BADGE[text]
    w = draw.textlength(text, font=fnt) + 12
    draw.rounded_rectangle([x, y, x + w, y + h], radius=7, fill=col)
    draw.text((x + 6, y + 2), text, font=fnt, fill=WHITE)
    return w


def draw_lead_art(draw, kind, x, y, w, h):
    if kind == 0:  # COP31: big globe, delegates, NO DEAL stamp
        draw.rectangle([x, y, x + w, y + h], fill=(18, 59, 60))
        draw.ellipse([x + 16, y + 14, x + 96, y + 94], fill=(58, 130, 140),
                     outline=(214, 226, 240), width=3)
        draw.ellipse([x + 40, y + 14, x + 72, y + 94], outline=(214, 226, 240),
                     width=2)
        draw.line([x + 16, y + 54, x + 96, y + 54], fill=(214, 226, 240),
                  width=2)
        for i, cx in enumerate((128, 164, 200, 236, 268)):
            draw.rectangle([x + cx, y + 58, x + cx + 24, y + 96],
                           fill=(201, 162, 39) if i % 2 else (214, 226, 240))
            draw.ellipse([x + cx + 4, y + 38, x + cx + 20, y + 54],
                         fill=(232, 196, 150) if i % 2 else (214, 180, 140))
        draw.rectangle([x + w - 132, y + 14, x + w - 12, y + 42],
                       fill=RED, outline=WHITE, width=2)
        tw = draw.textlength("NO DEAL", font=F_BADGE)
        draw.text((x + w - 132 + (120 - tw) / 2, y + 21), "NO DEAL",
                  font=F_BADGE, fill=WHITE)
    elif kind == 1:  # Merkury: big ship, blast, 7 drones
        draw.rectangle([x, y, x + w, y + h], fill=(15, 37, 64))
        draw.rectangle([x, y + 78, x + w, y + h], fill=(23, 68, 110))
        draw.polygon([(x + 60, y + 58), (x + 240, y + 58), (x + 218, y + 80),
                      (x + 82, y + 80)], fill=(120, 130, 145))
        draw.rectangle([x + 118, y + 28, x + 128, y + 58], fill=(120, 130, 145))
        draw.polygon([(x + 128, y + 28), (x + 172, y + 48), (x + 128, y + 48)],
                     fill=(200, 60, 40))
        for dx, dy in ((150, 18), (182, 10), (168, 32), (136, 32), (196, 28)):
            r = 12
            draw.polygon([(x + dx, y + dy - r), (x + dx + 4, y + dy - 2),
                          (x + dx + r, y + dy - 6), (x + dx + 5, y + dy + 3),
                          (x + dx + 9, y + dy + r), (x + dx, y + dy + 5),
                          (x + dx - 9, y + dy + r), (x + dx - 5, y + dy + 3),
                          (x + dx - r, y + dy - 6), (x + dx - 4, y + dy - 2)],
                         fill=(245, 158, 11))
        for dx, dy in ((36, 20), (252, 14), (282, 30), (210, 8)):
            draw.ellipse([x + dx, y + dy, x + dx + 8, y + dy + 8], fill=WHITE)
        draw.line([x + 36, y + 28, x + 60, y + 44], fill=WHITE, width=1)
        draw.line([x + 252, y + 22, x + 228, y + 40], fill=WHITE, width=1)
    else:  # Gulf: tanker, flame, waves
        draw.rectangle([x, y, x + w, y + h], fill=(31, 41, 55))
        draw.rectangle([x, y + 76, x + w, y + h], fill=(23, 68, 110))
        draw.polygon([(x + 36, y + 42), (x + 252, y + 42), (x + 236, y + 76),
                      (x + 52, y + 76)], fill=(150, 90, 40))
        draw.rectangle([x + 58, y + 22, x + 92, y + 42], fill=(200, 200, 200))
        draw.rectangle([x + 202, y + 18, x + 212, y + 42], fill=(200, 200, 200))
        draw.polygon([(x + 272, y + 12), (x + 296, y + 46), (x + 272, y + 66),
                      (x + 248, y + 46)], fill=(245, 158, 11))
        draw.ellipse([x + 263, y + 38, x + 281, y + 56], fill=WHITE)
        for wx in (16, 92, 168, 244):
            draw.arc([x + wx, y + 84, x + wx + 48, y + 100], 0, 180,
                     fill=(147, 197, 253), width=2)


def draw_lead(draw, idx, x, y, w):
    num, tag, col, head, summ, bdg, src = LEADS[idx]
    draw_lead_art(draw, idx, x, y, w, 110)
    draw.text((x, y + 116), tag, font=F_LKICK, fill=col)
    lines = wrap(draw, head, F_SERIF_LEAD, w)[:2]
    ty = y + 134
    for line in lines:
        draw.text((x, ty), line, font=F_SERIF_LEAD, fill=INK)
        ty += 26
    lines = wrap(draw, summ, F_LSUM, w)[:2]
    ty = y + 134 + 2 * 26 + 6
    for line in lines:
        draw.text((x, ty), line, font=F_LSUM, fill=MUTED)
        ty += 16
    by = y + 134 + 2 * 26 + 6 + 2 * 16 + 6
    bw = badge(draw, x, by, bdg)
    draw.text((x + bw + 8, by + 2), "Source: " + src, font=F_SRC, fill=MUTED)


def draw_grid_card(draw, idx, x, y, w, h):
    num, tag, col, head, summ, bdg, src = GRID[idx]
    draw.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=CARD,
                           outline=BORDER, width=1)
    draw.rectangle([x + 1, y + 1, x + w - 1, y + 6], fill=col)
    # badge top-right: the bottom of the card stays free for the summary
    bw = draw.textlength(bdg, font=F_BADGE) + 12
    badge(draw, x + w - bw - 10, y + 9, bdg)
    draw.text((x + 10, y + 11), "%d  •  %s" % (num, tag), font=F_GTAG, fill=col)
    lines = wrap(draw, head, F_GHEAD, w - 20)[:2]
    ty = y + 30
    for line in lines:
        draw.text((x + 10, ty), line, font=F_GHEAD, fill=INK)
        ty += 18
    lines = wrap(draw, summ, F_GSUM, w - 20)[:2]
    ty = y + 70
    for line in lines:
        draw.text((x + 10, ty), line, font=F_GSUM, fill=MUTED)
        ty += 13
    draw.text((x + 10, y + h - 12), src, font=F_SRC, fill=MUTED)


def draw_map(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(222, 234, 243),
                   outline=BORDER, width=1)
    for gx in range(0, w + 1, 46):
        draw.line([x + gx, y, x + gx, y + h], fill=(203, 218, 230), width=1)
    for gy in range(0, h + 1, 30):
        draw.line([x, y + gy, x + w, y + gy], fill=(203, 218, 230), width=1)
    sx, sy = w / 470.0, h / 150.0
    for poly in CONTINENTS:
        pts = [(x + px * sx, y + py * sy) for px, py in poly]
        draw.polygon(pts, fill=(233, 221, 193), outline=(182, 170, 142))
    for lx, ly in DOT_PINS:
        cx, cy = x + lx * sx, y + ly * sy
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=NAVY,
                     outline=WHITE, width=1)
    for px, py, n in LEAD_PINS:
        cx, cy = x + px * sx, y + py * sy
        draw.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=RED,
                     outline=WHITE, width=2)
        tw = draw.textlength(str(n), font=F_BADGE)
        draw.text((cx - tw / 2, cy - 5), str(n), font=F_BADGE, fill=WHITE)
    for label, lx, ly in PIN_LABELS:
        draw.text((x + lx * sx, y + ly * sy), label, font=F_SRC, fill=INK)
    draw.text((x + 8, y + h - 16), "Red pin = lead story  •  dot = grid story",
              font=F_SRC, fill=MUTED)


def section_head(draw, x, y, text):
    draw.rectangle([x, y, x + 5, y + 18], fill=RED)
    draw.text((x + 11, y), text, font=F_SECT, fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    mx = 22
    cw = W - 2 * mx

    # masthead: the date is the biggest thing on the page
    draw.rectangle([0, 0, W, 6], fill=RED)
    draw.text((mx, 11), "THE WORLD IN ONE DAY", font=F_KICK, fill=RED)
    right = "18 STORIES  •  6 REGIONS"
    rw = draw.textlength(right, font=F_KICK)
    draw.text((mx + cw - rw, 11), right, font=F_KICK, fill=MUTED)
    draw.text((mx, 30), "TUESDAY, 24 NOVEMBER 2026", font=F_SERIF, fill=INK)
    draw.text((mx, 90),
              "COP31 fails  •  Warship sunk off Libya  •  Gulf standoff deepens",
              font=F_SUB, fill=MUTED)
    draw.rectangle([mx, 110, mx + cw, 113], fill=GOLD)

    # key numbers strip
    bw = cw // 6
    for i, (val, lab) in enumerate(NUMBERS):
        bx = mx + i * bw
        if i:
            draw.line([bx, 120, bx, 158], fill=BORDER, width=1)
        vw = draw.textlength(val, font=F_NUM)
        draw.text((bx + (bw - vw) / 2, 118), val, font=F_NUM, fill=INK)
        lw = draw.textlength(lab, font=F_NUMLAB)
        draw.text((bx + (bw - lw) / 2, 150), lab, font=F_NUMLAB, fill=MUTED)
    draw.line([mx, 164, mx + cw, 164], fill=INK, width=1)

    # region bar (rects first, then labels)
    total = sum(c for _, c, _ in REGIONS)
    rx = mx
    segs = []
    for name, count, col in REGIONS:
        seg = int(round(cw * count / total))
        draw.rectangle([rx, 168, rx + seg - 2, 186], fill=col)
        segs.append((rx, seg, "%s %d" % (name, count)))
        rx += seg
    for rx, seg, label in segs:
        lw = draw.textlength(label, font=F_REG)
        draw.text((rx + (seg - lw) / 2, 171), label, font=F_REG, fill=WHITE)

    # timeline strip
    draw.rectangle([mx, 190, mx + cw, 212], fill=NAVY)
    draw.text((mx + 8, 195), "THE DAY IN UTC", font=F_TL, fill=(201, 162, 39))
    tx = mx + 128
    tw = (cw - 128) // 4
    for t, txt in TIMELINE:
        draw.text((tx, 195), t + "  " + txt, font=F_TL, fill=(214, 226, 240))
        tx += tw

    # leads: bigger art, bigger headlines
    lw = (cw - 2 * 16) // 3
    for i in range(3):
        draw_lead(draw, i, mx + i * (lw + 16), 218, lw)
    draw.line([mx, 470, mx + cw, 470], fill=INK, width=2)

    # grid: 3 x 3, roomier cards
    gw = (cw - 2 * 12) // 3
    for i in range(9):
        col, row = i % 3, i // 3
        draw_grid_card(draw, i, mx + col * (gw + 12), 476 + row * 114, gw, 110)
    draw.line([mx, 816, mx + cw, 816], fill=INK, width=2)

    # map (left) + also-on (right)
    section_head(draw, mx, 820, "THE WORLD — WHERE IT HAPPENED")
    draw_map(draw, mx, 842, 470, 116)
    ax = mx + 470 + 16
    section_head(draw, ax, 820, "ALSO ON TUESDAY")
    ay = 844
    for num, place, text in ALSO:
        draw.text((ax, ay), "%d." % num, font=F_ALSON, fill=RED)
        draw.text((ax + 26, ay), place + " — " + text, font=F_ALSO, fill=INK)
        ay += 20

    # date check
    draw.rounded_rectangle([mx, 962, mx + cw, 1000], radius=4,
                           outline=RED, width=2)
    draw.text((mx + 8, 967), "DATE CHECK", font=F_DC, fill=RED)
    dc1 = ("Every story above was reported on Tuesday, 24 November 2026. "
           "Oldest lead event: Poland, Fri 20 Nov. Nothing here is from "
           "before 20 Nov.")
    draw.text((mx + 108, 967), dc1, font=F_DCT, fill=INK)
    dc2 = ("LEFT OUT (not 24 Nov news): El Chapo Isidro captured Fri 20 Nov  •  "
           "US–Japan / US–Indonesia trade deals (Jul 2025)  •  SoftBank's $2bn "
           "Intel stake (Aug 2025)  •  ICJ Rohingya ruling itself (19 Nov).")
    lines = wrap(draw, dc2, F_DCT, cw - 16)
    draw.text((mx + 8, 980), lines[0] if lines else "", font=F_DCT, fill=INK)
    if len(lines) > 1:
        draw.text((mx + 8, 992), lines[1], font=F_DCT, fill=INK)

    # footer
    draw.text((mx, 1002),
              "SOURCES: Reuters · AP · CNN · WSJ · Al Jazeera · AFP · Gulf News · "
              "Ukr. Pravda · Kathmandu Post · Anadolu",
              font=F_FOOT, fill=MUTED)
    draw.text((mx, 1012),
              "CONFIRMED = 2+ outlets  •  REPORTED = carried by the wires today  •  "
              "Drawings are original, not photographs.",
              font=F_FOOT, fill=MUTED)

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    img.save(os.path.join(outdir, "entry.png"), format="PNG")


if __name__ == "__main__":
    main()
