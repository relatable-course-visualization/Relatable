import React from "react";
import "../stylings/home.css";
import Footer from "../components/footer";
import AboutUs from '../components/aboutUs';

const AboutUsPage = () => {
  return (
    <div id="aboutUsPage">
      <AboutUs />
      {/* Add footer back in later - will need to do some more work to 
      have it properly formated */}
      {/* <Footer /> */}
    </div>

  );
};

export default AboutUsPage;
