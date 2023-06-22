import React from "react";
import "../stylings/home.css";
import Footer from "../components/footer";
import AboutUs from '../components/aboutUs';

// import AboutUs from "../components/aboutUsV2";
const AboutUsPage = () => {
  return (
    <div id="aboutUsPage">
      <AboutUs />
      {/* <Footer /> */}
    </div>

  );
};

export default AboutUsPage;
