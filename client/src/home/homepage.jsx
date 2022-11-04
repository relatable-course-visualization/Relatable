import React from 'react';

import Course from ".././components/course";
import Header from "../components/header";

const Homepage = () =>  {
    return(
        <div className='container'>
            <Header/>
            <Course courseName='CMPT370' courseDescription='Learning to build a group project' dependencies='dep-list' prerequisites='pre-list'/>
        </div>
    )
}

export default Homepage