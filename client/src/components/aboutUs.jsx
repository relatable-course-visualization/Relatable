import React from 'react';
import '../stylings/aboutUs.css';

function AboutUs() {
  return (
    <div className='aboutUsStyling'>
      <h1 className='aboutUsHeader'>Reinventing the USask course catalogue. For students, by students.</h1>
      <div className='aboutUsRowContainer'>
        <div className='aboutUsText'>
          <p>
          Relatable was born out of the recognition for a better and smoother way 
          to browse for classes. What started as a class project for CMPT 370 has 
          evolved into a powerful platform designed to enhance the educational journey 
          for students. 
          </p>
          <p>
            At Relatable, our primary goal is to simplify the process of 
            exploring and selecting courses. We understand the frustration of navigating 
            complex course structures and deciphering prerequisites. That's why we've 
            developed a platform that allows students to directly see dependent courses, 
            easily access related courses, and presents prerequisites in a clear format.
          </p>
        </div>
        <img className='relatableFoundersImages'
          src="../images/about_us_image1.jpg"
        ></img>
      </div>

      <div className='aboutUsRowContainer'>
        <img className='relatableFoundersImages'
          src="../images/about_us_image2.jpg"
        ></img>
        <div className='aboutUsText'>
          <p>
            We're excited to present the first version of Relatable, but we're not stopping 
            there. We value your feedback and ideas as we continue to improve and expand 
            our services. Please don't hesitate to reach out to us at relatable@gmail.com 
            with any suggestions, feedback, or ideas you may have.
          </p>
          {/* <p>
            Join us on this journey of making the education experience more enjoyable, 
            accessible, and relatable for students everywhere.
          </p> */}
        </div>
      </div>
    </div>
  );
}

export default AboutUs;
