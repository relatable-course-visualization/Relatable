import React from "react";
import "../stylings/home.css";
import Footer from "../components/footer";
import AboutUs from '../components/aboutUs';

const AboutUsPage = () => {
  return (
    <div id="aboutus">
      <AboutUs />
      <Footer />
    </div>
  );
};

export default AboutUsPage;
