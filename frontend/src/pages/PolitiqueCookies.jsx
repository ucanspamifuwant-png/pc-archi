import { Header } from '../components/Header';
import { Footer } from '../components/Footer';

export const PolitiqueCookies = () => {
  return (
    <div className="min-h-screen flex flex-col" data-testid="politique-cookies-page">
      <Header />
      
      <main className="flex-grow py-16 md:py-24">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="font-heading text-4xl md:text-5xl font-extrabold tracking-tight mb-8">
            Politique des Cookies
          </h1>
          
          <p className="text-zinc-600 mb-8 text-sm font-mono">
            Dernière mise à jour : Janvier 2026
          </p>
          
          <div className="prose prose-zinc max-w-none space-y-8">
            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Qu'est-ce qu'un cookie ?</h2>
              <p className="text-zinc-600 leading-relaxed">
                Un cookie est un petit fichier texte déposé sur votre appareil (ordinateur, tablette, smartphone) lors de votre visite sur un site web. Il permet au site de mémoriser des informations sur votre visite, comme votre langue préférée et d'autres paramètres.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Types de cookies utilisés</h2>
              
              <h3 className="font-heading text-xl font-semibold mt-6 mb-3">Cookies essentiels</h3>
              <p className="text-zinc-600 leading-relaxed">
                Ces cookies sont nécessaires au fonctionnement du site. Ils vous permettent d'utiliser les fonctionnalités de base comme la navigation entre les pages.
              </p>

              <h3 className="font-heading text-xl font-semibold mt-6 mb-3">Cookies analytiques (Google Analytics)</h3>
              <p className="text-zinc-600 leading-relaxed">
                Nous utilisons Google Analytics pour comprendre comment les visiteurs interagissent avec notre site. Ces cookies collectent des informations de manière anonyme, notamment :
              </p>
              <ul className="list-disc pl-6 mt-2 space-y-1 text-zinc-600">
                <li>Nombre de visiteurs</li>
                <li>Pages les plus consultées</li>
                <li>Durée des visites</li>
                <li>Source du trafic</li>
              </ul>

              <h3 className="font-heading text-xl font-semibold mt-6 mb-3">Cookies publicitaires (Google AdSense)</h3>
              <p className="text-zinc-600 leading-relaxed">
                Google AdSense utilise des cookies pour afficher des publicités pertinentes basées sur vos centres d'intérêt. Ces cookies permettent :
              </p>
              <ul className="list-disc pl-6 mt-2 space-y-1 text-zinc-600">
                <li>D'afficher des publicités personnalisées</li>
                <li>De limiter le nombre de fois qu'une publicité vous est présentée</li>
                <li>De mesurer l'efficacité des campagnes publicitaires</li>
              </ul>

              <h3 className="font-heading text-xl font-semibold mt-6 mb-3">Cookies d'affiliation (Amazon)</h3>
              <p className="text-zinc-600 leading-relaxed">
                En tant que participant au Programme Partenaires Amazon EU, des cookies peuvent être déposés lorsque vous cliquez sur un lien vers Amazon. Ces cookies permettent de tracer votre parcours d'achat et de nous attribuer une commission sur les ventes éligibles.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Durée de conservation des cookies</h2>
              <div className="overflow-x-auto">
                <table className="w-full text-sm border-collapse mt-4">
                  <thead>
                    <tr className="border-y border-black bg-zinc-50">
                      <th className="p-3 text-left font-mono text-xs uppercase">Type</th>
                      <th className="p-3 text-left font-mono text-xs uppercase">Durée</th>
                    </tr>
                  </thead>
                  <tbody className="text-zinc-600">
                    <tr className="border-b border-zinc-200">
                      <td className="p-3">Cookies essentiels</td>
                      <td className="p-3">Session (supprimés à la fermeture du navigateur)</td>
                    </tr>
                    <tr className="border-b border-zinc-200">
                      <td className="p-3">Google Analytics</td>
                      <td className="p-3">26 mois maximum</td>
                    </tr>
                    <tr className="border-b border-zinc-200">
                      <td className="p-3">Google AdSense</td>
                      <td className="p-3">Variable selon le cookie (jusqu'à 2 ans)</td>
                    </tr>
                    <tr className="border-b border-zinc-200">
                      <td className="p-3">Amazon Partenaires</td>
                      <td className="p-3">24 heures pour les commissions</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Comment gérer les cookies ?</h2>
              <p className="text-zinc-600 leading-relaxed">
                Vous pouvez contrôler et/ou supprimer les cookies comme vous le souhaitez. Vous pouvez supprimer tous les cookies déjà présents sur votre ordinateur et paramétrer la plupart des navigateurs pour qu'ils les bloquent.
              </p>
              
              <h3 className="font-heading text-xl font-semibold mt-6 mb-3">Dans votre navigateur</h3>
              <ul className="list-disc pl-6 mt-2 space-y-2 text-zinc-600">
                <li><strong>Chrome :</strong> Paramètres → Confidentialité et sécurité → Cookies</li>
                <li><strong>Firefox :</strong> Options → Vie privée → Historique</li>
                <li><strong>Safari :</strong> Préférences → Confidentialité</li>
                <li><strong>Edge :</strong> Paramètres → Cookies et autorisations de site</li>
              </ul>

              <h3 className="font-heading text-xl font-semibold mt-6 mb-3">Pour Google</h3>
              <p className="text-zinc-600 leading-relaxed">
                Visitez <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener noreferrer" className="underline underline-offset-4 hover:text-black">les paramètres publicitaires Google</a> pour gérer la personnalisation des annonces.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Conséquences du refus des cookies</h2>
              <p className="text-zinc-600 leading-relaxed">
                Si vous choisissez de bloquer les cookies, certaines fonctionnalités du site pourraient ne pas fonctionner correctement. Le refus des cookies publicitaires n'empêchera pas l'affichage de publicités, mais celles-ci ne seront plus personnalisées.
              </p>
            </section>

            <section>
              <h2 className="font-heading text-2xl font-bold mt-8 mb-4">Contact</h2>
              <p className="text-zinc-600 leading-relaxed">
                Pour toute question concernant notre utilisation des cookies :<br />
                Email : pcarchi.contact@gmail.com
              </p>
            </section>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};
