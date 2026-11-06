import json, math, random, os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = json.load(open(os.path.join(HERE, 'base.json')))
IV = '#EFE8D8'; VI = '#8B6CC6'; OR = '#D4A537'; BK = '#1C1C1F'
JP = "'Dela Gothic One', sans-serif"
MIN = "'Shippori Mincho B1', serif"
AN = "'Anton', sans-serif"
BODY_J = "M260 54 L214 60 L148 86 Q116 92 102 124 L70 452 L128 460 L158 214 L160 472 L360 472 L362 214 L392 460 L450 452 L418 124 Q404 92 372 86 L306 60 Z"
BODY_P = "M70 30 H230 L232 48 L240 120 L236 460 H172 L152 176 Q150 171 148 176 L128 460 H64 L60 120 L68 48 Z"


def f(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def text(x, y, s, size, fill, fam=AN, anchor='middle', ls=0, extra=''):
    a = ' letter-spacing="%s"' % f(ls) if ls else ''
    return '<text x="%s" y="%s" font-family="%s" font-size="%s" fill="%s" text-anchor="%s"%s %s>%s</text>' % (
        f(x), f(y), fam, f(size), fill, anchor, a, extra, esc(s))


def vtext(x, y, s, size, fill, fam=MIN, step=None, weight='700', stroke=None):
    """Vertical (tategaki) text: one glyph per line, ー rotated."""
    step = step or size * 1.06
    out = []
    for i, ch in enumerate(s):
        cy = y + i * step
        if ch == ' ':
            continue
        st = ' stroke="%s" stroke-width="%s" paint-order="stroke" stroke-linejoin="round"' % stroke if stroke else ''
        if ch in 'ー〜':
            out.append('<text x="0" y="0" font-family="%s" font-weight="%s" font-size="%s" fill="%s" text-anchor="middle" dominant-baseline="central" transform="translate(%s %s) rotate(90)"%s>%s</text>' % (
                fam, weight, f(size), fill, f(x), f(cy), st, ch))
        else:
            dx = size * 0.12 if ch in 'ョッャュぁぃぅぇぉっゃゅょァィゥェォ' else 0
            dy = -size * 0.12 if dx else 0
            out.append('<text x="%s" y="%s" font-family="%s" font-weight="%s" font-size="%s" fill="%s" text-anchor="middle" dominant-baseline="central"%s>%s</text>' % (
                f(x + dx), f(cy + dy), fam, weight, f(size), fill, st, ch))
    return ''.join(out)


def vlen(s, size, step=None):
    return len(s) * (step or size * 1.06)


def disc(cx, cy, r, label=None, rot=0, sy=1, labcol=VI, ring=None):
    """A DISC: ivory platter, black grooves, gold hub."""
    o = ['<g transform="translate(%s %s) rotate(%s) scale(1 %s)">' % (f(cx), f(cy), f(rot), f(sy))]
    if ring:
        o.append('<circle cx="0" cy="0" r="%s" fill="none" stroke="%s" stroke-width="%s"></circle>' % (f(r + r * 0.12), ring, f(max(1.2, r * 0.09))))
    o.append('<circle cx="0" cy="0" r="%s" fill="%s"></circle>' % (f(r), IV))
    for k in (0.9, 0.8, 0.7, 0.6):
        o.append('<circle cx="0" cy="0" r="%s" fill="none" stroke="%s" stroke-width="%s"></circle>' % (f(r * k), BK, f(max(0.25, r * 0.012))))
    # sheen arcs
    a0, a1 = math.radians(-150), math.radians(-105)
    for k in (0.85, 0.65):
        rr = r * k
        o.append('<path d="M%s %s A%s %s 0 0 1 %s %s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"></path>' % (
            f(rr * math.cos(a0)), f(rr * math.sin(a0)), f(rr), f(rr), f(rr * math.cos(a1)), f(rr * math.sin(a1)), VI, f(max(0.6, r * 0.05))))
    o.append('<circle cx="0" cy="0" r="%s" fill="%s"></circle>' % (f(r * 0.36), OR))
    o.append('<circle cx="0" cy="0" r="%s" fill="%s"></circle>' % (f(r * 0.2), IV))
    o.append('<circle cx="0" cy="0" r="%s" fill="%s"></circle>' % (f(r * 0.1), BK))
    if label:
        o.append(text(0, r * 0.62, label, r * 0.2, labcol, AN, ls=r * 0.02, extra='dominant-baseline="central"'))
    o.append('</g>')
    return ''.join(o)


def stitch_disc(cx, cy, r, label=None):
    """DISC drawn as running stitches only (sashiko)."""
    o = []
    o.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="3.4 2.4" stroke-linecap="round"></circle>' % (f(cx), f(cy), f(r), IV))
    for k in (0.78, 0.6):
        o.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="1" stroke-dasharray="2.4 2.2" stroke-linecap="round"></circle>' % (f(cx), f(cy), f(r * k), IV))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"></circle>' % (f(cx), f(cy), f(r * 0.34), OR))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"></circle>' % (f(cx), f(cy), f(r * 0.12), BK))
    if label:
        o.append(text(cx, cy + r + 9, label, 7.5, OR, AN, ls=1.5))
    return ''.join(o)


def floret(x, y, s, rot):
    o = []
    for k in range(4):
        a = math.radians(rot + k * 90)
        px, py = x + math.cos(a) * s * 0.5, y + math.sin(a) * s * 0.5
        o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="0.6" transform="rotate(%s %s %s)"></ellipse>' % (
            f(px), f(py), f(s * 0.46), f(s * 0.34), VI, BK, f(rot + k * 90), f(px), f(py)))
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"></circle>' % (f(x), f(y), f(s * 0.15), IV))
    return ''.join(o)


def leaf(x, y, L, ang):
    a = math.radians(ang)
    ex, ey = x + math.cos(a) * L, y + math.sin(a) * L
    nx, ny = -math.sin(a) * L * 0.32, math.cos(a) * L * 0.32
    mx, my = (x + ex) / 2, (y + ey) / 2
    d = 'M%s %s Q%s %s %s %s Q%s %s %s %s Z' % (f(x), f(y), f(mx + nx), f(my + ny), f(ex), f(ey), f(mx - nx), f(my - ny), f(x), f(y))
    v = 'M%s %s L%s %s' % (f(x), f(y), f(ex), f(ey))
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="0.7"></path><path d="%s" stroke="%s" stroke-width="0.8" fill="none"></path>' % (d, OR, BK, v, BK)


def hydrangea(cx, cy, R, n=None, seed=1, leaves=((200, 1.2), (340, 1.1))):
    rnd = random.Random(seed)
    n = n or int(R * 0.9)
    o = []
    for ang, k in leaves:
        a = math.radians(ang)
        o.append(leaf(cx + math.cos(a) * R * 0.55, cy + math.sin(a) * R * 0.55, R * k, ang))
    pts = []
    for i in range(n):
        rr = R * math.sqrt((i + 0.5) / n)
        th = i * 2.39996
        pts.append((cx + rr * math.cos(th), cy + rr * math.sin(th) * 0.92))
    pts.sort(key=lambda p: p[1])
    s = R * 0.36
    for x, y in pts:
        o.append(floret(x, y, s, rnd.uniform(0, 90)))
    return ''.join(o)


def beetle(cx, cy, u, rot=0):
    o = ['<g transform="translate(%s %s) rotate(%s)">' % (f(cx), f(cy), f(rot))]
    sw = f(u * 0.42)
    legs = [(-1.6, -2.6, -3.4, -4.4, -4.0, -6.0), (-2.1, 0.2, -4.0, 0.6, -4.6, 2.6), (-2.0, 2.8, -3.6, 4.8, -4.0, 7.2)]
    for a, b, c, d, e, g in legs:
        for sg in (1, -1):
            o.append('<path d="M%s %s L%s %s L%s %s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"></path>' % (
                f(sg * a * u), f(b * u), f(sg * c * u), f(d * u), f(sg * e * u), f(g * u), OR, sw))
    # horn
    o.append('<path d="M%s %s Q%s %s 0 %s Q%s %s %s %s Z" fill="%s" stroke="%s" stroke-width="%s"></path>' % (
        f(-0.55 * u), f(-4.4 * u), f(-0.7 * u), f(-6.6 * u), f(-8.2 * u), f(0.7 * u), f(-6.6 * u), f(0.55 * u), f(-4.4 * u), OR, BK, f(u * 0.12)))
    o.append('<path d="M0 %s L%s %s M0 %s L%s %s" stroke="%s" stroke-width="%s" stroke-linecap="round"></path>' % (
        f(-7.7 * u), f(-1.0 * u), f(-8.8 * u), f(-7.7 * u), f(1.0 * u), f(-8.8 * u), OR, f(u * 0.45)))
    o.append('<ellipse cx="0" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"></ellipse>' % (f(-4.1 * u), f(1.0 * u), f(0.75 * u), OR, BK, f(u * 0.12)))
    o.append('<ellipse cx="0" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"></ellipse>' % (f(-2.5 * u), f(2.3 * u), f(1.5 * u), OR, BK, f(u * 0.14)))
    o.append('<path d="M0 %s C%s %s %s %s 0 %s C%s %s %s %s 0 %s Z" fill="%s" stroke="%s" stroke-width="%s"></path>' % (
        f(-1.2 * u), f(3.0 * u), f(-1.2 * u), f(3.0 * u), f(5.2 * u), f(6.4 * u), f(-3.0 * u), f(5.2 * u), f(-3.0 * u), f(-1.2 * u), f(-1.2 * u), OR, BK, f(u * 0.14)))
    o.append('<path d="M0 %s L0 %s M%s %s Q%s %s %s %s M%s %s Q%s %s %s %s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"></path>' % (
        f(-1.2 * u), f(6.3 * u), f(1.2 * u), f(0.2 * u), f(1.9 * u), f(2.6 * u), f(1.2 * u), f(4.8 * u), f(-1.2 * u), f(0.2 * u), f(-1.9 * u), f(2.6 * u), f(-1.2 * u), f(4.8 * u), BK, f(u * 0.14)))
    o.append('</g>')
    return ''.join(o)


def sparkle(x, y, r, col=OR):
    k = r * 0.22
    d = 'M%s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s Z' % (
        f(x), f(y - r), f(x + k), f(y - k), f(x + r), f(y), f(x + k), f(y + k), f(x), f(y + r), f(x - k), f(y + k), f(x - r), f(y), f(x - k), f(y - k), f(x), f(y - r))
    return '<path d="%s" fill="%s"></path>' % (d, col)


def cloud(cx, cy, s, flip=1):
    circles = [(-1.6, 0.3, 0.9), (-0.5, -0.5, 1.15), (0.8, -0.1, 1.0), (1.8, 0.45, 0.75), (0.2, 0.6, 0.85)]
    o = []
    for dx, dy, r in circles:
        x, y, rr = cx + flip * dx * s, cy + dy * s, r * s
        o.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.8"></circle>' % (f(x), f(y), f(rr), BK, IV))
        # curl
        o.append('<path d="M%s %s A%s %s 0 1 %s %s %s" fill="none" stroke="%s" stroke-width="1.3" stroke-linecap="round"></path>' % (
            f(x - flip * rr * 0.45), f(y), f(rr * 0.45), f(rr * 0.45), 1 if flip > 0 else 0, f(x + flip * rr * 0.1), f(y - rr * 0.42), IV))
    return ''.join(o)


def moon_phase(cx, cy, r, lit):
    """lit: 1 full, 0 new. waning from the right."""
    if lit >= 0.999:
        return '<circle cx="%s" cy="%s" r="%s" fill="%s"></circle>' % (f(cx), f(cy), f(r), IV)
    if lit <= 0.001:
        return '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.4"></circle>' % (f(cx), f(cy), f(r), BK, OR)
    # lit portion on the left side (waning)
    k = 2 * lit - 1  # -1..1
    rx = abs(k) * r
    sweep_t = 1 if k > 0 else 0
    d = 'M%s %s A%s %s 0 0 0 %s %s A%s %s 0 0 %d %s %s Z' % (
        f(cx), f(cy - r), f(r), f(r), f(cx), f(cy + r), f(rx), f(r), sweep_t, f(cx), f(cy - r))
    return '<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="0.8" stroke-dasharray="1.6 1.6"></circle><path d="%s" fill="%s"></path>' % (f(cx), f(cy), f(r), IV, d, IV)


def sleeve_pt(t, side='L', y0=214, y1=440):
    """Point on the centre line of a sleeve at fraction t (front & back share the outline)."""
    y = y0 + (y1 - y0) * t
    xo = 102 + (y - 124) * (70 - 102) / (452 - 124)
    xi = 158 + (y - 214) * (128 - 158) / (460 - 214)
    x = (xo + xi) / 2
    if side == 'R':
        x = 520 - x
    return x, y


def sleeve_edges(y, side='L'):
    xo = 102 + (y - 124) * (70 - 102) / (452 - 124)
    xi = 158 + (y - 214) * (128 - 158) / (460 - 214)
    if side == 'R':
        return 520 - xi, 520 - xo
    return xo, xi


SLEEVE_ANG = math.degrees(math.atan2(440 - 214, sleeve_pt(1)[0] - sleeve_pt(0)[0]))  # ~ 96


def svg(w, h, vb, label, body):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (w, h, vb, esc(label).replace('"', '&quot;'), body)


def jacket_front(deco, label, over_pockets='', defs=''):
    b = ''.join(BASE['F_UNDER']) + ''.join(BASE['F_POCK']) + deco + over_pockets + ''.join(BASE['F_COLLAR']) + ''.join(BASE['F_BTN'])
    return svg(540, 540, '0 0 520 520', label, defs + b)


def jacket_back(deco, label, defs=''):
    b = ''.join(BASE['B_UNDER']) + deco + ''.join(BASE['B_COLLAR']) + ''.join(BASE['B_TOP'])
    return svg(540, 540, '0 0 520 520', label, defs + b)


def jeans_front(deco, label, defs=''):
    b = ''.join(BASE['J_F_UNDER']) + deco + ''.join(BASE['J_F_TOP'])
    return svg(270, 432, '0 0 300 480', label, defs + b)


def jeans_back(deco, label, defs='', after_pockets=''):
    b = ''.join(BASE['J_B_UNDER']) + deco + after_pockets + ''.join(BASE['J_B_TOP'])
    return svg(270, 432, '0 0 300 480', label, defs + b)


def cuff_bands(colors=(OR, VI)):
    o = []
    for i, c in enumerate(colors):
        dy = 11.5 + i * 9
        o.append('<path d="M%s %sL%s %sM%s %sL%s %s" stroke="%s" stroke-width="3.6" fill="none"></path>' % (
            f(73.1 - 0.12 * dy), f(420 + dy), f(132.1 - 0.15 * dy), f(427 + dy), f(446.9 + 0.12 * dy), f(420 + dy), f(387.9 + 0.15 * dy), f(427 + dy), c))
    return ''.join(o)


SW = [('#1C1C1F', 'Noir', 'ta veste'), ('#6F6F73', 'Gris', 'col sherpa'), (IV, 'Ivoire', IV), (VI, 'Violet', VI), (OR, 'Or', OR)]


def page(title, h1, sub, jf, jb, pf, pb, idea, howto):
    sw = ''.join('<div style="display: flex; align-items: center; gap: 8px"><span style="width: 22px; height: 22px; border-radius: 6px; background: %s; border: 1px solid rgba(0, 0, 0, 0.2); display: inline-block"></span><span style="font-size: 14px; color: #1A1A1A">%s <span style="color: #5F5B54">%s</span></span></div>' % c for c in SW)

    def fig(s, cap):
        return '<figure style="margin: 0; display: flex; flex-direction: column; align-items: center; gap: 6px">%s<figcaption style="font-size: 13px; letter-spacing: 0.14em; text-transform: uppercase; color: #5F5B54">%s</figcaption></figure>' % (s, cap)

    def box(h, t):
        return '<div style="width: 230px; box-sizing: border-box; padding: 18px 18px 20px; background: #F7F5F1; border-radius: 14px; border: 1px solid rgba(0, 0, 0, 0.08); display: flex; flex-direction: column; gap: 8px; align-self: flex-start; margin-top: 8px"><div style="font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: #5F5B54; font-weight: 500">%s</div><div style="font-size: 13.5px; line-height: 1.5; color: #1A1A1A">%s</div></div>' % (h, t)

    return '''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Dela+Gothic+One&amp;family=Shippori+Mincho+B1:wght@700;800&amp;family=Inter:wght@400;500&amp;display=swap">
<style>
body{margin:0}
a{color:#666}a:hover{color:#333}
</style>
</helmet>
<div style="width: 1200px; height: 1190px; box-sizing: border-box; padding: 32px 48px 28px; background: #ECE9E3; display: flex; flex-direction: column; gap: 18px; font-family: 'Inter', sans-serif; color: #1A1A1A">
<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 24px">
<div style="display: flex; flex-direction: column; gap: 4px">
<h1 style="margin: 0; font-family: 'Anton', sans-serif; font-weight: 400; font-size: 34px; line-height: 1.05; letter-spacing: 0.02em; white-space: nowrap; color: #1A1A1A">%s</h1>
<p style="margin: 0; font-size: 15px; color: #5F5B54">%s</p>
</div>
<div style="display: flex; gap: 18px; align-items: center">%s</div>
</div>
<div style="display: flex; gap: 24px; justify-content: center">
%s
%s
</div>
<div style="display: flex; gap: 32px; justify-content: center">
%s
%s
%s
%s
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1200,"height":1190}}'>
class Component extends DCLogic {
renderVals() {
return {};
}
}
</script>
</body>
</html>
''' % (title, h1, sub, sw, fig(jf, 'Veste · devant'), fig(jb, 'Veste · dos'), box('D’où vient l’idée', idea), fig(pf, 'Jean · devant'), fig(pb, 'Jean · dos'), box('Comment le faire', howto))
