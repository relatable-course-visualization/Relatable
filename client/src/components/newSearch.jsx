import React, {useState, useEffect, Link} from 'react';
import '../stylings/newSearch.css'
import axios from 'axios';

import Button from '@material-ui/core/Button'
import "../stylings/course.css";
import CloseIcon from '@mui/icons-material/Close';
import { useRef } from 'react';

function NewSearch() {
    const [loading, setLoading] = useState(false);
    const [posts, setPosts] = useState([]);
    const [searchTitle, setSearchTitle] = useState("");
  
    useEffect(() => {
      const loadPosts = async () => {
        setLoading(true);
        const response = await axios.get(
          "https://jsonplaceholder.typicode.com/posts"
        );
        setPosts(response.data);
        setLoading(false);
      };
  
      loadPosts();
    }, []);

    return (
      <div className="App">
        <h3>Search Filter</h3>
        <input
          type="text"
          placeholder="Search..."
          onChange={(e) => setSearchTitle(e.target.value)}
        />
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
            .slice(0,15).map((item) => 
              <h5 key={item.id}>            
                <div className="course">  
                  <div className="course__title" >{item.title}</div>
                  {/* <div className="course__body" >Placeholder for course code</div>
                  <div className="course__title" >Placeholder for number of credits</div> */}
                  <div className="course__body">{item.body}</div>
                  <div className="sub">  
                      <div className="course__subboxes">Prerequisites</div>
                          <Button variant="contained" onClick={(e) => setSearchTitle( e.currentTarget.innerText )}>
                              {item.title}
                          </Button>
                      </div>

                    <div className="sub"> 
                        <div className="course__subboxes">Dependencies</div>
                            <Button variant="contained" onClick={(e) => setSearchTitle( e.currentTarget.innerText )}>
                                {item.id}
                            </Button>
                    </div>
                    <div className="sub">Placeholder for Restrictions </div>
                    <div className="course_body" >
                      <a href="Placeholder for hyperlink">
                        Link To Course
                      </a>
                    </div>
              </div> 
          </h5>)
        )}
      </div>
    );
}

export default NewSearch;
