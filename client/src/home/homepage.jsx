import React from 'react';

// import Course from ".././components/course";
import Header from "../components/header";
import SearchBar from '../components/searchBar';

import "../stylings/homepage.css";

import ClassData from '../MOCK_DATA.json';


const Homepage = () =>  {

    return(
        <div className='homepage'>
            <Header/>
            <SearchBar placeholder="Enter an Course..." data = {ClassData}/>
            {/* <Course courseName='CMPT370' courseDescription='Learning to build a group project' dependencies='dep-list' prerequisites='pre-list'/> */}
        </div>
    )
}

export default Homepage