import React from 'react';
import '../stylings/home.css';
import Footer from '../components/footer';
import Search from '../components/search';
import Courses from '../components/courses';
import Navbar from '../components/navbar';

const Home = () => {
  return (
    <div id="home">
      <Navbar />
      <Search />
      <Courses />
      <Footer />
    </div>
  );
};

export default Home;
