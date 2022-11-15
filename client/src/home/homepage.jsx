import React from 'react';

// import Course from ".././components/course";
import Header from "../components/header";
import NewSearch from '../components/newSearch';

import "../stylings/homepage.css";

import ClassData from '../MOCK_DATA.json';


const Homepage = () =>  {

    return(
        <div className='homepage'>
            <Header/>
            <NewSearch/>
            {/* <Course courseName='CMPT370' courseDescription='Learning to build a group project' dependencies='dep-list' prerequisites='pre-list'/> */}
        </div>
    )
}

export default Homepage