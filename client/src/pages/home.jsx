import React from "react";
import "../stylings/home.css";
import Footer from "../components/footer";
import Search from "../components/search";

const Home = () => {
  return (
    <div className="homepage">
      <Search />
      <Footer />
    </div>
  );
};

export default Home;
