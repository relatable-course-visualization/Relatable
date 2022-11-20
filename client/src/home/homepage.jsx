import React from 'react';

import Header from "../components/header";
import NewSearch from '../components/newSearch';
import "../stylings/homepage.css";

const Homepage = () =>  {
    return(
        <div className='homepage'>
            <Header/>
            <NewSearch/>
        </div>
    )
}

export default Homepage