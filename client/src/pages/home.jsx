import React from "react";
import NewSearch from "../components/newSearch";
import "../stylings/home.css";
import Footer from "../components/footer";

const Home = () => {
  return (
    <div id="home">
      <NewSearch />
      <Footer />
    </div>
  );
};

export default Home;
