import { ExternalLink, Check, X } from 'lucide-react';
import { cn } from '../lib/utils';

export const ComparisonTable = ({ products, specKeys = [] }) => {
  if (!products || products.length === 0) return null;

  // Default spec keys if not provided
  const displayKeys = specKeys.length > 0 ? specKeys : Object.keys(products[0]?.specs || {});

  return (
    <div className="table-wrapper my-8" data-testid="comparison-table">
      <table className="w-full border-collapse text-left text-sm min-w-[800px]">
        {/* Header */}
        <thead>
          <tr className="bg-zinc-50 border-y border-black">
            <th className="p-4 font-mono text-xs uppercase tracking-wider text-zinc-600 w-32">
              Modèle
            </th>
            {products.map((product) => (
              <th key={product.id} className="p-4 font-heading font-bold text-base">
                <div className="flex flex-col gap-1">
                  {product.badge && (
                    <span className={cn(
                      'text-xs font-bold px-2 py-0.5 uppercase tracking-wider w-fit',
                      product.badge === 'MEILLEUR CHOIX' ? 'bg-black text-white' : 
                      'bg-zinc-200 text-zinc-900'
                    )}>
                      {product.badge}
                    </span>
                  )}
                  <span>{product.name}</span>
                  <span className="font-mono text-zinc-500 text-xs font-normal">{product.brand}</span>
                </div>
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {/* Price Row */}
          <tr className="border-b border-zinc-200 bg-zinc-50/50">
            <td className="p-4 font-mono text-xs uppercase tracking-wider text-zinc-600">
              Prix
            </td>
            {products.map((product) => (
              <td key={product.id} className="p-4">
                <span className="font-heading font-bold text-xl">{product.price} €</span>
              </td>
            ))}
          </tr>

          {/* Rating Row */}
          <tr className="border-b border-zinc-200">
            <td className="p-4 font-mono text-xs uppercase tracking-wider text-zinc-600">
              Note
            </td>
            {products.map((product) => (
              <td key={product.id} className="p-4">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-sm">{product.rating}/5</span>
                  <div className="flex">
                    {[...Array(5)].map((_, i) => (
                      <div 
                        key={i}
                        className={cn(
                          'w-2 h-2 mx-0.5',
                          i < Math.floor(product.rating) ? 'bg-black' : 'bg-zinc-200'
                        )}
                      />
                    ))}
                  </div>
                </div>
              </td>
            ))}
          </tr>

          {/* Specs Rows */}
          {displayKeys.map((key, index) => (
            <tr key={key} className={cn(
              'border-b border-zinc-200',
              index % 2 === 0 ? 'bg-zinc-50/50' : ''
            )}>
              <td className="p-4 font-mono text-xs uppercase tracking-wider text-zinc-600">
                {key}
              </td>
              {products.map((product) => (
                <td key={product.id} className="p-4 text-zinc-700">
                  {product.specs?.[key] || '—'}
                </td>
              ))}
            </tr>
          ))}

          {/* Pros Row */}
          <tr className="border-b border-zinc-200">
            <td className="p-4 font-mono text-xs uppercase tracking-wider text-zinc-600 align-top">
              Avantages
            </td>
            {products.map((product) => (
              <td key={product.id} className="p-4 align-top">
                <ul className="space-y-1">
                  {product.pros?.slice(0, 3).map((pro, i) => (
                    <li key={i} className="flex items-start gap-2 text-xs text-zinc-600">
                      <Check className="h-3 w-3 mt-0.5 text-black flex-shrink-0" />
                      <span>{pro}</span>
                    </li>
                  ))}
                </ul>
              </td>
            ))}
          </tr>

          {/* Cons Row */}
          <tr className="border-b border-zinc-200 bg-zinc-50/50">
            <td className="p-4 font-mono text-xs uppercase tracking-wider text-zinc-600 align-top">
              Inconvénients
            </td>
            {products.map((product) => (
              <td key={product.id} className="p-4 align-top">
                <ul className="space-y-1">
                  {product.cons?.slice(0, 2).map((con, i) => (
                    <li key={i} className="flex items-start gap-2 text-xs text-zinc-600">
                      <X className="h-3 w-3 mt-0.5 text-zinc-400 flex-shrink-0" />
                      <span>{con}</span>
                    </li>
                  ))}
                </ul>
              </td>
            ))}
          </tr>

          {/* CTA Row */}
          <tr>
            <td className="p-4"></td>
            {products.map((product) => (
              <td key={product.id} className="p-4">
                <a 
                  href={product.amazonUrl}
                  target="_blank"
                  rel="noopener noreferrer nofollow"
                  className="btn-amazon inline-flex items-center gap-2"
                  data-testid={`table-amazon-btn-${product.id}`}
                >
                  Voir le prix
                  <ExternalLink className="h-4 w-4" />
                </a>
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    </div>
  );
};
