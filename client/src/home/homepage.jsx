import React from 'react';
//import Search from ".././components/searchBar";
//import pic from ".././images/Anoures.jpg";

import Search from '../components/searchBar';
import pic from "../images/Anoures.jpg";

const homepage = () =>  {
    return(
        <>
            <img src = {pic} className="App-pic" alt="pic" />
            <Search/>
        </>
    )
}

export default homepage