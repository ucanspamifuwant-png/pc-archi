import { ExternalLink, Check, X } from 'lucide-react';
import { cn } from '../lib/utils';

export const ProductCard = ({ product, featured = false }) => {
  const { name, brand, price, rating, badge, image, amazonUrl, specs, pros, cons } = product;

  return (
    <div 
      className={cn(
        'group relative border bg-white p-6 transition-all duration-300',
        featured ? 'border-black' : 'border-zinc-200 hover:border-black'
      )}
      data-testid={`product-card-${product.id}`}
    >
      {/* Badge */}
      {badge && (
        <div className="absolute -top-3 left-6">
          <span className={cn(
            'text-xs font-bold px-3 py-1 uppercase tracking-wider',
            badge === 'MEILLEUR CHOIX' ? 'bg-black text-white' : 
            badge === 'MEILLEUR BUDGET' ? 'bg-zinc-200 text-zinc-900' :
            badge === 'PREMIUM' ? 'bg-black text-white' :
            'border border-black text-black bg-white'
          )}>
            {badge}
          </span>
        </div>
      )}

      {/* Image */}
      <div className="aspect-video mb-6 overflow-hidden bg-zinc-50">
        <img 
          src={image} 
          alt={name}
          className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500"
          loading="lazy"
        />
      </div>

      {/* Content */}
      <div className="space-y-4">
        {/* Brand & Name */}
        <div>
          <span className="text-xs font-mono text-zinc-500 uppercase tracking-wider">{brand}</span>
          <h3 className="font-heading font-bold text-lg md:text-xl mt-1">{name}</h3>
        </div>

        {/* Price & Rating */}
        <div className="flex items-center justify-between">
          <span className="font-heading font-bold text-2xl">{price} €</span>
          <div className="flex items-center gap-1">
            <span className="text-sm font-mono">{rating}/5</span>
            <div className="flex">
              {[...Array(5)].map((_, i) => (
                <div 
                  key={i}
                  className={cn(
                    'w-2 h-2 mx-0.5',
                    i < Math.floor(rating) ? 'bg-black' : 'bg-zinc-200'
                  )}
                />
              ))}
            </div>
          </div>
        </div>

        {/* Key Specs */}
        <div className="border-t border-zinc-100 pt-4">
          <div className="grid grid-cols-2 gap-2 text-xs font-mono">
            {specs && Object.entries(specs).slice(0, 4).map(([key, value]) => (
              <div key={key} className="truncate">
                <span className="text-zinc-400 uppercase">{key}:</span>
                <span className="ml-1 text-zinc-700">{value}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Pros/Cons (if expanded view) */}
        {featured && (
          <div className="border-t border-zinc-100 pt-4 grid grid-cols-2 gap-4">
            <div>
              <span className="text-xs font-bold uppercase tracking-wider text-zinc-500 mb-2 block">Avantages</span>
              <ul className="space-y-1">
                {pros?.slice(0, 3).map((pro, i) => (
                  <li key={i} className="flex items-start gap-2 text-xs text-zinc-600">
                    <Check className="h-3 w-3 mt-0.5 text-black flex-shrink-0" />
                    <span>{pro}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <span className="text-xs font-bold uppercase tracking-wider text-zinc-500 mb-2 block">Inconvénients</span>
              <ul className="space-y-1">
                {cons?.slice(0, 2).map((con, i) => (
                  <li key={i} className="flex items-start gap-2 text-xs text-zinc-600">
                    <X className="h-3 w-3 mt-0.5 text-zinc-400 flex-shrink-0" />
                    <span>{con}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}

        {/* CTA Button */}
        <a 
          href={amazonUrl}
          target="_blank"
          rel="noopener noreferrer nofollow"
          className="btn-amazon w-full flex items-center justify-center gap-2 mt-4"
          data-testid={`amazon-btn-${product.id}`}
        >
          Voir sur Amazon
          <ExternalLink className="h-4 w-4" />
        </a>
      </div>
    </div>
  );
};
