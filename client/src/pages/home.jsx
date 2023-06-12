import React from 'react';
import '../stylings/home.css';
import Footer from '../components/footer';
import Search from '../components/search';
import Courses from '../components/courses';

const Home = () => {
  return (
    <div id="home">
      <Search />
      <div>
        <Courses />
      </div>
      <div>
        <Footer />
      </div>
    </div>
  );
};

export default Home;
