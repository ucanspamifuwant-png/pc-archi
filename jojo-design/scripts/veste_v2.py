"""V2 of the four kept directions : jacket on the user's photos, jeans, and a strip of alternative palettes."""
import json, sys, math
from lib import f, text, esc, BASE, AN, JP, MIN, IV, BK
from PIL import Image as _I

URLS = json.load(open(sys.argv[1]))
OUT = sys.argv[2]
ASSETS = sys.argv[3]

BACK_CROP, KB = (0, 182, 528, 800), 1.13
FRONT_CROP, KF = (0, 262, 586, 905), 0.80
BY, FY = BACK_CROP[1], FRONT_CROP[1]
KM = 0.667
KJ = 0.9


def _ar(n):
    w, h = _I.open('%s/%s.png' % (ASSETS, n)).size
    return w / h


# ------------------------------------------------------------------ seams traced on the back photo
L = [(115, 335), (128, 380), (140, 430), (149, 480), (155, 530), (160, 580), (165, 630), (169, 670), (172, 705)]
R = [(420, 330), (410, 380), (400, 430), (390, 480), (380, 530), (373, 580), (365, 630), (360, 670), (355, 705)]
Y = [(92, 342), (115, 331), (150, 318), (210, 306), (260, 302), (310, 304), (370, 314), (420, 328), (425, 330)]
LSIDE = [(96, 342), (100, 440), (102, 560), (104, 705)]
RSIDE = [(440, 338), (438, 440), (436, 560), (440, 705)]


def poly(pts, close=False):
    return 'M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts) + (' Z' if close else '')


PANEL = poly(L + R[::-1] + [(370, 314), (310, 304), (260, 302), (210, 306), (150, 318)], True)
LPANEL = poly([(96, 342), (115, 335)] + L + [(104, 705), (102, 560), (100, 440)], True)
RPANEL = poly([(420, 330), (440, 338), (438, 440), (436, 560), (440, 705)] + R[::-1], True)
YOKE = poly([(84, 318), (66, 288), (125, 252), (197, 234), (262, 230), (334, 234), (400, 252), (456, 282), (446, 316), (440, 338)] + Y[::-1], True)
SLT = poly([(66, 288), (44, 330), (40, 346), (97, 346), (96, 342), (84, 318)], True)
SLR = poly([(456, 282), (480, 326), (486, 346), (438, 346), (440, 338), (446, 316)], True)
CUFF_L = poly([(28, 744), (106, 750), (104, 794), (62, 798), (36, 774)], True)
CUFF_R = poly([(500, 744), (426, 750), (428, 794), (466, 798), (490, 774)], True)
F_CUFF_L = 'M30 800 H100 L98 862 H44 Z'
F_CUFF_R = 'M454 800 H524 L510 858 L456 862 Z'
F_FLAP_L = 'M78 434 H192 V470 L135 492 L78 470 Z'
F_FLAP_R = 'M362 434 H476 V470 L419 492 L362 470 Z'
# jeans (300 x 480 drawing)
J_HEMS = 'M60 408 H132 V452 H60 Z M168 408 H238 V452 H168 Z'
J_YOKE = 'M68 48 H231 L237 96 L150 116 L63 96 Z'
J_LPOCK = 'M82 118 L132 114 L130 170 L107 182 L84 170 Z'
J_RPOCK = 'M218 118 L168 114 L170 170 L193 182 L216 170 Z'
J_COIN = 'M198 62 H214 V78 H198 Z'


def lerp_seam(seam, y):
    for (x0, y0), (x1, y1) in zip(seam, seam[1:]):
        if y0 <= y <= y1:
            return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    return seam[-1][0]


def stitches(col, w=2):
    d = 'fill="none" stroke="%s" stroke-width="%s" stroke-dasharray="6 4" stroke-linecap="round"' % (col, w)
    return ''.join('<path d="%s" %s></path>' % (p, d) for p in (
        poly([(x + 5, y) for x, y in L]), poly([(x - 5, y) for x, y in R]), poly([(x, y + 5) for x, y in Y[2:-2]])))


def cross(x, y, h, col, w=2.8):
    return '<path d="M%s %s V%s M%s %s H%s" stroke="%s" stroke-width="%s" stroke-linecap="round"></path>' % (
        f(x), f(y - h / 2), f(y + h / 2), f(x - h * 0.32), f(y - h * 0.18), f(x + h * 0.32), col, f(w))


def vcol(chars, x0, y0, x1, y1, size, col, fam=MIN, weight='800'):
    o = []
    n = len(chars)
    for i, ch in enumerate(chars):
        t = i / max(1, n - 1)
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        o.append('<text x="%s" y="%s" font-family="%s" font-weight="%s" font-size="%s" fill="%s" text-anchor="middle" dominant-baseline="central">%s</text>' % (f(x), f(y), fam, weight, size, col, ch))
    return ''.join(o)


def clipped(cid, d, inner):
    return '<defs><clipPath id="%s"><path d="%s"></path></clipPath></defs><g clip-path="url(#%s)">%s</g>' % (cid, d, cid, inner)


def rect(col, x=0, y=0, w=600, h=900):
    return '<rect x="%d" y="%d" width="%d" height="%d" fill="%s"></rect>' % (x, y, w, h, col)


def stripes_block(y0, y1, col, x0=20, x1=508, step=11, size=7, ls=2.4):
    o = []
    for i, y in enumerate(range(y0, y1, step)):
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%s"></line>' % (x0, y, x1, y, col, f(step * 0.08)))
        if i % 2 == 0:
            o.append(text(x0 + (i * 7) % 20, y + size * 1.15, 'G Δ C T ' * 24, size, col, AN, anchor='start', ls=ls))
    return ''.join(o)


def dots(x0, y0, cols, rows, step, r_of_row):
    o = []
    for row in range(rows):
        y = y0 + row * step
        rr = r_of_row(row)
        for col in range(cols):
            x = x0 + col * (step - 1) + ((step - 1) / 2 if row % 2 else 0)
            o.append('M%s %sa%s %s 0 1 0 0.01 0Z' % (f(x - rr), f(y), f(rr), f(rr)))
    return ''.join(o)


def tally(x, y, light, acc, h=9, w=1.6):
    o = ''.join('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="round"></line>' % (
        f(x - 6 + kk * 4), f(y - h), f(x - 6 + kk * 4), f(y + h), light, f(w)) for kk in range(4))
    return o + '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="round"></line>' % (f(x - 9), f(y + h * 0.66), f(x + 9), f(y - h * 0.66), acc, f(w))


# ------------------------------------------------------------------ html helpers
def img(name, cx, cy, w, k, y0, rot=0, extra='', alt=''):
    W = w * k
    H = W / _ar(name)
    return ('<img src="%s" alt="%s" style="position: absolute; left: %.1fpx; top: %.1fpx; width: %.1fpx; height: %.1fpx; transform: rotate(%sdeg)%s">'
            % (URLS[name], alt, cx * k - W / 2, (cy - y0) * k - H / 2, W, H, rot, extra))


def img_top(name, cx, top, h, k, y0, alt=''):
    H = h * k
    W = H * _ar(name)
    return ('<img src="%s" alt="%s" style="position: absolute; left: %.1fpx; top: %.1fpx; width: %.1fpx; height: %.1fpx">'
            % (URLS[name], alt, cx * k - W / 2, (top - y0) * k, W, H))


def layer(svg_inner, crop, k):
    W, H = crop[2] - crop[0], crop[3] - crop[1]
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%.0f" height="%.0f" viewBox="0 0 %d %d" style="position: absolute; left: 0px; top: 0px" aria-hidden="true">'
            '<g transform="translate(0 %d)">%s</g></svg>') % (W * k, H * k, W, H, -crop[1], svg_inner)


def mock(photo, crop, k, layers, label):
    W, H = crop[2] - crop[0], crop[3] - crop[1]
    return ('<div role="img" aria-label="%s" style="position: relative; width: %.0fpx; height: %.0fpx">'
            '<img src="%s" alt="" style="position: absolute; left: 0px; top: 0px; width: %.0fpx; height: %.0fpx">%s</div>') % (
        esc(label), W * k, H * k, URLS[photo], W * k, H * k, ''.join(layers))


def pocket_disc(name, k=KF):
    return img(name, 135, 424, 64, k, FY, 0, '; clip-path: inset(0 0 34% 0)', 'DISC glissé dans la poche')


def ws_center(name, k, top=345, bottom=705):
    return img_top(name, 262, top, bottom - top, k, BY, 'Pale Snake, image de l’anime')


def jsvg(inner):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="270" height="432" viewBox="0 0 300 480" style="position: absolute; left: 0px; top: 0px" aria-hidden="true">%s</svg>' % inner


def jean(under, imgs, over, label):
    return '<div role="img" aria-label="%s" style="position: relative; width: 270px; height: 432px">%s%s%s</div>' % (esc(label), jsvg(under), imgs, jsvg(over))


def jimg(name, cx, cy, w, rot=0, extra='', alt='DISC'):
    W = w * KJ
    H = W / _ar(name)
    return ('<img src="%s" alt="%s" style="position: absolute; left: %.1fpx; top: %.1fpx; width: %.1fpx; height: %.1fpx; transform: rotate(%sdeg)%s">'
            % (URLS[name], alt, cx * KJ - W / 2, cy * KJ - H / 2, W, H, rot, extra))


def back_pocket_disc(name):
    return jimg(name, 193, 110, 36, 0, '; clip-path: inset(0 0 42% 0)', 'DISC glissé dans la poche arrière')


JF_UNDER, JF_TOP = ''.join(BASE['J_F_UNDER']), ''.join(BASE['J_F_TOP'])
JB_UNDER, JB_TOP = ''.join(BASE['J_B_UNDER']), ''.join(BASE['J_B_TOP'])

# ------------------------------------------------------------------ palettes
GREY = '#A9A9B0'
PAL = {
    'lilas': dict(main='#A58FCB', accent=GREY, light=IV, ws='ws-lilas', disc='disc-incline-lilas', discface='disc-face-lilas',
                  name='Lilas et gris', chips=[(IV, 'Ivoire'), ('#A58FCB', 'Lilas'), (GREY, 'Gris clair')]),
    'ivoire': dict(main=IV, accent=IV, light=IV, ws='ws-ivoire', disc='disc-incline-ivoire', discface='disc-face-ivoire',
                   name='Ivoire seul', chips=[(IV, 'Ivoire')]),
    'bordeaux': dict(main='#9B3B52', accent='#9B3B52', light=IV, ws='ws-bordeaux', disc='disc-incline-ivoire', discface='disc-face-bordeaux',
                     name='Bordeaux et ivoire', chips=[(IV, 'Ivoire'), ('#9B3B52', 'Bordeaux')]),
    'vo-a': dict(main='#7B5CC4', accent='#F08D3E', light=IV, ws='ws-vo-a', disc='disc-incline-vo-a', discface='disc-face-vo-a',
                 name='Crépuscule · violet, ivoire, orange', chips=[(IV, 'Ivoire'), ('#7B5CC4', 'Violet'), ('#F08D3E', 'Orange')]),
    'vo-b': dict(main='#9466E8', accent='#FF8A3D', light='#FF8A3D', ws='ws-vo-b', disc='disc-incline-vo-b', discface='disc-face-vo-a',
                 name='Néon · violet vif, orange vif', chips=[('#9466E8', 'Violet vif'), ('#FF8A3D', 'Orange vif')]),
}


# ================================================================== 1 · Couronne
def back_couronne(p, k, pre):
    main, acc, light = p['main'], p['accent'], p['light']
    s = clipped(pre + 'band', YOKE + ' ' + SLT + ' ' + SLR, stripes_block(236, 350, main))
    s += stitches(acc, 1.8)
    for seam, ref in ((L, LSIDE), (R, RSIDE)):
        for j, ch in enumerate('GΔCTGΔCTGΔ'):
            y = 380 + j * 16
            x = (lerp_seam(seam, y) + lerp_seam(ref, y)) / 2
            s += text(x, y, ch, 12, main if j % 2 else light, AN, extra='dominant-baseline="central"')
    s += text(262, 738, 'G Δ C T · G Δ C T · G Δ C T', 12, acc, AN, ls=2)
    return [layer(s, BACK_CROP, k), img_top(p['ws'], 262, 248, 457, k, BY, 'Pale Snake, image de l’anime')]


def front_couronne(p, k, pre):
    region = 'M84 400 H200 V432 H84 Z M346 402 H484 V434 H346 Z ' + F_CUFF_L + ' ' + F_CUFF_R
    s = clipped(pre + 'fb', region, stripes_block(396, 870, p['main'], x0=20, x1=540))
    return [layer(s, FRONT_CROP, k), pocket_disc(p['discface'], k)]


def jeans_couronne(p):
    main, light = p['main'], p['light']
    hem = stripes_block(404, 456, main, x0=40, x1=260, step=8, size=5, ls=1.8)
    front = clipped('j1f', J_HEMS, hem)
    for j, ch in enumerate('GΔCTGΔCTGΔCTGΔCT'):
        front += text(72, 92 + j * 18, ch, 9, main if j % 2 else light, AN, extra='dominant-baseline="central"')
    back = clipped('j1b', J_HEMS + ' ' + J_YOKE, hem + stripes_block(44, 118, main, x0=40, x1=260, step=8, size=5, ls=1.8))
    return (jean(JF_UNDER + front, '', JF_TOP, 'Jean, devant : rayures GΔCT aux ourlets, colonne de lettres le long de la couture extérieure gauche.'),
            jean(JB_UNDER + back, back_pocket_disc(p['discface']), JB_TOP, 'Jean, dos : rayures GΔCT sur l’empiècement et aux ourlets, un DISC qui dépasse de la poche droite.'),
            'Les rayures GΔCT reviennent aux ourlets, devant et derrière, et sur l’empiècement arrière du jean, comme sur celui de la veste. Une colonne de lettres descend la couture extérieure gauche. Un DISC dépasse de la poche arrière droite.')


# ================================================================== 2 · Sérigraphie
def back_serigraphie(p, k, pre):
    main, light = p['main'], p['light']
    s = clipped(pre + 'panel', PANEL, '<path d="%s" fill="%s"></path>' % (dots(112, 322, 40, 44, 9, lambda r: 0.4 + 2.6 * (r / 43) ** 1.4), main))
    s += clipped(pre + 'sides', LPANEL + ' ' + RPANEL, '<path d="%s" fill="%s"></path>' % (dots(90, 350, 50, 40, 9, lambda r: 1.8 - 1.5 * (r / 39)), main))
    s += text(262, 290, 'ホワイトスネイク', 22, light, JP, ls=3)
    s += text(258, 738, '2 3 5 7 11 13 17 19 23', 12, light, AN, ls=2.4)
    discs = ''.join(img(p['disc'], x, y, w, k, BY, r, alt='DISC') for x, y, w, r in ((120, 395, 42, 18), (128, 462, 46, -12), (414, 395, 42, -18), (406, 462, 46, 12)))
    return [layer(s, BACK_CROP, k), img_top(p['ws'], 262, 292, 413, k, BY, 'Pale Snake, image de l’anime en trame'), discs]


def front_serigraphie(p, k, pre):
    s = text(419, 459, 'PALE SNAKE', 9, p['light'], AN, ls=2)
    s += clipped(pre + 'fc', F_CUFF_L + ' ' + F_CUFF_R, '<path d="%s" fill="%s"></path>' % (dots(20, 802, 70, 7, 9, lambda r: 2.4 - 0.3 * r), p['main']))
    return [layer(s, FRONT_CROP, k), pocket_disc(p['discface'], k)]


def jeans_serigraphie(p):
    main, light = p['main'], p['light']
    front = clipped('j2f', 'M166 250 H240 V456 H166 Z', '<path d="%s" fill="%s"></path>' % (dots(166, 254, 12, 23, 9, lambda r: 0.4 + 2.2 * (r / 22) ** 1.3), main))
    front += vcol('PALE SNAKE', 84, 150, 84, 330, 10, light, AN, '400')
    back = clipped('j2b', J_LPOCK, '<path d="%s" fill="%s"></path>' % (dots(80, 118, 8, 8, 9, lambda r: 2.2 - 0.2 * r), main))
    back += text(150, 42, '2 3 5 7 11 13 17 19', 7, light, AN, ls=1.6)
    return (jean(JF_UNDER + front, '', JF_TOP, 'Jean, devant : trame de points ivoire qui grossit vers l’ourlet sur la jambe droite, PALE SNAKE en lettres empilées sur la cuisse gauche.'),
            jean(JB_UNDER + back, back_pocket_disc(p['discface']), JB_TOP, 'Jean, dos : poche gauche tramée, nombres premiers sur la ceinture, un DISC tramé qui dépasse de la poche droite.'),
            'La trame de points descend la jambe droite et grossit vers l’ourlet, comme sur le panneau central du dos. PALE SNAKE s’empile sur la cuisse gauche. Derrière, la poche gauche est tramée, un DISC tramé dépasse de la droite.')


# ================================================================== 3 · Green Dolphin Street (bars behind the Stand)
def back_prison(p, k, pre):
    main, acc, light = p['main'], p['accent'], p['light']
    hl = BK if main == light else light
    s = text(260, 272, 'GREEN DOLPHIN STREET', 17, light, AN, ls=3) + text(260, 291, 'G.D.st 刑務所', 10, acc, JP, ls=2)
    for seam, ref in ((L, LSIDE), (R, RSIDE)):
        for gi in range(5):
            y = 372 + gi * 30
            s += tally((lerp_seam(seam, y) + lerp_seam(ref, y)) / 2, y, light, acc)
    for gi in range(4):
        s += tally(58, 420 + gi * 34, light, acc, h=8, w=1.4)
    s += text(262, 739, '教誨師 · No. 2357', 12, light, JP, ls=2)
    bars = []
    for i in range(8):
        x = 142 + i * 34
        bars.append('<rect x="%s" y="296" width="9" height="414" fill="%s" stroke="%s" stroke-width="1.2"></rect>' % (f(x - 4.5), main, BK))
        bars.append('<line x1="%s" y1="296" x2="%s" y2="710" stroke="%s" stroke-width="1.2"></line>' % (f(x - 2), f(x - 2), hl))
    for y in (420, 640):
        bars.append('<rect x="100" y="%d" width="330" height="10" fill="%s" stroke="%s" stroke-width="1.2"></rect>' % (y, main, BK))
        for i in range(8):
            bars.append('<circle cx="%s" cy="%d" r="2.2" fill="%s"></circle>' % (f(142 + i * 34), y + 5, acc))
    s += clipped(pre + 'door', PANEL, ''.join(bars))
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="9" stroke-linejoin="round"></path>' % (PANEL, main)
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="1.2" stroke-linejoin="round"></path>' % (PANEL, BK)
    lx = lerp_seam(R, 530) - 30
    s += '<rect x="%s" y="508" width="26" height="44" rx="3" fill="%s" stroke="%s" stroke-width="1.2"></rect>' % (f(lx), acc, BK)
    s += '<circle cx="%s" cy="524" r="4" fill="%s"></circle><path d="M%s 526 L%s 540 L%s 540 Z" fill="%s"></path>' % (f(lx + 13), BK, f(lx + 10.5), f(lx + 8), f(lx + 18), BK)
    return [layer(s, BACK_CROP, k), ws_center(p['ws'], k)]


def front_prison(p, k, pre):
    main, acc, light = p['main'], p['accent'], p['light']
    dark = main != light
    badge = ('<g transform="rotate(-3 418 535)"><rect x="392" y="512" width="54" height="40" rx="2.5" fill="%s"></rect><rect x="392" y="512" width="54" height="10" rx="2.5" fill="%s"></rect>' % (light, main) +
             text(419, 519.6, 'G.D.st 刑務所', 6.5, light if dark else BK, JP, ls=0.5) + cross(402, 535, 16, acc if dark else BK, 2.4) +
             text(425, 538, '教誨師', 11, BK, JP) + text(425, 547, 'No. 2357', 6.5, BK, AN, ls=0.6) + '</g>')
    bars = ''.join('<rect x="%s" y="436" width="4" height="60" fill="%s" stroke="%s" stroke-width="0.8"></rect>' % (f(x - 2), main, BK) for x in (96, 115, 153, 172))
    return [pocket_disc(p['discface'], k), layer(badge + clipped(pre + 'flap', F_FLAP_L, bars), FRONT_CROP, k)]


def jeans_prison(p):
    main, acc, light = p['main'], p['accent'], p['light']
    front = ''.join(tally(226, 150 + gi * 40, light, acc, h=8, w=1.3) for gi in range(7))
    front += vcol('教誨師', 96, 128, 96, 176, 12, light)
    over = clipped('j3o', 'M160 96 H226 V182 H160 Z', ''.join('<rect x="%s" y="96" width="3.4" height="90" fill="%s" stroke="%s" stroke-width="0.6"></rect>' % (f(x - 1.7), main, BK) for x in (176, 187, 198, 209)))
    back = text(150, 80, 'No. 2357', 11, light, AN, ls=2)
    return (jean(JF_UNDER + front, '', JF_TOP, 'Jean, devant : bâtons de prisonnier le long de la couture extérieure droite, 教誨師 sur la cuisse gauche.'),
            jean(JB_UNDER + back, back_pocket_disc(p['discface']), over + JB_TOP, 'Jean, dos : No. 2357 sur l’empiècement, un DISC derrière de petits barreaux sur la poche droite.'),
            'Les jours comptés descendent la couture extérieure droite. Derrière, la poche droite devient une petite cellule : quatre barreaux, et le DISC enfermé qui dépasse. No. 2357 sur l’empiècement, comme un numéro de matricule.')


# ================================================================== 4 · Color block
def back_colorblock(p, k, pre):
    main, light = p['main'], p['light']
    tcol = BK if main == light else light
    s = clipped(pre + 'blocks', LPANEL + ' ' + RPANEL + ' ' + YOKE + ' ' + CUFF_L + ' ' + CUFF_R, rect(main))
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="5 3.5"></path>' % (PANEL, light)
    s += text(260, 290, '天国へ行く方法', 24, tcol, MIN, ls=3, extra='font-weight="800"')
    s += vcol('らせん階段', 118, 600, 128, 690, 12, tcol) + vcol('秘密の皇帝', 412, 600, 402, 690, 12, tcol)
    layers = [layer(s, BACK_CROP, k), ws_center(p['ws'], k)]
    if main != light:
        layers.append(''.join(img(p['disc'], x, y, w, k, BY, r, alt='DISC') for x, y, w, r in ((118, 420, 40, 20), (126, 500, 44, -14), (414, 420, 40, -20), (406, 500, 44, 14))))
    return layers


def front_colorblock(p, k, pre):
    s = clipped(pre + 'ff', F_FLAP_L + ' ' + F_FLAP_R + ' ' + F_CUFF_L + ' ' + F_CUFF_R, rect(p['main']))
    s += ''.join('<circle cx="%d" cy="470" r="5.2" fill="#2D2D31" stroke="#4B4B51" stroke-width="0.9"></circle>' % x for x in (135, 419))
    return [layer(s, FRONT_CROP, k), pocket_disc(p['discface'], k)]


def jeans_colorblock(p):
    main, light = p['main'], p['light']
    tcol = BK if main == light else light
    front = clipped('j4f', J_HEMS + ' ' + J_COIN, rect(main))
    back = clipped('j4b', J_HEMS + ' ' + J_LPOCK + ' ' + J_RPOCK, rect(main))
    back += text(150, 80, '天国へ行く方法', 9, light, MIN, ls=1.5, extra='font-weight="800"')
    over = '<path d="%s" fill="none" stroke="#4D4D54" stroke-width="0.9" stroke-dasharray="3.2 2.4"></path>' % 'M85 121.94 L129 118.42 L127.24 167.7 L107 178.26 L86.76 167.7 Z M215 121.94 L171 118.42 L172.76 167.7 L193 178.26 L213.24 167.7 Z'
    return (jean(JF_UNDER + front, '', JF_TOP, 'Jean, devant : ourlets et poche à monnaie peints en bordeaux.'),
            jean(JB_UNDER + back, back_pocket_disc(p['discface']), over + JB_TOP, 'Jean, dos : les deux poches et les ourlets peints en bordeaux, 天国へ行く方法 sur l’empiècement, un DISC qui dépasse de la poche droite.'),
            'Le color block continue sur le jean : les deux poches arrière, les ourlets et la petite poche à monnaie prennent la couleur des rabats de la veste. Le reste du jean reste noir, comme le panneau central du dos.')


# ------------------------------------------------------------------ board
def chip(c, name):
    return ('<div style="display: flex; align-items: center; gap: 7px"><span style="width: 20px; height: 20px; border-radius: 6px; background: %s; border: 1px solid rgba(0, 0, 0, 0.2); display: inline-block"></span>'
            '<span style="font-size: 13px; color: #1A1A1A">%s <span style="color: #5F5B54">%s</span></span></div>') % (c, name, c)


def box(h, t, flex='1 1 0'):
    return ('<div style="flex: %s; box-sizing: border-box; padding: 16px 16px 18px; background: #F7F5F1; border-radius: 14px; border: 1px solid rgba(0, 0, 0, 0.08); display: flex; flex-direction: column; gap: 8px">'
            '<div style="font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: #5F5B54; font-weight: 500">%s</div>'
            '<div style="font-size: 13px; line-height: 1.5; color: #1A1A1A">%s</div></div>') % (flex, h, t)


def fig(inner, cap):
    return '<figure style="margin: 0; display: flex; flex-direction: column; align-items: center; gap: 6px">%s<figcaption style="font-size: 13px; letter-spacing: 0.14em; text-transform: uppercase; color: #5F5B54">%s</figcaption></figure>' % (inner, cap)


def board(fname, title, h1, sub, pkey, back_fn, front_fn, jeans_fn, front_label, back_label, idea, how, alt_keys):
    p = PAL[pkey]
    chips = ''.join(chip(c, n) for c, n in [('#1C1C1F', 'Noir'), ('#6F6F73', 'Gris sherpa')] + p['chips'])
    front = mock('photo-devant', FRONT_CROP, KF, front_fn(p, KF, 'f-'), front_label)
    back = mock('photo-dos', BACK_CROP, KB, back_fn(p, KB, 'm-'), back_label)
    jf, jb, jtext = jeans_fn(p)
    minis = ''
    for i, key in enumerate(alt_keys):
        q = PAL[key]
        minis += ('<figure style="margin: 0; display: flex; flex-direction: column; gap: 8px">%s'
                  '<figcaption style="display: flex; flex-direction: column; gap: 5px"><div style="font-size: 14px; font-weight: 500; color: #1A1A1A">%s</div>'
                  '<div style="display: flex; gap: 10px; flex-wrap: wrap">%s</div></figcaption></figure>') % (
            mock('photo-dos', BACK_CROP, KM, back_fn(q, KM, 'abc'[i] + '-'), 'Dos, palette %s' % q['name']), q['name'], ''.join(chip(c, n) for c, n in q['chips']))
    html = '''<!doctype html>
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
<div style="width: 1200px; height: 1940px; box-sizing: border-box; padding: 32px 48px 28px; background: #ECE9E3; display: flex; flex-direction: column; gap: 18px; font-family: 'Inter', sans-serif; color: #1A1A1A">
<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 24px">
<div style="display: flex; flex-direction: column; gap: 4px">
<h1 style="margin: 0; font-family: 'Anton', sans-serif; font-weight: 400; font-size: 34px; line-height: 1.05; letter-spacing: 0.02em; white-space: nowrap; color: #1A1A1A">%s</h1>
<p style="margin: 0; font-size: 15px; color: #5F5B54">%s</p>
</div>
<div style="display: flex; gap: 14px; align-items: center; flex-wrap: wrap; justify-content: flex-end; max-width: 440px">%s</div>
</div>
<div style="display: flex; gap: 24px; justify-content: center; align-items: flex-start">
<div style="width: 469px; display: flex; flex-direction: column; gap: 16px">
%s
<div style="display: flex; gap: 14px">%s%s</div>
</div>
%s
</div>
<div style="display: flex; gap: 24px; align-items: flex-start">
%s
%s
%s
</div>
<div style="display: flex; flex-direction: column; gap: 12px; margin-top: 6px">
<div style="font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: #5F5B54; font-weight: 500">Le même dos dans d’autres palettes</div>
<div style="display: flex; gap: 24px; justify-content: center; align-items: flex-start">%s</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1200,"height":1940}}'>
class Component extends DCLogic {
renderVals() {
return {};
}
}
</script>
</body>
</html>
''' % (title, h1, sub, chips, fig(front, 'Veste · devant'), box('L’idée · ce qui change', idea), box('Comment le faire', how), fig(back, 'Veste · dos'),
       fig(jf, 'Jean · devant'), fig(jb, 'Jean · dos'), box('Le jean', jtext), minis)
    open('%s/%s' % (OUT, fname), 'w', encoding='utf-8').write(html)


board('Veste2Couronne.dc.html', 'Ta veste – Couronne V2', 'Couronne · la bande rayée passe les épaules', 'V2 · lilas et gris · les rayures GΔCT passent les épaules',
      'lilas', back_couronne, front_couronne, jeans_couronne,
      'Devant : rayures GΔCT sous la couture de poitrine et sur les poignets, un DISC dans la poche gauche.',
      'Dos : bande rayée GΔCT lilas sur l’empiècement et le haut des manches ; Pale Snake grand, la couronne dans la bande, les bras sur les volets ; colonnes de lettres sur les volets ; GΔCT sur la ceinture.',
      'Pale Snake grand, la couronne qui traverse la couture de l’empiècement. Ce qui change : la bande rayée GΔCT ne s’arrête plus à l’empiècement, elle passe les épaules jusqu’aux manches, comme le bandeau d’un sukajan ; les mêmes rayures reviennent aux poignets et sous la couture de poitrine, devant. Le gris clair rappelle le col sherpa.',
      'Rayures : ruban de masquage fin tendu sur le dos et les manches, peinture lilas au pinceau plat entre les bandes, lettres au pochoir de lettres. Pale Snake au papier transfert pour textiles foncés, posé en dernier, par-dessus les rayures.',
      ['vo-a', 'vo-b', 'ivoire'])

board('Veste4Serigraphie.dc.html', 'Ta veste – Sérigraphie V2', 'Sérigraphie · les trames se répondent', 'V2 · ivoire seul · les trames des volets répondent au centre',
      'ivoire', back_serigraphie, front_serigraphie, jeans_serigraphie,
      'Devant : un DISC tramé dans la poche gauche, PALE SNAKE sur le rabat droit, trame de points sur les poignets.',
      'Dos : ホワイトスネイク sur l’empiècement ; trame de points ivoire qui grossit vers le bas dans le panneau central et qui s’affine vers le bas sur les volets ; Pale Snake en trame ivoire, grand, par-dessus les coutures ; deux DISC tramés de chaque côté ; nombres premiers sur la ceinture.',
      'Une seule couleur, comme un tee-shirt de groupe sérigraphié : l’ivoire, les demi-teintes en points. Ce qui change : la trame des volets répond à celle du panneau central (dense en haut sur les côtés, dense en bas au centre), si bien que les coutures dessinent un chevron. Pale Snake passe par-dessus, et la trame revient sur les poignets.',
      'Une seule peinture : ivoire opaque. Pale Snake et les DISC au papier transfert. Trame : rhodoïd percé à la perforatrice, points de plus en plus gros, tamponnés à l’éponge.',
      ['vo-a', 'vo-b', 'lilas'])

board('Veste5Prison.dc.html', 'Ta veste – Green Dolphin Street V2', 'Green Dolphin Street · Pale Snake devant la porte', 'V2 · violet, ivoire et orange · les barreaux derrière le Stand',
      'vo-a', back_prison, front_prison, jeans_prison,
      'Devant : le DISC de la poche gauche derrière de petits barreaux sur le rabat, badge d’aumônier sous la poche droite.',
      'Dos : GREEN DOLPHIN STREET sur l’empiècement ; porte de cellule violette dans le panneau central, cadre le long des coutures, barreaux à rivets orange et plaque de serrure ; Pale Snake devant la porte ; bâtons de prisonnier sur les volets et la manche gauche ; 教誨師 · No. 2357 sur la ceinture.',
      'Pucci est l’aumônier de la prison de Green Dolphin Street. Ce qui change : plus de vert, c’est violet, ivoire et orange ; les barreaux passent derrière Pale Snake, qui sort de la cellule au lieu d’y être enfermé ; les deux coutures du dos font le cadre de la porte, avec rivets et serrure orange ; les jours sont comptés sur les volets et la manche.',
      'Barreaux et cadre au ruban de masquage, peinture violette au pinceau plat, rivets et serrure au feutre peinture orange. Pale Snake au papier transfert, posé en dernier, par-dessus les barreaux. Bâtons au feutre peinture ivoire.',
      ['vo-b', 'lilas', 'ivoire'])

board('Veste6ColorBlock.dc.html', 'Ta veste – Color block V2', 'Color block · jusqu’au col et aux poignets', 'V2 · bordeaux et ivoire · jusqu’au col, aux poignets et aux rabats',
      'bordeaux', back_colorblock, front_colorblock, jeans_colorblock,
      'Devant : rabats de poche et poignets peints en bordeaux, un DISC dans la poche gauche.',
      'Dos : l’empiècement jusqu’au col, les deux volets et les poignets peints en bordeaux, bord à bord avec les coutures ; 天国へ行く方法 en ivoire sur l’empiècement ; le panneau central reste noir avec Pale Snake, cerné d’une surpiqûre ivoire ; DISC tramés sur les volets ; らせん階段 et 秘密の皇帝 en bas des volets.',
      'Chaque pièce de tissu prend une couleur unie, bord à bord avec les coutures, comme un vêtement assemblé en patchwork. Ce qui change : l’empiècement est peint jusqu’au col, et les poignets suivent, devant et derrière, comme les rabats de poche. Le panneau central reste noir et met Pale Snake en valeur.',
      'Peinture textile bordeaux au pinceau plat, coutures masquées au ruban, deux couches. Pale Snake et les DISC au papier transfert. Surpiqûre du panneau au feutre peinture ivoire.',
      ['vo-a', 'vo-b', 'ivoire'])
print('v2 ok')
