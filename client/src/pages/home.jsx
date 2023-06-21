import React from "react";
import "../stylings/home.css";
import Footer from "../components/footer";
import Search from "../components/search";

const Home = () => {
  return (
    <div id="home">
      <Search />
      <Footer />
    </div>
  );
};

export default Home;
