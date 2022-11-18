import React, {useState, useEffect} from "react";
import Button from '@material-ui/core/Button'
import "../stylings/course.css";
import axios from 'axios';

const Course = (props) => {
    
    const [course] = useState("");
    const courseHandler =()=>{
        return {course}
    }

    const [dependencies, setDependencies] = useState([]);
    const [isDependenciesEmpty, setIsDependenciesEmpty] = useState(false);

    var code = props.course_code.replace(" ", "");

    useEffect(() => {
        const loadDependency = (code) => {

            // list of dependencies 
            axios.get(
            `${process.env.REACT_APP_SERVER_ENDPOINT}/getDependants/${code}`
            ).then((response) => {
                
                var data = response.data;
            })
        }
    
        loadDependency(code);
    }, []);
    
    return(
        <div className="wrapper">
            <div className="course">  
                <div className="course__title" >{props.course_code}</div>
                <div className="course__body">{props.body}</div>
                <div className="sub">  
                    <div className="course__subboxes">Prerequisites</div>
                        <Button variant="contained" onClick={(e) => courseHandler(e.target.value)}>
                            {props.title}
                        </Button>
                    </div>

                <div className="sub"> 
                    <div className="course__subboxes">Dependencies</div>
                            {isDependenciesEmpty ? <h2>No Dependencies</h2> : <h2>{dependencies}</h2>}        
                </div>
                <div className="sub">Placeholder for Restrictions </div>
                    <div className="course_body" >
                      <a href="Placeholder for hyperlink">
                        Link To Course
                      </a>
                    </div>
            </div>  
        </div>           
    )
}

export default Course;