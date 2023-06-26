import React from "react";
import "../stylings/aboutUsPage.css"
import Footer from "../components/footer";
import AboutUs from '../components/aboutUs';

const AboutUsPage = () => {
  return (
    <div id="aboutUsPage">
      <div id="content-wrap">
        <AboutUs/>
        {/* <Footer/> */}
      </div>
      <Footer/>
    </div>

  );
};

export default AboutUsPage;
