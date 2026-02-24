// Products data for comparison tables and product cards
export const products = {
  laptops: [
    {
      id: 'asus-proart-studiobook',
      name: 'ASUS ProArt Studiobook 16 OLED',
      brand: 'ASUS',
      price: 2499,
      rating: 4.8,
      badge: 'MEILLEUR CHOIX',
      image: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400',
      amazonUrl: 'https://www.amazon.fr/ASUS-ProArt-StudioBook-OLED-RTX3000/dp/B0CFK4273P?pd_rd_w=4sEf4&content-id=amzn1.sym.e1744f29-8ae7-49f6-9859-46cbe9e6a02e%3Aamzn1.symc.30e3dbb4-8dd8-4bad-b7a1-a45bcdbc49b8&pf_rd_p=e1744f29-8ae7-49f6-9859-46cbe9e6a02e&pf_rd_r=MQYJFX0JVNRJWP9YNF13&pd_rd_wg=N3zVP&pd_rd_r=25ee566b-f043-45ec-aff0-fcc26444c402&pd_rd_i=B0CFK4273P&linkCode=ll2&tag=pcarchi21-21&linkId=7a7ae14b84c1038a224efe1c73cefcf4&ref_=as_li_ss_tl',
      specs: {
        cpu: 'Intel Core i9-13980HX',
        ram: '32 Go DDR5',
        gpu: 'NVIDIA RTX 4070',
        storage: '1 To SSD NVMe',
        screen: '16" OLED 3.2K',
        battery: '90 Wh'
      },
      pros: [
        'Écran OLED exceptionnel pour le rendu',
        'Performances de pointe',
        'Construction professionnelle',
        'Bonne autonomie'
      ],
      cons: [
        'Prix élevé',
        'Poids conséquent (2.4 kg)'
      ],
      idealFor: 'Revit, ArchiCAD, Rhino, rendu 3D'
    },
    {
      id: 'macbook-pro-m4',
      name: 'MacBook Pro 14,2" M4 Max',
      brand: 'Apple',
      price: 2299,
      rating: 4.9,
      badge: 'PREMIUM',
      image: 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400',
      amazonUrl: '#affiliate-macbook-m4',
      specs: {
        cpu: 'Apple M4 Max',
        ram: '24 Go unifiée',
        gpu: 'GPU 16 cœurs',
        storage: '512 To SSD',
        screen: '14.2" Liquid Retina XDR',
        battery: '22h autonomie'
      },
      pros: [
        'Performances exceptionnelles',
        'Autonomie record',
        'Écran sublime',
        'Silence de fonctionnement'
      ],
      cons: [
        'Prix très élevé',
        'Compatibilité logiciels Windows'
      ],
      idealFor: 'SketchUp, Vectorworks, Archicad (Mac)'
    },
    {
      id: 'lenovo-thinkpad-p16',
      name: 'Lenovo ThinkPad P16',
      brand: 'Lenovo',
      price: 2199,
      rating: 4.6,
      badge: 'MEILLEUR RAPPORT QUALITÉ/PRIX',
      image: 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=400',
      amazonUrl: '#affiliate-lenovo-p16',
      specs: {
        cpu: 'Intel Core i7-13850HX',
        ram: '32 Go DDR5',
        gpu: 'NVIDIA RTX A2000',
        storage: '512 Go SSD',
        screen: '16" IPS WQXGA',
        battery: '94 Wh'
      },
      pros: [
        'Certifié ISV pour logiciels pro',
        'Excellent clavier',
        'Fiabilité ThinkPad',
        'Extensible'
      ],
      cons: [
        'Design austère',
        'GPU moins puissant que RTX 4000'
      ],
      idealFor: 'Revit, AutoCAD, BIM'
    },
    {
      id: 'dell-precision-5680',
      name: 'Dell Precision 5680',
      brand: 'Dell',
      price: 2899,
      rating: 4.7,
      badge: null,
      image: 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400',
      amazonUrl: '#affiliate-dell-5680',
      specs: {
        cpu: 'Intel Core i7-13700H',
        ram: '32 Go DDR5',
        gpu: 'NVIDIA RTX 3500 Ada',
        storage: '512 Go SSD',
        screen: '16" OLED 3.5K',
        battery: '86 Wh'
      },
      pros: [
        'Design fin et léger',
        'Écran OLED magnifique',
        'GPU professionnel certifié',
        'Support Dell excellent'
      ],
      cons: [
        'Prix premium',
        'Ports limités'
      ],
      idealFor: 'Revit, 3ds Max, rendu'
    },
    {
      id: 'hp-zbook-fury-g10',
      name: 'HP ZBook Fury 16 G10',
      brand: 'HP',
      price: 2599,
      rating: 4.5,
      badge: null,
      image: 'https://images.unsplash.com/photo-1547082299-de196ea013d6?w=400',
      amazonUrl: '#affiliate-hp-zbook',
      specs: {
        cpu: 'Intel Core i7-13850HX',
        ram: '32 Go DDR5',
        gpu: 'NVIDIA RTX 4000 Ada',
        storage: '512 Go SSD',
        screen: '16" DreamColor 4K',
        battery: '95 Wh'
      },
      pros: [
        'Écran DreamColor calibré',
        'GPU très puissant',
        'Robuste et fiable',
        'Nombreux ports'
      ],
      cons: [
        'Lourd (2.8 kg)',
        'Ventilation audible'
      ],
      idealFor: 'Rendu 3D intensif, V-Ray, Lumion'
    }
  ],
  tablets: [
    {
      id: 'wacom-intuos-pro',
      name: 'Wacom Intuos Pro M',
      brand: 'Wacom',
      price: 379,
      rating: 4.8,
      badge: 'MEILLEUR CHOIX',
      image: 'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=400',
      amazonUrl: '#affiliate-wacom-intuos',
      specs: {
        surface: '224 x 148 mm',
        resolution: '5080 lpi',
        pressure: '8192 niveaux',
        connection: 'USB-C / Bluetooth',
        compatibility: 'Windows, Mac'
      },
      pros: [
        'Précision professionnelle',
        'Durabilité exceptionnelle',
        'Express Keys personnalisables',
        'Multi-touch'
      ],
      cons: [
        'Prix élevé',
        'Pas d\'écran intégré'
      ],
      idealFor: 'Esquisse, retouche, présentation'
    },
    {
      id: 'xp-pen-deco-pro',
      name: 'XP-Pen Deco Pro MW',
      brand: 'XP-Pen',
      price: 129,
      rating: 4.5,
      badge: 'MEILLEUR BUDGET',
      image: 'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=400',
      amazonUrl: '#affiliate-xppen-deco',
      specs: {
        surface: '228 x 152 mm',
        resolution: '5080 lpi',
        pressure: '8192 niveaux',
        connection: 'USB-C / Bluetooth',
        compatibility: 'Windows, Mac, Android'
      },
      pros: [
        'Excellent rapport qualité/prix',
        'Sans fil Bluetooth',
        'Compatible Android',
        'Design moderne'
      ],
      cons: [
        'Drivers parfois capricieux',
        'Touch moins précis que Wacom'
      ],
      idealFor: 'Esquisse, dessin technique'
    },
    {
      id: 'huion-kamvas-22',
      name: 'Huion Kamvas 22 Plus',
      brand: 'Huion',
      price: 449,
      rating: 4.6,
      badge: 'AVEC ÉCRAN',
      image: 'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=400',
      amazonUrl: '#affiliate-huion-kamvas',
      specs: {
        surface: '21.5" IPS',
        resolution: '1920 x 1080',
        pressure: '8192 niveaux',
        connection: 'USB-C',
        compatibility: 'Windows, Mac'
      },
      pros: [
        'Grand écran pour dessiner',
        'Couleurs fidèles (140% sRGB)',
        'Prix compétitif pour la taille',
        'Antireflet mat'
      ],
      cons: [
        'Résolution Full HD seulement',
        'Encombrant sur le bureau'
      ],
      idealFor: 'Dessin détaillé, présentation clients'
    }
  ],
  printers3d: [
    {
      id: 'creality-ender-3-v3',
      name: 'Creality Ender-3 V3 SE',
      brand: 'Creality',
      price: 199,
      rating: 4.5,
      badge: 'MEILLEUR BUDGET',
      image: 'https://images.unsplash.com/photo-1631467606873-f8a4f4a7d728?w=400',
      amazonUrl: '#affiliate-ender3v3',
      specs: {
        technology: 'FDM',
        volume: '220 x 220 x 250 mm',
        resolution: '0.1 mm',
        speed: '250 mm/s',
        materials: 'PLA, PETG, TPU'
      },
      pros: [
        'Prix imbattable',
        'Communauté énorme',
        'Auto-nivellement',
        'Facile à monter'
      ],
      cons: [
        'Qualité moyenne sur détails fins',
        'Bruyante'
      ],
      idealFor: 'Maquettes grandes échelles, prototypes'
    },
    {
      id: 'bambu-lab-a1',
      name: 'Bambu Lab A1',
      brand: 'Bambu Lab',
      price: 459,
      rating: 4.8,
      badge: 'MEILLEUR CHOIX',
      image: 'https://images.unsplash.com/photo-1631467606873-f8a4f4a7d728?w=400',
      amazonUrl: '#affiliate-bambu-a1',
      specs: {
        technology: 'FDM',
        volume: '256 x 256 x 256 mm',
        resolution: '0.05 mm',
        speed: '500 mm/s',
        materials: 'PLA, PETG, TPU, ABS'
      },
      pros: [
        'Vitesse impressionnante',
        'Qualité excellente',
        'Calibration automatique',
        'App mobile'
      ],
      cons: [
        'Consommables propriétaires recommandés',
        'Nécessite WiFi'
      ],
      idealFor: 'Maquettes détaillées, production rapide'
    },
    {
      id: 'anycubic-photon-mono',
      name: 'Anycubic Photon Mono M5s',
      brand: 'Anycubic',
      price: 369,
      rating: 4.7,
      badge: 'MEILLEURE RÉSINE',
      image: 'https://images.unsplash.com/photo-1631467606873-f8a4f4a7d728?w=400',
      amazonUrl: '#affiliate-anycubic-mono',
      specs: {
        technology: 'MSLA (Résine)',
        volume: '218 x 123 x 200 mm',
        resolution: '0.019 mm (19 microns)',
        speed: '105 mm/h',
        materials: 'Résines UV'
      },
      pros: [
        'Détails ultra-fins',
        'Idéal pour maquettes précises',
        'Écran 12K',
        'Auto-nivellement'
      ],
      cons: [
        'Volume plus petit',
        'Post-traitement nécessaire',
        'Résine odorante'
      ],
      idealFor: 'Maquettes architecturales détaillées'
    }
  ]
};

export const getProductsByType = (type) => {
  return products[type] || [];
};

export const getProductById = (type, id) => {
  const productList = products[type] || [];
  return productList.find(p => p.id === id);
};
