"""Violet / orange palette assets : Whitesnake and DISCs, studs and reflections remapped (no gold)."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BK = (0x1C, 0x1C, 0x1F)
IV = (0xEF, 0xE8, 0xD8)


def hx(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


PALS = {
    # name : (violet (mid tones), light tones, accent for the studs / spikes)
    'vo-a': (hx('#7B5CC4'), IV, hx('#F08D3E')),          # crépuscule : violet, ivoire, orange
    'vo-b': (hx('#9466E8'), hx('#FF8A3D'), hx('#FF8A3D')),  # néon : violet vif, orange vif, pas d'ivoire
    'vo-c': (hx('#6E5A9E'), IV, hx('#D9733F')),          # sanguine : violet sourd, ivoire, terre cuite
}


def feats(img, blur=0.5):
    rgb = np.asarray(img.convert('RGB').filter(ImageFilter.GaussianBlur(blur)), np.float32) / 255
    L = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]
    mx, mn = rgb.max(-1), rgb.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    d = np.maximum(mx - mn, 1e-6)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    return L, sat, hue


def three(img, main, light, accent, t_dark=0.30, t_light=0.74):
    L, sat, hue = feats(img)
    out = np.zeros(L.shape + (3,), np.float32); out[:] = main
    out[L < t_dark] = BK
    out[L >= t_light] = light
    out[(hue >= 22) & (hue <= 62) & (sat > 0.38) & (L > 0.3)] = accent
    a = np.asarray(img.split()[-1])
    return Image.fromarray(np.dstack([out.astype(np.uint8), a]), 'RGBA')


def contour(im, px, color):
    W, H = im.size
    c = Image.new('RGBA', (W + 2 * px, H + px), (0, 0, 0, 0)); c.paste(im, (px, px), im)
    a = c.split()[-1].point(lambda v: 255 if v > 110 else 0)
    grown = a.filter(ImageFilter.MaxFilter(2 * px + 1)).filter(ImageFilter.GaussianBlur(0.6))
    base = Image.new('RGBA', c.size, color + (0,)); base.putalpha(grown); base.alpha_composite(c)
    return base


src = Image.open('disc/dl_LimpBizkitStandDISCAnime.png').convert('RGBA')
W, H = src.size
CX, CY, RX, RY = 469, 299, 406, 217


def dmask(rim):
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    d.ellipse([CX - RX, CY - RY, CX + RX, CY + RY], fill=255)
    if rim: d.ellipse([CX - RX, CY - RY + rim, CX + RX, CY + RY + rim], fill=255)
    d.ellipse([469 - 64, 287 - 34, 469 + 64, 287 + 34], fill=0)
    return m.filter(ImageFilter.GaussianBlur(1.2))


big = np.asarray(src.convert('RGB').filter(ImageFilter.GaussianBlur(2.2)), np.float32) / 255
fine = np.asarray(src.convert('RGB').filter(ImageFilter.GaussianBlur(0.6)), np.float32) / 255
refl = ((big.max(-1) - big.min(-1)) > 0.075) | ((0.2126 * big[..., 0] + 0.7152 * big[..., 1] + 0.0722 * big[..., 2]) > 0.47)
dark = (0.2126 * fine[..., 0] + 0.7152 * fine[..., 1] + 0.0722 * fine[..., 2]) < 0.24


def disc(main, light, rim):
    out = np.zeros(refl.shape + (3,), np.float32); out[:] = main
    out[refl] = light; out[dark] = BK
    im = Image.fromarray(out.astype(np.uint8), 'RGB').convert('RGBA'); im.putalpha(dmask(rim))
    im = im.crop(im.split()[-1].getbbox())
    if not rim:
        im = im.resize((im.size[0], round(im.size[1] * RX / RY)), Image.LANCZOS)
    im = im.resize((im.size[0] // 2, im.size[1] // 2), Image.LANCZOS)
    hard = im.split()[-1].point(lambda v: 255 if v > 128 else 0)
    edge = np.asarray(hard) & ~np.asarray(hard.filter(ImageFilter.MinFilter(5)))
    arr = np.array(im); arr[edge > 0, :3] = BK; arr[..., 3] = np.asarray(hard.filter(ImageFilter.GaussianBlur(0.7)))
    return Image.fromarray(arr, 'RGBA')


def save(im, name):
    im.save('assets/%s.png' % name, optimize=True)
    p = Image.new('RGBA', im.size, BK + (255,)); p.alpha_composite(im); p.convert('RGB').save('assets/_prev_%s.png' % name)


ws = Image.open('ref_ws/ws_app.png').convert('RGBA').crop((0, 0, 744, 1100)).resize((560, 828), Image.LANCZOS)
for key, (main, light, acc) in PALS.items():
    save(contour(three(ws, main, light, acc), 9, light), 'ws-%s' % key)
    save(disc(main, light, 18), 'disc-incline-%s' % key)
    save(disc(main, light, 0), 'disc-face-%s' % key)
print('ok')
