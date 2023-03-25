import React from 'react';
import '../stylings/aboutUs.css';

function AboutUs() {
  return (
    <div>
      <h1 className="aboutUsHeaderText">ABOUT US</h1>
      <div className="aboutUsDiv">
        <div className="aboutUsSubDiv1">
          <div className="aboutUsImage1Div">
            <img
              src="../images/about_us_image1.jpg"
              className="aboutUsImage1"
            ></img>
          </div>
          <div className="aboutUsTextBox1">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
          </div>
        </div>

        <div className="aboutUsSubDiv2">
          <div className="aboutUsTextBox2">
            <p>
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat.
            </p>
          </div>
          <div className="aboutUsImage2Div">
            <img
              src="../images/about_us_image2.jpg"
              className="aboutUsImage2"
            ></img>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AboutUs;
