import "./App.css";
import Home from "./pages/home";
import AboutUsPage from "./pages/aboutUsPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from "react";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about-us" element={<AboutUsPage />} />
        {/* <Route path="/contact-us" element={<Contact />} /> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
