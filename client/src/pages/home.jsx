import React from "react";
import "../stylings/home.css";
import Footer from "../components/footer";
import Search from "../components/search";
import Navbar from "../components/navbar"

const Home = () => {
  return (
    <div className="homepage">
      <Navbar />
      <Search />
      <Footer />
    </div>
  );
};

export default Home;
