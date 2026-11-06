# Customisation JoJo's : veste trucker noire et jean (Pucci · Pale Snake)

Kit de travail de la session cloud, pour continuer en local.

- Le canvas (toutes les planches) : https://claude.ai/artifact/Wkd57Dw57DFicBGKxKxc4u
- `boards/` : les planches publiées (fichiers `.dc.html` du canvas, page « Ta veste · essais »).
- `scripts/` : les générateurs. `veste_v2.py` fait les 4 planches veste (V2), `jeans_boards.py` les 4 planches jean,
  `prep_assets.py` et `vo_assets.py` recolorent les images officielles aux palettes (fichiers dans `assets/`).
  `lib.py` et `base.json` : le dessin du jean et les aides communes.
- `assets/` : Pale Snake et les DISC de l'anime, ramenés aux couleurs de chaque palette, prêts pour le papier transfert.
- `photos/` : les photos de la veste (devant, dos), recadrées, sur lesquelles les motifs sont posés.
- `sources/` : les deux images d'origine (jojowiki.com) dont partent les recolorations.

## Régénérer les planches

```
cd scripts
python3 veste_v2.py urls_blob.json ../boards ../assets
python3 jeans_boards.py urls_blob.json ../boards ../assets
```

`urls_blob.json` relie chaque image à son adresse sur le canvas (`/_blob/…`). Pour un aperçu local,
remplace ces adresses par des chemins `file://` vers `assets/` et `photos/`, puis `node preview.js planche.html sortie.png`
(Playwright + Chromium).

## Règles retenues

- Les Stands ne sont jamais redessinés : images officielles, seulement recolorées.
- Pas d'or ; les palettes sont lilas/gris, ivoire seul, violet/ivoire/orange, bordeaux/ivoire.
- Les motifs suivent les coutures de la veste (empiècement, panneau central, volets, ceinture, poignets) et du jean
  (empiècement, poches, couture extérieure, poche à monnaie, ourlets).
- Réalisation : papier transfert pour textiles foncés, pochoirs vinyle ou rhodoïd, peinture textile, feutres peinture.
