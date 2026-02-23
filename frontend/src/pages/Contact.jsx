import React from "react";

export function Contact() {
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "40px 20px" }}>
      <h1>Contact</h1>
      <p>
        Une question, une suggestion ou une correction ? Vous pouvez nous écrire :
      </p>
      <p>
        <strong>Email :</strong>{" "}
        <a href="mailto:pcarchi.contact@gmail.com">pcarchi.contact@gmail.com</a>
      </p>
      <p>
        Nous répondons généralement sous quelques jours ouvrés.
      </p>
    </main>
  );
}
