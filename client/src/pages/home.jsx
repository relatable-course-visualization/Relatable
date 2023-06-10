import React from 'react';
import '../stylings/home.css';
import Footer from '../components/footer';
import Search from '../components/search';
import CoursePage from '../components/coursePage';

const Home = () => {
  return (
    <div id="home">
      <Search />
      <div>
        <CoursePage />
      </div>
      <div>
        <Footer />
      </div>
    </div>
  );
};

export default Home;
