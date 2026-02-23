import { Link } from 'react-router-dom';
import { ArrowRight, Monitor, PenTool, Printer, Code } from 'lucide-react';
import { Header } from '../components/Header';
import { Footer } from '../components/Footer';
import { ArticleCard } from '../components/ArticleCard';
import { AdSlot } from '../components/AdSlot';
import { getFeaturedArticles, categories } from '../data/articles';

const categoryIcons = {
  'pc-architecture': Monitor,
  'tablettes-graphiques': PenTool,
  'imprimantes-3d': Printer,
  'logiciels': Code
};

export const HomePage = () => {
  const featuredArticles = getFeaturedArticles();
  const mainArticle = featuredArticles[0];
  const otherArticles = featuredArticles.slice(1);

  return (
    <div className="min-h-screen flex flex-col" data-testid="home-page">
      <Header />
      
      <main className="flex-grow">
        {/* Hero Section */}
        <section className="bg-white border-b border-zinc-200" data-testid="hero-section">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24">
            <div className="max-w-4xl">
              <span className="font-mono text-xs uppercase tracking-widest text-zinc-500 mb-4 block">
                Guide 2026
              </span>
              <h1 className="font-heading text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-black leading-tight mb-6">
                Le guide ultime pour<br />
                <span className="text-zinc-500">étudiants en architecture</span>
              </h1>
              <p className="text-lg md:text-xl text-zinc-600 leading-relaxed max-w-2xl mb-8">
                Trouvez le PC portable, la tablette graphique ou l'imprimante 3D parfait pour vos études d'architecture. Comparatifs indépendants et conseils d'experts.
              </p>
              <div className="flex flex-wrap gap-4">
                <Link 
                  to="/article/meilleur-pc-portable-architecture-2026"
                  className="btn-amazon"
                  data-testid="hero-cta-primary"
                >
                  Guide PC 2026
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Link>
                <Link 
                  to="/categorie/pc-architecture"
                  className="h-12 px-8 bg-white text-black border border-black hover:bg-zinc-50 transition-colors duration-200 font-medium text-sm tracking-wide uppercase inline-flex items-center"
                  data-testid="hero-cta-secondary"
                >
                  Voir les catégories
                </Link>
              </div>
            </div>
          </div>
        </section>

        {/* Categories Grid */}
        <section className="py-16 md:py-24 bg-zinc-50" data-testid="categories-section">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex items-end justify-between mb-12">
              <div>
                <span className="font-mono text-xs uppercase tracking-widest text-zinc-500 mb-2 block">
                  Explorer
                </span>
                <h2 className="font-heading text-3xl md:text-4xl font-bold tracking-tight">
                  Catégories
                </h2>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-px bg-zinc-200">
              {categories.map((category) => {
                const Icon = categoryIcons[category.id] || Monitor;
                return (
                  <Link
                    key={category.id}
                    to={`/categorie/${category.slug}`}
                    className="group bg-white p-8 hover:bg-zinc-50 transition-colors"
                    data-testid={`category-link-${category.slug}`}
                  >
                    <Icon className="h-8 w-8 mb-6 text-zinc-400 group-hover:text-black transition-colors" strokeWidth={1.5} />
                    <h3 className="font-heading font-bold text-lg mb-2 group-hover:underline underline-offset-4 decoration-1">
                      {category.name}
                    </h3>
                    <p className="text-sm text-zinc-500 leading-relaxed">
                      {category.description}
                    </p>
                    <span className="font-mono text-xs text-zinc-400 mt-4 block">
                      {category.articleCount} article{category.articleCount !== 1 ? 's' : ''}
                    </span>
                  </Link>
                );
              })}
            </div>
          </div>
        </section>

        {/* AdSlot */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <AdSlot size="leaderboard" />
        </div>

        {/* Featured Articles */}
        <section className="py-16 md:py-24" data-testid="featured-articles-section">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex items-end justify-between mb-12">
              <div>
                <span className="font-mono text-xs uppercase tracking-widest text-zinc-500 mb-2 block">
                  À la une
                </span>
                <h2 className="font-heading text-3xl md:text-4xl font-bold tracking-tight">
                  Articles populaires
                </h2>
              </div>
              <Link 
                to="/categorie/pc-architecture"
                className="hidden md:flex items-center gap-1 text-sm font-medium uppercase tracking-wider text-zinc-500 hover:text-black transition-colors"
              >
                Tous les articles
                <ArrowRight className="h-4 w-4" />
              </Link>
            </div>

            {/* Main Featured Article */}
            {mainArticle && (
              <div className="mb-8">
                <ArticleCard article={mainArticle} featured />
              </div>
            )}

            {/* Other Featured Articles */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {otherArticles.map((article) => (
                <ArticleCard key={article.id} article={article} />
              ))}
            </div>
          </div>
        </section>

        {/* Trust Section */}
        <section className="py-16 md:py-24 bg-black text-white" data-testid="trust-section">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8">
              <div>
                <span className="font-mono text-5xl font-bold text-zinc-500">01</span>
                <h3 className="font-heading font-bold text-xl mt-4 mb-2">Tests indépendants</h3>
                <p className="text-zinc-400 text-sm leading-relaxed">
                  Nos recommandations sont basées sur des critères techniques objectifs et adaptés aux besoins des étudiants en architecture.
                </p>
              </div>
              <div>
                <span className="font-mono text-5xl font-bold text-zinc-500">02</span>
                <h3 className="font-heading font-bold text-xl mt-4 mb-2">Expertise métier</h3>
                <p className="text-zinc-400 text-sm leading-relaxed">
                  Nous connaissons les exigences des logiciels d'architecture : Revit, ArchiCAD, Rhino, SketchUp et bien d'autres.
                </p>
              </div>
              <div>
                <span className="font-mono text-5xl font-bold text-zinc-500">03</span>
                <h3 className="font-heading font-bold text-xl mt-4 mb-2">Mise à jour continue</h3>
                <p className="text-zinc-400 text-sm leading-relaxed">
                  Nos guides sont régulièrement mis à jour pour refléter les dernières sorties et évolutions du marché.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* AdSlot */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <AdSlot size="leaderboard" />
        </div>
      </main>

      <Footer />
    </div>
  );
};
