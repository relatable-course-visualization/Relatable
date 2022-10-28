import React from "react";


import './App.css';

import homepage from "./home/homepage";
import Course from "./components/course";

import pic from "./images/RelatableIcon.png";
import Search from "./components/searchBar";

import Header from "./components/Header";



//<input type="text" placeholder="Search..."/>
//<Course aCourse='CMPT370' aCourseDesctiption='learning to build a group project'/>
// function App() {
//   return (
//     <>
//       {/* <img src = {pic} className="App-pic" alt="pic" />
//       <Search/> */}
//     </>
//   );
// }

const App = () => {
  return (
    <div className='container'>
      <Header/>
    </div>
  );
}

export default App;
