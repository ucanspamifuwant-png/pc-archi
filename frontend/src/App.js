import "@/index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage } from "./pages/HomePage";
import { CategoryPage } from "./pages/CategoryPage";
import { ArticlePage } from "./pages/ArticlePage";
import { Contact } from "./pages/Contact";
import { MentionsLegales } from "./pages/MentionsLegales";
import { PolitiqueConfidentialite } from "./pages/PolitiqueConfidentialite";
import { PolitiqueCookies } from "./pages/PolitiqueCookies";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/categorie/:slug" element={<CategoryPage />} />
        <Route path="/article/:slug" element={<ArticlePage />} />
        <Route path="/mentions-legales" element={<MentionsLegales />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/politique-confidentialite" element={<PolitiqueConfidentialite />} />
        <Route path="/cookies" element={<PolitiqueCookies />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
