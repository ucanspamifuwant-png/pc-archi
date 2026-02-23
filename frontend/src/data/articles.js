export const articles = [
  {
    id: 'meilleur-pc-portable-architecture-2026',
    slug: 'meilleur-pc-portable-architecture-2026',
    title: 'Meilleur PC Portable pour Architecture (Guide 2026)',
    metaDescription: 'Découvrez notre sélection des meilleurs PC portables pour étudiants en architecture en 2026. Comparatif complet, critères de choix et recommandations.',
    category: 'pc-architecture',
    categoryName: 'PC pour Architecture',
    excerpt: 'Guide complet pour choisir le PC portable idéal pour vos études d\'architecture. Comparatif des meilleurs modèles 2026.',
    image: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800',
    readTime: '15 min',
    updatedAt: '2026-01-15',
    featured: true,
    relatedArticles: ['pc-revit-archicad-rhino', 'configuration-minimale-architecture']
  },
  {
    id: 'pc-revit-archicad-rhino',
    slug: 'pc-revit-archicad-rhino',
    title: 'Quel PC pour Revit, ArchiCAD et Rhino ?',
    metaDescription: 'Configuration PC optimale pour Revit, ArchiCAD et Rhino. Découvrez les specs recommandées pour chaque logiciel d\'architecture.',
    category: 'pc-architecture',
    categoryName: 'PC pour Architecture',
    excerpt: 'Configurations PC recommandées pour les principaux logiciels d\'architecture : Revit, ArchiCAD, Rhino et plus.',
    image: 'https://images.unsplash.com/photo-1547082299-de196ea013d6?w=800',
    readTime: '12 min',
    updatedAt: '2026-01-12',
    featured: true,
    relatedArticles: ['meilleur-pc-portable-architecture-2026', 'configuration-minimale-architecture']
  },
  {
    id: 'configuration-minimale-architecture',
    slug: 'configuration-minimale-architecture',
    title: 'Configuration Minimale pour Études d\'Architecture',
    metaDescription: 'Quelle configuration PC minimale pour des études d\'architecture ? CPU, RAM, GPU, stockage - tous les critères expliqués.',
    category: 'pc-architecture',
    categoryName: 'PC pour Architecture',
    excerpt: 'Les spécifications techniques minimales pour un PC destiné aux études d\'architecture. Guide pratique et économique.',
    image: 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=800',
    readTime: '10 min',
    updatedAt: '2026-01-10',
    featured: false,
    relatedArticles: ['meilleur-pc-portable-architecture-2026', 'pc-revit-archicad-rhino']
  },
  {
    id: 'meilleure-tablette-graphique-architecture',
    slug: 'meilleure-tablette-graphique-architecture',
    title: 'Meilleure Tablette Graphique pour Étudiant en Architecture',
    metaDescription: 'Comparatif des meilleures tablettes graphiques pour étudiants en architecture. Wacom, XP-Pen, Huion - laquelle choisir ?',
    category: 'tablettes-graphiques',
    categoryName: 'Tablettes Graphiques',
    excerpt: 'Comparatif complet des tablettes graphiques adaptées aux études d\'architecture. Prix, fonctionnalités et recommandations.',
    image: 'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=800',
    readTime: '13 min',
    updatedAt: '2026-01-08',
    featured: true,
    relatedArticles: ['meilleur-pc-portable-architecture-2026', 'meilleure-imprimante-3d-etudiant']
  },
  {
    id: 'meilleure-imprimante-3d-etudiant',
    slug: 'meilleure-imprimante-3d-etudiant',
    title: 'Meilleure Imprimante 3D pour Étudiant',
    metaDescription: 'Guide d\'achat des meilleures imprimantes 3D pour étudiants en architecture. FDM, résine, budget - notre sélection 2026.',
    category: 'imprimantes-3d',
    categoryName: 'Imprimantes 3D',
    excerpt: 'Sélection des meilleures imprimantes 3D abordables pour réaliser vos maquettes d\'architecture. Guide complet.',
    image: 'https://images.unsplash.com/photo-1631467606873-f8a4f4a7d728?w=800',
    readTime: '14 min',
    updatedAt: '2026-01-05',
    featured: true,
    relatedArticles: ['meilleure-tablette-graphique-architecture', 'configuration-minimale-architecture']
  }
];

export const categories = [
  {
    id: 'pc-architecture',
    slug: 'pc-architecture',
    name: 'PC pour Architecture',
    description: 'Ordinateurs portables et fixes optimisés pour les logiciels d\'architecture comme Revit, ArchiCAD et Rhino.',
    image: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800',
    articleCount: 3
  },
  {
    id: 'tablettes-graphiques',
    slug: 'tablettes-graphiques',
    name: 'Tablettes Graphiques',
    description: 'Tablettes graphiques pour le dessin technique et la création architecturale.',
    image: 'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=800',
    articleCount: 1
  },
  {
    id: 'imprimantes-3d',
    slug: 'imprimantes-3d',
    name: 'Imprimantes 3D',
    description: 'Imprimantes 3D pour la réalisation de maquettes architecturales.',
    image: 'https://images.unsplash.com/photo-1631467606873-f8a4f4a7d728?w=800',
    articleCount: 1
  },
  {
    id: 'logiciels',
    slug: 'logiciels',
    name: 'Logiciels',
    description: 'Guides et comparatifs des logiciels essentiels pour les étudiants en architecture.',
    image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800',
    articleCount: 0
  }
];

export const getArticlesByCategory = (categorySlug) => {
  return articles.filter(article => article.category === categorySlug);
};

export const getArticleBySlug = (slug) => {
  return articles.find(article => article.slug === slug);
};

export const getFeaturedArticles = () => {
  return articles.filter(article => article.featured);
};

export const getRelatedArticles = (articleId) => {
  const article = articles.find(a => a.id === articleId);
  if (!article) return [];
  return articles.filter(a => article.relatedArticles?.includes(a.id));
};
