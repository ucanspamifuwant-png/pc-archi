"""Dedicated jeans boards for the four kept designs (drawn jean, 300x480 units, shown at KJ)."""
import json, sys
from lib import f, text, esc, BASE, AN, JP, MIN, IV, BK
from PIL import Image as _I

URLS = json.load(open(sys.argv[1]))
OUT = sys.argv[2]
ASSETS = sys.argv[3]
KJ = 1.35
W, H = 300 * KJ, 480 * KJ


def _ar(n):
    w, h = _I.open('%s/%s.png' % (ASSETS, n)).size
    return w / h


# ------------------------------------------------------------------ jean geometry (units)
def xo_l(y):  # left leg outer edge (viewer's left)
    return 68 + (60 - 68) * (y - 48) / 72 if y < 120 else 60 + (64 - 60) * (y - 120) / 340


def xo_r(y):
    return 300 - xo_l(y)


def xi_l(y):  # left leg inner edge
    return 150 + (128 - 150) * (y - 176) / 284


def xi_r(y):
    return 300 - xi_l(y)


def poly(pts, close=True):
    return 'M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts) + (' Z' if close else '')


def leg_l(y0, y1):
    return poly([(xo_l(y0), y0), (xi_l(max(y0, 176)), max(y0, 176)), (xi_l(y1), y1), (xo_l(y1), y1)])


def leg_r(y0, y1):
    return poly([(xo_r(y0), y0), (xi_r(max(y0, 176)), max(y0, 176)), (xi_r(y1), y1), (xo_r(y1), y1)])


def band_l(w, y0=52, y1=452, n=12):  # band along the left outer seam
    ys = [y0 + (y1 - y0) * i / n for i in range(n + 1)]
    return poly([(xo_l(y), y) for y in ys] + [(xo_l(y) + w, y) for y in ys[::-1]])


def band_r(w, y0=52, y1=452, n=12):
    ys = [y0 + (y1 - y0) * i / n for i in range(n + 1)]
    return poly([(xo_r(y), y) for y in ys] + [(xo_r(y) - w, y) for y in ys[::-1]])


J_HEMS = 'M60 408 H132 V452 H60 Z M168 408 H240 V452 H168 Z'
J_YOKE = 'M68 48 H231 L237 96 L150 116 L63 96 Z'
J_LPOCK = 'M82 118 L132 114 L130 170 L107 182 L84 170 Z'
J_RPOCK = 'M218 118 L168 114 L170 170 L193 182 L216 170 Z'
J_COIN = 'M198 62 H214 V78 H198 Z'
J_LOOPS_F = 'M81 26 H87 V50 H81 Z M115 26 H121 V50 H115 Z M173 26 H179 V50 H173 Z M207 26 H213 V50 H207 Z'
J_LOOPS_B = 'M81 26 H87 V50 H81 Z M115 26 H121 V50 H115 Z M147 26 H153 V50 H147 Z M179 26 H185 V50 H179 Z M213 26 H219 V50 H213 Z'
POCK_DASH = 'M85 121.94 L129 118.42 L127.24 167.7 L107 178.26 L86.76 167.7 Z M215 121.94 L171 118.42 L172.76 167.7 L193 178.26 L213.24 167.7 Z'
JF_UNDER, JF_TOP = ''.join(BASE['J_F_UNDER']), ''.join(BASE['J_F_TOP'])
JB_UNDER, JB_TOP = ''.join(BASE['J_B_UNDER']), ''.join(BASE['J_B_TOP'])


# ------------------------------------------------------------------ drawing helpers
def clipped(cid, d, inner):
    return '<defs><clipPath id="%s"><path d="%s"></path></clipPath></defs><g clip-path="url(#%s)">%s</g>' % (cid, d, cid, inner)


def rect(col):
    return '<rect x="0" y="0" width="300" height="480" fill="%s"></rect>' % col


def stripes(y0, y1, col, x0=40, x1=260, step=8, size=5, ls=1.8):
    o = []
    for i, y in enumerate(range(y0, y1, step)):
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.7"></line>' % (x0, y, x1, y, col))
        if i % 2 == 0:
            o.append(text(x0 + (i * 5) % 14, y + size * 1.15, 'G Δ C T ' * 14, size, col, AN, anchor='start', ls=ls))
    return ''.join(o)


def dots(x0, y0, cols, rows, step, r_of_row):
    o = []
    for row in range(rows):
        y = y0 + row * step
        rr = r_of_row(row)
        for col in range(cols):
            x = x0 + col * (step - 1) + ((step - 1) / 2 if row % 2 else 0)
            o.append('M%s %sa%s %s 0 1 0 0.01 0Z' % (f(x - rr), f(y), f(rr), f(rr)))
    return '<path d="%s"></path>' % ''.join(o)


def vcol(chars, x0, y0, x1, y1, size, col, fam=MIN, weight='800'):
    o = []
    n = len(chars)
    for i, ch in enumerate(chars):
        t = i / max(1, n - 1)
        o.append('<text x="%s" y="%s" font-family="%s" font-weight="%s" font-size="%s" fill="%s" text-anchor="middle" dominant-baseline="central">%s</text>' % (
            f(x0 + (x1 - x0) * t), f(y0 + (y1 - y0) * t), fam, weight, size, col, ch))
    return ''.join(o)


def tally(x, y, light, acc, h=8, w=1.3):
    o = ''.join('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="round"></line>' % (
        f(x - 6 + kk * 4), f(y - h), f(x - 6 + kk * 4), f(y + h), light, f(w)) for kk in range(4))
    return o + '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="round"></line>' % (f(x - 9), f(y + h * 0.66), f(x + 9), f(y - h * 0.66), acc, f(w))


def bars(xs, y0, y1, col, w=3.4):
    return ''.join('<rect x="%s" y="%d" width="%s" height="%d" fill="%s" stroke="%s" stroke-width="0.6"></rect>' % (f(x - w / 2), y0, f(w), y1 - y0, col, BK) for x in xs)


# ------------------------------------------------------------------ html helpers
def jsvg(inner):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="%.0f" height="%.0f" viewBox="0 0 300 480" style="position: absolute; left: 0px; top: 0px" aria-hidden="true">%s</svg>' % (W, H, inner)


def jean(under, imgs, over, label):
    return '<div role="img" aria-label="%s" style="position: relative; width: %.0fpx; height: %.0fpx">%s%s%s</div>' % (esc(label), W, H, jsvg(under), imgs, jsvg(over))


def jimg(name, cx, cy, w, rot=0, extra='', alt='DISC'):
    Wi = w * KJ
    Hi = Wi / _ar(name)
    return ('<img src="%s" alt="%s" style="position: absolute; left: %.1fpx; top: %.1fpx; width: %.1fpx; height: %.1fpx; transform: rotate(%sdeg)%s">'
            % (URLS[name], alt, cx * KJ - Wi / 2, cy * KJ - Hi / 2, Wi, Hi, rot, extra))


def jimg_top(name, cx, top, h, alt=''):
    Hi = h * KJ
    Wi = Hi * _ar(name)
    return ('<img src="%s" alt="%s" style="position: absolute; left: %.1fpx; top: %.1fpx; width: %.1fpx; height: %.1fpx">'
            % (URLS[name], alt, cx * KJ - Wi / 2, top * KJ, Wi, Hi))


def pocket_disc(name):
    return jimg(name, 193, 110, 36, 0, '; clip-path: inset(0 0 42% 0)', 'DISC glissé dans la poche arrière')


GREY = '#A9A9B0'
PAL = {
    'lilas': dict(main='#A58FCB', accent=GREY, light=IV, ws='ws-lilas', discface='disc-face-lilas', chips=[(IV, 'Ivoire'), ('#A58FCB', 'Lilas'), (GREY, 'Gris clair')]),
    'ivoire': dict(main=IV, accent=IV, light=IV, ws='ws-ivoire', discface='disc-face-ivoire', chips=[(IV, 'Ivoire')]),
    'vo-a': dict(main='#7B5CC4', accent='#F08D3E', light=IV, ws='ws-vo-a', discface='disc-face-vo-a', chips=[(IV, 'Ivoire'), ('#7B5CC4', 'Violet'), ('#F08D3E', 'Orange')]),
    'bordeaux': dict(main='#9B3B52', accent='#9B3B52', light=IV, ws='ws-bordeaux', discface='disc-face-bordeaux', chips=[(IV, 'Ivoire'), ('#9B3B52', 'Bordeaux')]),
}


# ================================================================== 1 · Couronne
def couronne(p):
    main, acc, light = p['main'], p['accent'], p['light']
    hem = stripes(404, 456, main)
    galon = clipped('c-gl', band_l(16), stripes(44, 460, main, x0=40, x1=100, step=8, size=5))
    front = galon + clipped('c-hf', J_HEMS, hem)
    front += clipped('c-coin', J_COIN, rect(main)) + clipped('c-lf', J_LOOPS_F, rect(acc))
    for j, ch in enumerate('GΔCTGΔCTGΔCTGΔCTGΔ'):
        front += text(xo_l(78 + j * 20) + 8, 78 + j * 20, ch, 7, light if j % 2 else BK, AN, extra='dominant-baseline="central"')
    back = clipped('c-gr', band_r(16), stripes(44, 460, main, x0=200, x1=260, step=8, size=5))
    back += clipped('c-yb', J_YOKE + ' ' + J_HEMS + ' ' + J_LPOCK, stripes(44, 460, main))
    back += clipped('c-lb', J_LOOPS_B, rect(acc))
    for j, ch in enumerate('GΔCTGΔCTGΔCTGΔCTGΔ'):
        back += text(xo_r(78 + j * 20) - 8, 78 + j * 20, ch, 7, light if j % 2 else BK, AN, extra='dominant-baseline="central"')
    return (jean(JF_UNDER + front, '', JF_TOP, 'Jean, devant : galon rayé GΔCT le long de la couture extérieure droite, rayures aux ourlets, poche à monnaie lilas, passants gris.'),
            jean(JB_UNDER + back, pocket_disc(p['discface']), '<path d="%s" fill="none" stroke="#4D4D54" stroke-width="0.9" stroke-dasharray="3.2 2.4"></path>' % POCK_DASH + JB_TOP,
                 'Jean, dos : le galon continue sur la même jambe, empiècement, poche gauche et ourlets rayés, un DISC qui dépasse de la poche droite.'),
            'Le galon : une bande rayée GΔCT qui descend toute la couture extérieure de la jambe droite, devant et derrière, comme le galon d’un pantalon de smoking, avec une lettre sur deux posée dessus. L’empiècement arrière et la poche gauche sont rayés comme l’empiècement de la veste, et les ourlets comme ses poignets. Les passants passent en gris, comme le col sherpa.',
            'Galon et rayures au ruban de masquage et à la peinture textile lilas, pinceau plat. Lettres au pochoir de lettres (feutre peinture ivoire et noir). Poche à monnaie et passants au pinceau. Le DISC au papier transfert, glissé sous le bord de la poche avant de le fixer au fer.')


# ================================================================== 2 · Sérigraphie
def serigraphie(p):
    main, light = p['main'], p['light']
    front = clipped('s-leg', leg_r(236, 452), '<g fill="%s">%s</g>' % (main, dots(150, 240, 14, 24, 9, lambda r: 0.4 + 2.4 * (r / 23) ** 1.3)))
    front += vcol('PALE SNAKE', 96, 236, 96, 400, 11, light, AN, '400')
    front += clipped('s-coin', J_COIN, '<g fill="%s">%s</g>' % (main, dots(196, 62, 3, 3, 7, lambda r: 1.6)))
    back = clipped('s-lp', J_LPOCK, '<g fill="%s">%s</g>' % (main, dots(80, 118, 8, 8, 9, lambda r: 2.2 - 0.2 * r)))
    back += text(150, 42, '2 3 5 7 11 13 17 19 23', 7, light, AN, ls=1.6)
    back += clipped('s-calf', leg_l(300, 452), '<g fill="%s">%s</g>' % (main, dots(56, 304, 12, 17, 9, lambda r: 0.3 + 1.6 * (r / 16))))
    imgs_f = jimg(p['discface'], 100, 150, 58, -12, '', 'DISC tramé sur la cuisse gauche')
    imgs_b = pocket_disc(p['discface']) + jimg_top(p['ws'], 204, 318, 96, 'Pale Snake en trame ivoire, sur le mollet droit')
    return (jean(JF_UNDER + front, imgs_f, JF_TOP, 'Jean, devant : grand DISC tramé sur la cuisse gauche, PALE SNAKE empilé dessous, trame de points qui grossit vers l’ourlet sur la jambe droite.'),
            jean(JB_UNDER + back, imgs_b, '<path d="%s" fill="none" stroke="#4D4D54" stroke-width="0.9" stroke-dasharray="3.2 2.4"></path>' % POCK_DASH + JB_TOP,
                 'Jean, dos : poche gauche tramée, DISC tramé qui dépasse de la poche droite, nombres premiers sur la ceinture, Pale Snake en trame sur le mollet droit, trame sur le mollet gauche.'),
            'Tout en ivoire, en points. Devant, le grand DISC tramé fait office de pièce de genou sur la cuisse gauche, PALE SNAKE s’empile dessous ; la trame monte de l’ourlet droit comme sur le panneau central de la veste. Derrière, Pale Snake lui-même, en trame, sur le mollet droit, là où un vrai jean customisé porte son image.',
            'Une seule peinture, ivoire opaque. DISC et Pale Snake au papier transfert pour textiles foncés. Trames au rhodoïd percé à la perforatrice, points de plus en plus gros, tamponnés à l’éponge. Lettres au pochoir.')


# ================================================================== 3 · Green Dolphin Street
def prison(p):
    main, acc, light = p['main'], p['accent'], p['light']
    front = ''.join(tally(xo_r(y) - 12, y, light, acc) for y in range(130, 440, 40))
    front += vcol('教誨師', 100, 128, 100, 180, 13, light)
    front += clipped('p-coin', J_COIN, bars((201, 206, 211), 60, 80, main, 2.2))
    front += text(150, 62, 'No. 2357', 7, acc, AN, ls=1.2)
    back = text(150, 82, 'No. 2357', 12, light, AN, ls=2) + text(150, 68, 'GREEN DOLPHIN STREET', 6, acc, AN, ls=1.2)
    back += ''.join(tally(xo_l(y) + 12, y, light, acc) for y in range(200, 440, 40))
    back += ''.join(tally(107, y, light, acc, h=6, w=1.1) for y in (132, 150, 168))
    over = '<path d="%s" fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round"></path>' % (J_RPOCK, main)
    over += clipped('p-cell', 'M160 92 H226 V184 H160 Z', bars((176, 187, 198, 209), 92, 186, main))
    over += '<rect x="214" y="142" width="7" height="12" rx="1" fill="%s" stroke="%s" stroke-width="0.6"></rect>' % (acc, BK)
    return (jean(JF_UNDER + front, '', JF_TOP, 'Jean, devant : bâtons de prisonnier le long de la couture extérieure droite, 教誨師 sur la cuisse gauche, petits barreaux sur la poche à monnaie, No. 2357 sur la ceinture.'),
            jean(JB_UNDER + back, pocket_disc(p['discface']), over + JB_TOP,
                 'Jean, dos : No. 2357 sur l’empiècement, poche droite en cellule avec barreaux violets, serrure orange et le DISC enfermé, bâtons sur la poche gauche et le long de la jambe gauche.'),
            'Le jean compte les jours : des bâtons de prisonnier descendent la couture extérieure devant, et l’autre jambe derrière, comme gravés sur un mur de cellule. La poche arrière droite devient la cellule : cadre violet, barreaux, serrure orange, et le DISC enfermé qui dépasse. La poche à monnaie a ses propres barreaux. No. 2357, le matricule, sur l’empiècement et la ceinture.',
            'Bâtons au feutre peinture ivoire, barre orange en travers. Cadre et barreaux de la poche au ruban de masquage et peinture violette, serrure au feutre orange. Le DISC au papier transfert, posé avant les barreaux.')


# ================================================================== 4 · Color block
def colorblock(p):
    main, light = p['main'], p['light']
    front = clipped('b-f', J_HEMS + ' ' + J_COIN + ' ' + J_LOOPS_F, rect(main))
    front += '<path d="M72 52 Q96 60 106 102" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"></path><path d="M228 52 Q204 60 194 102" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"></path>' % (main, main)
    back = clipped('b-b', J_YOKE + ' ' + J_HEMS + ' ' + J_LPOCK + ' ' + J_RPOCK + ' ' + J_LOOPS_B, rect(main))
    back += '<path d="M66 98 L150 118 L234 98" fill="none" stroke="%s" stroke-width="1" stroke-dasharray="3 2.2"></path>' % light
    back += text(150, 80, '天国へ行く方法', 11, light, MIN, ls=2, extra='font-weight="800"')
    over = '<path d="%s" fill="none" stroke="%s" stroke-width="0.9" stroke-dasharray="3.2 2.4"></path>' % (POCK_DASH, light)
    return (jean(JF_UNDER + front, '', JF_TOP, 'Jean, devant : ourlets, poche à monnaie et passants peints en bordeaux, bord des poches souligné de bordeaux.'),
            jean(JB_UNDER + back, pocket_disc(p['discface']), over + JB_TOP,
                 'Jean, dos : empiècement, les deux poches, ourlets et passants en bordeaux, 天国へ行く方法 en ivoire sur l’empiècement, surpiqûre ivoire, un DISC qui dépasse de la poche droite.'),
            'Le color block suit les pièces du jean comme celles de la veste : l’empiècement arrière (le pendant de celui de la veste), les deux poches, les ourlets (les poignets), la poche à monnaie et les passants prennent le bordeaux. Le bord des poches avant est juste souligné. Tout le reste reste noir, et 天国へ行く方法 revient sur l’empiècement.',
            'Peinture textile bordeaux au pinceau plat, coutures masquées au ruban, deux couches ; passants et bords de poche au pinceau fin. Surpiqûres au feutre peinture ivoire. Le DISC au papier transfert.')


# ------------------------------------------------------------------ board
def chip(c, name):
    return ('<div style="display: flex; align-items: center; gap: 7px"><span style="width: 20px; height: 20px; border-radius: 6px; background: %s; border: 1px solid rgba(0, 0, 0, 0.2); display: inline-block"></span>'
            '<span style="font-size: 13px; color: #1A1A1A">%s <span style="color: #5F5B54">%s</span></span></div>') % (c, name, c)


def box(h, t):
    return ('<div style="box-sizing: border-box; padding: 16px 16px 18px; background: #F7F5F1; border-radius: 14px; border: 1px solid rgba(0, 0, 0, 0.08); display: flex; flex-direction: column; gap: 8px">'
            '<div style="font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: #5F5B54; font-weight: 500">%s</div>'
            '<div style="font-size: 13px; line-height: 1.5; color: #1A1A1A">%s</div></div>') % (h, t)


def fig(inner, cap):
    return '<figure style="margin: 0; display: flex; flex-direction: column; align-items: center; gap: 6px">%s<figcaption style="font-size: 13px; letter-spacing: 0.14em; text-transform: uppercase; color: #5F5B54">%s</figcaption></figure>' % (inner, cap)


def board(fname, title, h1, sub, pkey, fn):
    p = PAL[pkey]
    jf, jb, idea, how = fn(p)
    chips = ''.join(chip(c, n) for c, n in [('#1C1C1F', 'Noir'), ('#1C1C1F', 'ton jean')][:1] + p['chips'])
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
<div style="width: 1200px; height: 880px; box-sizing: border-box; padding: 32px 48px 28px; background: #ECE9E3; display: flex; flex-direction: column; gap: 18px; font-family: 'Inter', sans-serif; color: #1A1A1A">
<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 24px">
<div style="display: flex; flex-direction: column; gap: 4px">
<h1 style="margin: 0; font-family: 'Anton', sans-serif; font-weight: 400; font-size: 34px; line-height: 1.05; letter-spacing: 0.02em; white-space: nowrap; color: #1A1A1A">%s</h1>
<p style="margin: 0; font-size: 15px; color: #5F5B54">%s</p>
</div>
<div style="display: flex; gap: 14px; align-items: center; flex-wrap: wrap; justify-content: flex-end; max-width: 440px">%s</div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start">
%s
%s
<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 14px">%s%s</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1200,"height":880}}'>
class Component extends DCLogic {
renderVals() {
return {};
}
}
</script>
</body>
</html>
''' % (title, h1, sub, chips, fig(jf, 'Jean · devant'), fig(jb, 'Jean · dos'), box('L’idée', idea), box('Comment le faire', how))
    open('%s/%s' % (OUT, fname), 'w', encoding='utf-8').write(html)


board('Jean2Couronne.dc.html', 'Ton jean – Couronne', 'Le jean · Couronne', 'Galon rayé GΔCT sur la couture extérieure, empiècement et ourlets rayés', 'lilas', couronne)
board('Jean4Serigraphie.dc.html', 'Ton jean – Sérigraphie', 'Le jean · Sérigraphie', 'Ivoire seul : DISC tramé sur la cuisse, Pale Snake en trame sur le mollet', 'ivoire', serigraphie)
board('Jean5Prison.dc.html', 'Ton jean – Green Dolphin Street', 'Le jean · Green Dolphin Street', 'Les jours comptés le long des coutures, la poche arrière en cellule', 'vo-a', prison)
board('Jean6ColorBlock.dc.html', 'Ton jean – Color block', 'Le jean · Color block', 'Empiècement, poches, ourlets et poche à monnaie en bordeaux', 'bordeaux', colorblock)
print('jeans ok')
