import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import NewSearch from "../components/newSearch";
import "../stylings/homepage.css";

const Homepage = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<NewSearch />} />
        {/* <Route path="/about-us" element={<AboutUs />} />
        <Route path="/contact-us" element={<Contact />} /> */}
      </Routes>
    </BrowserRouter>
  );
};

export default Homepage;
