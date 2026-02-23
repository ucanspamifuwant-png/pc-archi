import React from "react";

export function MentionsLegales() {
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "40px 20px" }}>
      <h1>Mentions légales</h1>

      <h2>Éditeur du site</h2>
      <p>
        Nom du site : PC-ARCHI
        <br />
        Responsable de publication : PC Archi
        <br />
        Contact :{" "}
        <a href="mailto:pcarchi.contact@gmail.com">pcarchi.contact@gmail.com</a>
      </p>

      <h2>Hébergement</h2>
      <p>
        Vercel Inc.
        <br />
        340 S Lemon Ave #4133
        <br />
        Walnut, CA 91789
        <br />
        États-Unis
      </p>

      <h2>Affiliation</h2>
      <p>
        Certains liens présents sur ce site peuvent être des liens d’affiliation.
        Une commission peut être perçue si vous effectuez un achat via ces liens,
        sans coût supplémentaire pour vous.
      </p>

      <h2>Publicité</h2>
      <p>
        Ce site peut afficher des publicités via Google AdSense. Des cookies ou
        identifiants publicitaires peuvent être utilisés, selon votre consentement.
      </p>
    </main>
  );
}
