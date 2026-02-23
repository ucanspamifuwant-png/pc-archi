import { Header } from '../components/Header';
import { Footer } from '../components/Footer';

export const MentionsLegales = () => {
  return (
    <div className="min-h-screen flex flex-col" data-testid="mentions-legales-page">
      <Header />
      
      <main className="flex-grow py-16 md:py-24">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="font-heading text-4xl md:text-5xl font-extrabold tracking-tight mb-8">
            Mentions Légales
          </h1>
          
          <div className="prose prose-zinc max-w-none space-y-8">
            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Éditeur du site</h2>
              <p className="text-zinc-600 leading-relaxed">
                Le site PC-Archi.fr est édité par [Nom de l'éditeur], [forme juridique].<br />
                Siège social : [Adresse]<br />
                Numéro de téléphone : [Numéro]<br />
                Email : contact@pc-archi.fr<br />
                Numéro SIRET : [Numéro SIRET]<br />
                Numéro de TVA intracommunautaire : [Numéro TVA]
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Directeur de la publication</h2>
              <p className="text-zinc-600 leading-relaxed">
                Le directeur de la publication est [Nom du directeur].
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Hébergement</h2>
              <p className="text-zinc-600 leading-relaxed">
                Ce site est hébergé par [Nom de l'hébergeur]<br />
                Adresse : [Adresse de l'hébergeur]<br />
                Téléphone : [Numéro de téléphone]
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Propriété intellectuelle</h2>
              <p className="text-zinc-600 leading-relaxed">
                L'ensemble de ce site relève de la législation française et internationale sur le droit d'auteur et la propriété intellectuelle. Tous les droits de reproduction sont réservés, y compris pour les documents téléchargeables et les représentations iconographiques et photographiques.
              </p>
              <p className="text-zinc-600 leading-relaxed mt-4">
                La reproduction de tout ou partie de ce site sur un support électronique ou autre quel qu'il soit est formellement interdite sauf autorisation expresse du directeur de la publication.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Liens d'affiliation</h2>
              <p className="text-zinc-600 leading-relaxed">
                PC-Archi.fr participe au Programme Partenaires d'Amazon EU, un programme d'affiliation conçu pour permettre à des sites de percevoir une rémunération grâce à la création de liens vers Amazon.fr.
              </p>
              <p className="text-zinc-600 leading-relaxed mt-4">
                En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises. Cette affiliation n'affecte en rien le prix des produits pour vous.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Limitation de responsabilité</h2>
              <p className="text-zinc-600 leading-relaxed">
                Les informations contenues sur ce site sont aussi précises que possible et le site est périodiquement remis à jour, mais peut toutefois contenir des inexactitudes, des omissions ou des lacunes.
              </p>
              <p className="text-zinc-600 leading-relaxed mt-4">
                PC-Archi.fr ne pourra être tenu responsable des dommages directs et indirects causés au matériel de l'utilisateur, lors de l'accès au site, et résultant soit de l'utilisation d'un matériel ne répondant pas aux spécifications, soit de l'apparition d'un bug ou d'une incompatibilité.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Droit applicable</h2>
              <p className="text-zinc-600 leading-relaxed">
                Les présentes mentions légales sont régies par le droit français. En cas de litige, les tribunaux français seront seuls compétents.
              </p>
            </section>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};
