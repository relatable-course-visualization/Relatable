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

    // prerequisites buttons
    const [prerequisites, setprerequisites] = useState([]);
    const [isprerequisitesEmpty, setIsprerequisitesEmpty] = useState(false);

    var code = props.course_code.replace(" ", "");

    useEffect(() => {
        const loadDependency = (code) => {

            // list of dependencies 
            axios.get(
            `${process.env.REACT_APP_SERVER_ENDPOINT}/getDependants/${code}`
            ).then((response) => {
                
                var data = response.data;
        
                // no dependencies
                if(data == "[]"){
                    setDependencies([]); 
                    setIsDependenciesEmpty(true);
                }
                // dependencies
                else{
                    // clean up data
                    data = data.replace('[', "");
                    data = data.replace("]", "");
                    data = data.replaceAll('"', "");

                    // data is now a list
                    data = data.split(',');

                    var arrayedData = [];

                    // store jsx into an array
                    data.forEach((course) => {
                        arrayedData.push( 
                            <Button variant="contained"  onClick={(e) => courseHandler( e.currentTarget.innerText )}> 
                                <h1>{course}</h1>
                            </Button>)
                    })

                    setDependencies(arrayedData);
                    setIsDependenciesEmpty(false);
                }
            })
        }
    
        loadDependency(code);

        
        const loadPrerequisites = (code) => {

            // list of prerequisites 
            axios.get(
            `${process.env.REACT_APP_SERVER_ENDPOINT}/getPrereqs/${code}`  // Not Sure what it's called
            ).then((response) => {
                
                var data = response.data;
        
                // no prerequisites
                if(data == "[]"){
                    setprerequisites([]); 
                    setIsprerequisitesEmpty(true);
                }
                // prerequisites
                else{
                    // clean up data
                    // data = data.replace('[', "");
                    // data = data.replace("]", "");
                    // data = data.replaceAll('"', "");

                    // data is now a list
                    data = data.split(',');

                    var arrayedData = [];

                    // store jsx into an array
                    data.forEach((course) => {
                        arrayedData.push( 
                            <Button variant="contained"  onClick={(e) => courseHandler( e.currentTarget.innerText )}> 
                                <h1>{course}</h1>
                            </Button>)
                    })

                    setprerequisites(arrayedData);
                    setIsprerequisitesEmpty(false);
                }
            })
        }
    
        loadPrerequisites(code);
    }, []);


    
    return(
        <div className="wrapper">
            <div className="course">  
                <div className="course__title" >{props.course_code}</div>
                <div className="course__body">{props.body}</div>
                <div className="sub">  
                    <div className="course__subboxes">Prerequisites</div>
                            {isprerequisitesEmpty ? <h2>No Prerequisites</h2> : <h2>{prerequisites}</h2>} 
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