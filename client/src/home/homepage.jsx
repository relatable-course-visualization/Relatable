import React from 'react';

import NewSearch from '../components/newSearch';
import "../stylings/homepage.css";

const Homepage = () =>  {
    return(
        <div className='homepage'>
            <NewSearch/>
        </div>
    )
}

export default Homepage