import { useParams, Link } from 'react-router-dom';
import { ChevronRight } from 'lucide-react';
import { Header } from '../components/Header';
import { Footer } from '../components/Footer';
import { ArticleCard } from '../components/ArticleCard';
import { AdSlot } from '../components/AdSlot';
import { categories, getArticlesByCategory } from '../data/articles';

export const CategoryPage = () => {
  const { slug } = useParams();
  const category = categories.find(c => c.slug === slug);
  const categoryArticles = getArticlesByCategory(slug);

  if (!category) {
    return (
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-grow flex items-center justify-center">
          <div className="text-center">
            <h1 className="font-heading text-4xl font-bold mb-4">Catégorie non trouvée</h1>
            <Link to="/" className="btn-amazon">Retour à l'accueil</Link>
          </div>
        </main>
        <Footer />
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col" data-testid={`category-page-${slug}`}>
      <Header />
      
      <main className="flex-grow">
        {/* Breadcrumb */}
        <div className="border-b border-zinc-200 bg-zinc-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <nav className="flex items-center gap-2 text-sm" data-testid="breadcrumb">
              <Link to="/" className="text-zinc-500 hover:text-black transition-colors">
                Accueil
              </Link>
              <ChevronRight className="h-4 w-4 text-zinc-400" />
              <span className="text-black font-medium">{category.name}</span>
            </nav>
          </div>
        </div>

        {/* Category Header */}
        <section className="py-12 md:py-20 border-b border-zinc-200">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <span className="font-mono text-xs uppercase tracking-widest text-zinc-500 mb-4 block">
              Catégorie
            </span>
            <h1 className="font-heading text-4xl md:text-5xl font-extrabold tracking-tight mb-4">
              {category.name}
            </h1>
            <p className="text-lg text-zinc-600 max-w-2xl">
              {category.description}
            </p>
          </div>
        </section>

        {/* AdSlot */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <AdSlot size="leaderboard" />
        </div>

        {/* Articles Grid */}
        <section className="py-12 md:py-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            {categoryArticles.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {categoryArticles.map((article) => (
                  <ArticleCard key={article.id} article={article} />
                ))}
              </div>
            ) : (
              <div className="text-center py-16">
                <p className="text-zinc-500 mb-4">Aucun article dans cette catégorie pour le moment.</p>
                <Link to="/" className="btn-amazon">Voir tous les articles</Link>
              </div>
            )}
          </div>
        </section>

        {/* Related Categories */}
        <section className="py-12 md:py-16 bg-zinc-50 border-t border-zinc-200">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="font-heading text-2xl font-bold tracking-tight mb-8">
              Autres catégories
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              {categories
                .filter(c => c.slug !== slug)
                .slice(0, 3)
                .map((cat) => (
                  <Link
                    key={cat.id}
                    to={`/categorie/${cat.slug}`}
                    className="group border border-zinc-200 bg-white p-6 hover:border-black transition-colors"
                  >
                    <h3 className="font-heading font-bold mb-2 group-hover:underline underline-offset-4 decoration-1">
                      {cat.name}
                    </h3>
                    <span className="font-mono text-xs text-zinc-500">
                      {cat.articleCount} article{cat.articleCount !== 1 ? 's' : ''}
                    </span>
                  </Link>
                ))}
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
};
