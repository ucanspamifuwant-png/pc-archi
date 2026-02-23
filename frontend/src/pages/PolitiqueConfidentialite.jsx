import { Header } from '../components/Header';
import { Footer } from '../components/Footer';

export const PolitiqueConfidentialite = () => {
  return (
    <div className="min-h-screen flex flex-col" data-testid="politique-confidentialite-page">
      <Header />
      
      <main className="flex-grow py-16 md:py-24">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="font-heading text-4xl md:text-5xl font-extrabold tracking-tight mb-8">
            Politique de Confidentialité
          </h1>
          
          <p className="text-zinc-600 mb-8 text-sm font-mono">
            Dernière mise à jour : Janvier 2026
          </p>
          
          <div className="prose prose-zinc max-w-none space-y-8">
            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Introduction</h2>
              <p className="text-zinc-600 leading-relaxed">
                PC-Archi.fr s'engage à protéger la vie privée de ses utilisateurs. Cette politique de confidentialité explique comment nous collectons, utilisons et protégeons vos informations personnelles lorsque vous utilisez notre site web.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Données collectées</h2>
              <p className="text-zinc-600 leading-relaxed">
                Nous pouvons collecter les types d'informations suivants :
              </p>
              <ul className="list-disc pl-6 mt-4 space-y-2 text-zinc-600">
                <li>Données de navigation (pages visitées, durée de visite, type de navigateur)</li>
                <li>Adresse IP anonymisée</li>
                <li>Données de cookies (voir notre Politique Cookies)</li>
                <li>Informations fournies volontairement (formulaires de contact)</li>
              </ul>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Utilisation des données</h2>
              <p className="text-zinc-600 leading-relaxed">
                Les données collectées sont utilisées pour :
              </p>
              <ul className="list-disc pl-6 mt-4 space-y-2 text-zinc-600">
                <li>Améliorer l'expérience utilisateur sur notre site</li>
                <li>Analyser le trafic et les performances du site</li>
                <li>Personnaliser le contenu affiché</li>
                <li>Afficher des publicités pertinentes via Google AdSense</li>
                <li>Mesurer l'efficacité de nos liens d'affiliation</li>
              </ul>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Google AdSense et publicité</h2>
              <p className="text-zinc-600 leading-relaxed">
                Notre site utilise Google AdSense pour afficher des publicités. Google AdSense utilise des cookies pour diffuser des annonces basées sur vos visites antérieures sur notre site et d'autres sites web.
              </p>
              <p className="text-zinc-600 leading-relaxed mt-4">
                Vous pouvez désactiver la publicité personnalisée en visitant les <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener noreferrer" className="underline underline-offset-4 hover:text-black">Paramètres de publicité Google</a>.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Programme d'affiliation Amazon</h2>
              <p className="text-zinc-600 leading-relaxed">
                PC-Archi.fr participe au Programme Partenaires d'Amazon EU. Lorsque vous cliquez sur un lien Amazon et effectuez un achat, Amazon peut collecter des données vous concernant conformément à sa propre politique de confidentialité.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Partage des données</h2>
              <p className="text-zinc-600 leading-relaxed">
                Nous ne vendons pas vos données personnelles. Cependant, nous pouvons partager des données avec :
              </p>
              <ul className="list-disc pl-6 mt-4 space-y-2 text-zinc-600">
                <li>Google (Analytics et AdSense)</li>
                <li>Amazon (Programme Partenaires)</li>
                <li>Notre hébergeur web</li>
              </ul>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Vos droits (RGPD)</h2>
              <p className="text-zinc-600 leading-relaxed">
                Conformément au Règlement Général sur la Protection des Données (RGPD), vous disposez des droits suivants :
              </p>
              <ul className="list-disc pl-6 mt-4 space-y-2 text-zinc-600">
                <li>Droit d'accès à vos données personnelles</li>
                <li>Droit de rectification des données inexactes</li>
                <li>Droit à l'effacement de vos données</li>
                <li>Droit à la limitation du traitement</li>
                <li>Droit à la portabilité des données</li>
                <li>Droit d'opposition au traitement</li>
              </ul>
              <p className="text-zinc-600 leading-relaxed mt-4">
                Pour exercer ces droits, contactez-nous à : contact@pc-archi.fr
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Sécurité des données</h2>
              <p className="text-zinc-600 leading-relaxed">
                Nous mettons en œuvre des mesures de sécurité techniques et organisationnelles appropriées pour protéger vos données personnelles contre tout accès, modification, divulgation ou destruction non autorisés.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Modifications de cette politique</h2>
              <p className="text-zinc-600 leading-relaxed">
                Nous pouvons mettre à jour cette politique de confidentialité périodiquement. La date de dernière mise à jour sera toujours indiquée en haut de cette page.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Contact</h2>
              <p className="text-zinc-600 leading-relaxed">
                Pour toute question concernant cette politique de confidentialité, contactez-nous :<br />
                Email : contact@pc-archi.fr
              </p>
            </section>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};
