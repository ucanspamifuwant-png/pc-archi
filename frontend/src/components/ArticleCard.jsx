import { Link } from 'react-router-dom';
import { Clock, ArrowRight } from 'lucide-react';
import { cn } from '../lib/utils';

export const ArticleCard = ({ article, featured = false }) => {
  const { slug, title, excerpt, image, readTime, categoryName, updatedAt } = article;

  return (
    <Link 
      to={`/article/${slug}`}
      className={cn(
        'group relative border border-zinc-200 bg-white transition-all duration-300 hover:border-black block',
        featured ? 'md:flex' : ''
      )}
      data-testid={`article-card-${slug}`}
    >
      {/* Image */}
      <div className={cn(
        'overflow-hidden bg-zinc-100',
        featured ? 'md:w-1/2 aspect-video md:aspect-auto' : 'aspect-video'
      )}>
        <img 
          src={image} 
          alt={title}
          className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500"
          loading="lazy"
        />
      </div>

      {/* Content */}
      <div className={cn(
        'p-6',
        featured ? 'md:w-1/2 md:p-8 flex flex-col justify-center' : ''
      )}>
        {/* Category & Date */}
        <div className="flex items-center gap-4 mb-3">
          <span className="text-xs font-mono uppercase tracking-wider text-zinc-500">
            {categoryName}
          </span>
          <span className="text-xs text-zinc-400">
            {new Date(updatedAt).toLocaleDateString('fr-FR', { 
              day: 'numeric', 
              month: 'long', 
              year: 'numeric' 
            })}
          </span>
        </div>

        {/* Title */}
        <h3 className={cn(
          'font-heading font-bold tracking-tight mb-3 group-hover:underline underline-offset-4 decoration-1',
          featured ? 'text-xl md:text-2xl' : 'text-lg'
        )}>
          {title}
        </h3>

        {/* Excerpt */}
        <p className="text-zinc-600 text-sm leading-relaxed mb-4 line-clamp-2">
          {excerpt}
        </p>

        {/* Footer */}
        <div className="flex items-center justify-between mt-auto">
          <div className="flex items-center gap-1.5 text-zinc-500">
            <Clock className="h-3.5 w-3.5" />
            <span className="text-xs font-mono">{readTime}</span>
          </div>
          
          <span className="flex items-center gap-1 text-xs font-medium uppercase tracking-wider text-black group-hover:gap-2 transition-all">
            Lire
            <ArrowRight className="h-3.5 w-3.5" />
          </span>
        </div>
      </div>
    </Link>
  );
};
