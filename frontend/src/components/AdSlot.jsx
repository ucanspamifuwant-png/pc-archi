import { cn } from '../lib/utils';

export const AdSlot = ({ 
  size = 'medium', 
  className,
  label = 'Espace publicitaire'
}) => {
  const sizeClasses = {
    small: 'h-24',
    medium: 'h-40',
    large: 'h-64',
    leaderboard: 'h-24 w-full',
    sidebar: 'h-[600px] w-full max-w-[300px]',
    rectangle: 'h-[250px] w-full max-w-[300px]'
  };

  return (
    <div 
      className={cn(
        'ad-slot',
        sizeClasses[size],
        className
      )}
      data-testid={`ad-slot-${size}`}
      aria-label={label}
    >
      <div className="text-center">
        <span className="font-mono text-xs uppercase tracking-wider">{label}</span>
        <span className="block text-xs mt-1 opacity-60">AdSense</span>
      </div>
    </div>
  );
};
