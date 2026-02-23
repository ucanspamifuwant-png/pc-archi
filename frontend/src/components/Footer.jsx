import { Link } from 'react-router-dom';
import { categories } from '../data/articles';

export const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-zinc-950 text-white" data-testid="footer">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 md:gap-8">
          {/* Brand */}
          <div className="md:col-span-1">
            <Link to="/" className="font-heading font-extrabold text-2xl tracking-tighter">
              PC-ARCHI
            </Link>
            <p className="mt-4 text-zinc-400 text-sm leading-relaxed">
              Le guide de référence pour choisir votre équipement informatique en tant qu'étudiant en architecture.
            </p>
          </div>

          {/* Categories */}
          <div>
            <h3 className="font-heading font-bold text-xs tracking-wider uppercase mb-6">
              Catégories
            </h3>
            <ul className="space-y-3">
              {categories.map((category) => (
                <li key={category.id}>
                  <Link 
                    to={`/categorie/${category.slug}`}
                    className="text-zinc-400 hover:text-white transition-colors text-sm"
                  >
                    {category.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Resources */}
          <div>
            <h3 className="font-heading font-bold text-xs tracking-wider uppercase mb-6">
              Ressources
            </h3>
            <ul className="space-y-3">
              <li>
                <Link to="/article/meilleur-pc-portable-architecture-2026" className="text-zinc-400 hover:text-white transition-colors text-sm">
                  Guide PC 2026
                </Link>
              </li>
              <li>
                <Link to="/article/pc-revit-archicad-rhino" className="text-zinc-400 hover:text-white transition-colors text-sm">
                  PC pour Revit
                </Link>
              </li>
              <li>
                <Link to="/article/meilleure-tablette-graphique-architecture" className="text-zinc-400 hover:text-white transition-colors text-sm">
                  Tablettes graphiques
                </Link>
              </li>
              <li>
                <Link to="/article/meilleure-imprimante-3d-etudiant" className="text-zinc-400 hover:text-white transition-colors text-sm">
                  Imprimantes 3D
                </Link>
              </li>
            </ul>
          </div>

          {/* Legal */}
          <div>
            <h3 className="font-heading font-bold text-xs tracking-wider uppercase mb-6">
              Informations
            </h3>
            <ul className="space-y-3">
              <li>
                <Link to="/mentions-legales" className="text-zinc-400 hover:text-white transition-colors text-sm">
                  Mentions légales
                </Link>
              </li>
              <li>
                <Link to="/politique-confidentialite" className="text-zinc-400 hover:text-white transition-colors text-sm">
                  Politique de confidentialité
                </Link>
              </li>
              <li>
                <Link to="/cookies" className="text-zinc-400 hover:text-white transition-colors text-sm">
                  Politique cookies
                </Link>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom */}
        <div className="mt-16 pt-8 border-t border-zinc-800">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-zinc-500 text-xs">
              © {currentYear} PC-Archi.fr - Tous droits réservés
            </p>
            <p className="text-zinc-600 text-xs">
              En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};
