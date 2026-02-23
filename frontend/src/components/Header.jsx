import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Menu, X, ChevronDown } from 'lucide-react';
import { categories } from '../data/articles';

export const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isCategoryOpen, setIsCategoryOpen] = useState(false);
  const location = useLocation();

  const isActive = (path) => location.pathname === path;

  return (
    <header className="sticky top-0 z-50 bg-white/95 backdrop-blur-sm border-b border-zinc-200" data-testid="header">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16 md:h-20">
          {/* Logo */}
          <Link 
            to="/" 
            className="font-heading font-extrabold text-xl md:text-2xl tracking-tighter text-black hover:opacity-80 transition-opacity"
            data-testid="logo-link"
          >
            PC-ARCHI
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8" data-testid="desktop-nav">
            <Link 
              to="/" 
              className={`text-sm font-medium tracking-wide uppercase transition-colors ${
                isActive('/') ? 'text-black' : 'text-zinc-500 hover:text-black'
              }`}
            >
              Accueil
            </Link>
            
            {/* Categories Dropdown */}
            <div 
              className="relative"
              onMouseEnter={() => setIsCategoryOpen(true)}
              onMouseLeave={() => setIsCategoryOpen(false)}
            >
              <button 
                className="flex items-center text-sm font-medium tracking-wide uppercase text-zinc-500 hover:text-black transition-colors"
                data-testid="categories-dropdown-btn"
              >
                Catégories
                <ChevronDown className="ml-1 h-4 w-4" />
              </button>
              
              {isCategoryOpen && (
                <div className="absolute top-full left-0 mt-2 w-64 bg-white border border-zinc-200 shadow-lg" data-testid="categories-dropdown">
                  {categories.map((category) => (
                    <Link
                      key={category.id}
                      to={`/categorie/${category.slug}`}
                      className="block px-4 py-3 text-sm text-zinc-700 hover:bg-zinc-50 hover:text-black transition-colors border-b border-zinc-100 last:border-b-0"
                    >
                      {category.name}
                    </Link>
                  ))}
                </div>
              )}
            </div>

            <Link 
              to="/mentions-legales" 
              className={`text-sm font-medium tracking-wide uppercase transition-colors ${
                isActive('/mentions-legales') ? 'text-black' : 'text-zinc-500 hover:text-black'
              }`}
            >
              À propos
            </Link>
          </nav>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Menu"
            data-testid="mobile-menu-btn"
          >
            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-zinc-200" data-testid="mobile-nav">
            <nav className="flex flex-col space-y-4">
              <Link 
                to="/" 
                className="text-sm font-medium tracking-wide uppercase text-zinc-700"
                onClick={() => setIsMenuOpen(false)}
              >
                Accueil
              </Link>
              
              <div className="border-t border-zinc-100 pt-4">
                <span className="text-xs font-bold tracking-wider uppercase text-zinc-400 mb-3 block">
                  Catégories
                </span>
                {categories.map((category) => (
                  <Link
                    key={category.id}
                    to={`/categorie/${category.slug}`}
                    className="block py-2 text-sm text-zinc-700"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    {category.name}
                  </Link>
                ))}
              </div>
              
              <div className="border-t border-zinc-100 pt-4">
                <Link 
                  to="/mentions-legales" 
                  className="text-sm font-medium tracking-wide uppercase text-zinc-700"
                  onClick={() => setIsMenuOpen(false)}
                >
                  À propos
                </Link>
              </div>
            </nav>
          </div>
        )}
      </div>
    </header>
  );
};
