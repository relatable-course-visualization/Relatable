import React, {useState, useEffect, Link} from 'react';
import '../stylings/newSearch.css'
import axios from 'axios';

import "../stylings/course.css";
import Course from './course';

function NewSearch() {
    const [loading, setLoading] = useState(false);
    const [posts, setPosts] = useState([]);
    const [searchTitle, setSearchTitle] = useState("");
  
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

    return (
      <div className="App">
        <>
          <div className='searchFilterText'>Search Filter</div>
          <div className='searchFilterTextBar'>
            <input
              type="text"
              placeholder="Search..."
              onChange={(e) => setSearchTitle(e.target.value)}
            />
          </div>
        </>
        {loading ? (
          <h4>Loading ...</h4>
        ) : (
          posts
            .filter((value) => {
              if (searchTitle === "") {
                return value;
              } else if (
                value.title.toLowerCase().includes(searchTitle.toLowerCase())
              ) {
                return value;
              }
            })
            .slice(0,1).map((item) => 
              <h5 key={item.id}>  
              <div className='wrapper'>   
                <Course body={item.description} course_code={item.course_code}/>    
              </div>   
          </h5>)
        )}
      </div>
    );
    
}

export default NewSearch;
