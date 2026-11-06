import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BK = (0x1C, 0x1C, 0x1F)
IV = (0xEF, 0xE8, 0xD8)
PAL = {
    'violet': (0x8B, 0x6C, 0xC6),
    'lilas': (0xA5, 0x8F, 0xCB),
    'ciel': (0x7F, 0xA6, 0xD6),
    'vert': (0x4F, 0x9B, 0x7F),
    'bordeaux': (0x9B, 0x3B, 0x52),
}
BAYER = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]], np.float32) / 16


def feats(img, blur=0.5):
    rgb = np.asarray(img.convert('RGB').filter(ImageFilter.GaussianBlur(blur)), np.float32) / 255
    L = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]
    mx, mn = rgb.max(-1), rgb.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    d = np.maximum(mx - mn, 1e-6)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    return L, sat, hue, mx - mn


def gold_mask(L, sat, hue):
    return (hue >= 22) & (hue <= 62) & (sat > 0.38) & (L > 0.3)


def three(img, main, t_dark=0.30, t_light=0.74, light=IV):
    L, sat, hue, _ = feats(img)
    out = np.zeros(L.shape + (3,), np.float32)
    out[:] = main
    out[L < t_dark] = BK
    out[L >= t_light] = light
    out[gold_mask(L, sat, hue)] = light
    a = np.asarray(img.split()[-1])
    return Image.fromarray(np.dstack([out.astype(np.uint8), a]), 'RGBA')


def halftone(img, t_dark=0.28, t_light=0.72, cell=2):
    """Ivory-only screen print : solid lights, black darks, ordered-dither dots for the mid tones."""
    L, sat, hue, _ = feats(img)
    h, w = L.shape
    yy, xx = np.mgrid[0:h, 0:w]
    th = BAYER[(yy // cell) % 4, (xx // cell) % 4]
    t = np.clip((L - t_dark) / (t_light - t_dark), 0, 1)
    on = (t > th) | gold_mask(L, sat, hue)
    out = np.where(on[..., None], np.array(IV, np.float32), np.array(BK, np.float32))
    a = np.asarray(img.split()[-1])
    return Image.fromarray(np.dstack([out.astype(np.uint8), a]), 'RGBA')


def contour(im, px, color=IV, pad_bottom=True):
    W, H = im.size
    c = Image.new('RGBA', (W + 2 * px, H + px + (px if pad_bottom else 0)), (0, 0, 0, 0))
    c.paste(im, (px, px), im)
    a = c.split()[-1].point(lambda v: 255 if v > 110 else 0)
    grown = a.filter(ImageFilter.MaxFilter(2 * px + 1)).filter(ImageFilter.GaussianBlur(0.6))
    base = Image.new('RGBA', c.size, color + (0,))
    base.putalpha(grown)
    base.alpha_composite(c)
    return base


def components(im, n=3):
    """Split a sheet of n side-by-side cut-outs ; return the crops left to right."""
    a = np.asarray(im.split()[-1]) > 20
    cols = a.any(0)
    xs = np.where(cols)[0]
    runs, start = [], xs[0]
    for i in range(1, len(xs)):
        if xs[i] - xs[i - 1] > 6:
            runs.append((start, xs[i - 1])); start = xs[i]
    runs.append((start, xs[-1]))
    runs = sorted(runs, key=lambda r: r[1] - r[0], reverse=True)[:n]
    runs.sort()
    out = []
    for x0, x1 in runs:
        sub = im.crop((x0, 0, x1 + 1, im.size[1]))
        out.append(sub.crop(sub.split()[-1].getbbox()))
    return out


def fit(im, maxw, maxh):
    im = im.copy(); im.thumbnail((maxw, maxh), Image.LANCZOS); return im


# ---------------------------------------------------------------- sources
ws = Image.open('ref_ws/ws_app.png').convert('RGBA').crop((0, 0, 744, 1100)).resize((560, 828), Image.LANCZOS)
ws_heads = components(Image.open('stands/Whitesnake_Anime_Headshots.png').convert('RGBA'))
cm_heads = components(Image.open('stands/C-MOON_Portrait_Render_Anime.png').convert('RGBA'))
def isolate(im, seed):
    m = im.split()[-1].point(lambda v: 255 if v > 20 else 0)
    ImageDraw.floodfill(m, seed, 128, thresh=0)
    keep = m.point(lambda v: 255 if v == 128 else 0)
    out = im.copy()
    out.putalpha(Image.fromarray(np.minimum(np.asarray(im.split()[-1]), np.asarray(keep)).astype(np.uint8)))
    return out.crop(out.split()[-1].getbbox())


mih_sheet = Image.open('stands/Made_in_Heaven_Portrait_Render_Anime.png').convert('RGBA')
mih_heads = [None, isolate(mih_sheet, (715, 450)), None]
mih_full = fit(Image.open('stands/Made_In_Heaven_Render_Appearance_Anime.png').convert('RGBA'), 420, 1000)
print('heads', [h.size for h in ws_heads], [h.size for h in cm_heads], mih_heads[1].size, 'mih', mih_full.size)

# DISC from the anime frame
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
chroma = big.max(-1) - big.min(-1)
Ls = 0.2126 * big[..., 0] + 0.7152 * big[..., 1] + 0.0722 * big[..., 2]
Lf = 0.2126 * fine[..., 0] + 0.7152 * fine[..., 1] + 0.0722 * fine[..., 2]
refl = (chroma > 0.075) | (Ls > 0.47)
dark = Lf < 0.24


def disc(main, rim, mono=False):
    h, w = Ls.shape
    if mono:
        yy, xx = np.mgrid[0:h, 0:w]
        body = (BAYER[(yy // 3) % 4, (xx // 3) % 4] < 0.45)
        out = np.where(body[..., None], np.array(IV, np.float32), np.array(BK, np.float32))
    else:
        out = np.zeros((h, w, 3), np.float32); out[:] = main
    out[refl] = IV
    out[dark] = BK
    im = Image.fromarray(out.astype(np.uint8), 'RGB').convert('RGBA'); im.putalpha(dmask(rim))
    im = im.crop(im.split()[-1].getbbox())
    if not rim:
        im = im.resize((im.size[0], round(im.size[1] * RX / RY)), Image.LANCZOS)
    im = im.resize((im.size[0] // 2, im.size[1] // 2), Image.LANCZOS)
    a = im.split()[-1]
    hard = a.point(lambda v: 255 if v > 128 else 0)
    edge = np.asarray(hard) & ~np.asarray(hard.filter(ImageFilter.MinFilter(5)))
    arr = np.array(im); arr[edge > 0, :3] = BK; arr[..., 3] = np.asarray(hard.filter(ImageFilter.GaussianBlur(0.7)))
    return Image.fromarray(arr, 'RGBA')


def save(im, name):
    im.save('assets/%s.png' % name, optimize=True)
    prev = Image.new('RGBA', im.size, BK + (255,)); prev.alpha_composite(im)
    prev.convert('RGB').save('assets/_prev_%s.png' % name)


for key, main in PAL.items():
    save(contour(three(ws, main), 9, pad_bottom=False), 'ws-%s' % key)
    save(disc(main, 18), 'disc-incline-%s' % key)
    save(disc(main, 0), 'disc-face-%s' % key)
save(contour(halftone(ws), 9, pad_bottom=False), 'ws-ivoire')
save(disc(None, 18, mono=True), 'disc-incline-ivoire')
save(disc(None, 0, mono=True), 'disc-face-ivoire')
# the three Stands, sky palette
ciel = PAL['ciel']
save(contour(three(fit(ws_heads[1], 320, 320), ciel), 6), 'head-ws-ciel')
save(contour(three(fit(cm_heads[1], 320, 320), ciel, t_dark=0.22, t_light=0.66), 6), 'head-cmoon-ciel')
save(contour(three(fit(mih_heads[1], 360, 320), ciel, t_dark=0.25, t_light=0.70), 6), 'head-mih-ciel')
save(contour(three(mih_full, ciel, t_dark=0.25, t_light=0.70), 8), 'mih-ciel')
import glob
print(sorted(p.split('/')[-1] for p in glob.glob('assets/[!_]*.png')))
