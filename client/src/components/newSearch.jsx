import React, {useState, useEffect, Link} from 'react';
import '../stylings/newSearch.css'
import axios from 'axios';

import "../stylings/course.css";
import Course from './course';
import { Button } from '@material-ui/core';

function NewSearch() {
    const [loading, setLoading] = useState(false);
    const [posts, setPosts] = useState([]);
    const [searchTitle, setSearchTitle] = useState("");
    const [numShown, setNumShown] = useState(10);
    //const [numFiltered, setNumFiltered] = useState(0);

    // var numShown = 10;

    // const setNumShown = (num) => {
    //   numShown = num;
    // }

    var numFiltered = 0;

    const setNumFiltered = () => {
      numFiltered+=1;
    }
  
    useEffect(() => {
      const loadPosts = async () => {
        setLoading(true);
        const response = await axios.get(
          `${process.env.REACT_APP_SERVER_ENDPOINT}/courses`
          
        );
        setPosts(response.data);
        setLoading(false);
      };
  
      loadPosts();
    }, []);

    const morePosts = () => {
      setNumShown(numShown + 10);
      console.log(numShown);
    }

    const searchHandler = (courseName) => {
      setSearchTitle(courseName);
    }

    return (
      <div className="App">
        <>
          <div className='searchFilterText'>Search Filter</div>
          <div className='searchFilterTextBar'>
            <input
              type="text"
              placeholder="Search..."
              onChange={(e) => {setSearchTitle(e.target.value); setNumShown(10)}}
              value={searchTitle}
            />
          </div>
        </>
        {loading ? (
          <h4>Loading ...</h4>
        ) : (
          posts
            .filter((value) => {
              if (searchTitle === "") {
                return;
              } else if (value.course_code.toLowerCase().includes(searchTitle.toLowerCase())) {
                setNumFiltered();
                return value;
              }
            })
            .slice(0, numShown).map((item) => 
              <h5 key={item.id}>  
                <div className='wrapper'>   
                  <Course body={item.description} course_code={item.course_code} searchHandler={searchHandler}/>    
                </div>   
              </h5>
            )
        )}
        
        {numFiltered <= numShown ? <></> : <Button variant="contained"  onClick={(e) => morePosts()}> 
           Show More
        </Button>}
      </div>
    );
    
}

export default NewSearch;
