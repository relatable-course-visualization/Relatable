import React from 'react';

// import Course from ".././components/course";
import Header from "../components/header";
import NewSearch from '../components/newSearch';
import ReactiveCard from '../components/reactive';

import "../stylings/homepage.css";

import ClassData from '../MOCK_DATA.json';
import Reactive from '../components/reactive';


const Homepage = () =>  {

    return(
        // At line 19 change NewSearch to Reactive to see the new card
        <div className='homepage'>
            <Header/>
            <NewSearch/>
            {/* <Course courseName='CMPT370' courseDescription='Learning to build a group project' dependencies='dep-list' prerequisites='pre-list'/> */}
        </div>
    )
}

export default Homepage