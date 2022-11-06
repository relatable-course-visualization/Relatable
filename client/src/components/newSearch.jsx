import React, {useState, useEffect} from 'react';
import '../stylings/newSearch.css'
import axios from 'axios';

import Button from '@material-ui/core/Button'
import "../stylings/course.css";

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
          //style={{ width: "30%", height: "25px" }}
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
                <div className="course__body">{item.body}</div>
                <div className="sub">  
                    <div className="course__subboxes">Prerequisites</div>
                        <Button variant="contained">
                            {item.userId}
                        </Button>
                    </div>

                  <div className="sub"> 
                      <div className="course__subboxes">Dependencies</div>
                          <Button variant="contained">
                              {item.Id}
                          </Button>
                  </div>
              </div> 
          </h5>)
        )}
      </div>
    );
}

export default NewSearch;
