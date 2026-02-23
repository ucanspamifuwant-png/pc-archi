import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "./ui/accordion";

export const FAQ = ({ items, title = "Questions Fréquentes" }) => {
  if (!items || items.length === 0) return null;

  return (
    <section className="my-12" data-testid="faq-section">
      <h2 className="text-2xl md:text-3xl font-bold font-heading tracking-tight mb-8">
        {title}
      </h2>
      
      <Accordion type="single" collapsible className="w-full">
        {items.map((item, index) => (
          <AccordionItem 
            key={index} 
            value={`item-${index}`}
            className="border-b border-zinc-200"
          >
            <AccordionTrigger 
              className="text-left font-heading font-semibold text-base md:text-lg py-5 hover:no-underline"
              data-testid={`faq-trigger-${index}`}
            >
              {item.question}
            </AccordionTrigger>
            <AccordionContent className="text-zinc-600 leading-relaxed pb-5">
              {item.answer}
            </AccordionContent>
          </AccordionItem>
        ))}
      </Accordion>

      {/* Schema.org FAQ structured data */}
      <script type="application/ld+json" dangerouslySetInnerHTML={{
        __html: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": items.map(item => ({
            "@type": "Question",
            "name": item.question,
            "acceptedAnswer": {
              "@type": "Answer",
              "text": item.answer
            }
          }))
        })
      }} />
    </section>
  );
};
