import React from "react";


import './App.css';

import homepage from "./home/homepage";
import Course from "./components/course";

import pic from "./images/Anoures.jpg";
import Search from "./components/searchBar";



//<input type="text" placeholder="Search..."/>
//<Course aCourse='CMPT370' aCourseDesctiption='learning to build a group project'/>
function App() {
  return (
    <>
      <img src = {pic} className="App-pic" alt="pic" />
      <Search/>
    </>
  );
}

export default App;
