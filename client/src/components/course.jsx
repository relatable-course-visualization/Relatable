import React, {useState, useEffect} from "react";
import Button from '@material-ui/core/Button'
import "../stylings/course.css";
import axios from 'axios';

const Course = (props) => {
    
    const courseHandler = (course) =>{
       props.searchHandler(course);
    }

    const [dependencies, setDependencies] = useState([]);
    const [isDependenciesEmpty, setIsDependenciesEmpty] = useState(false);

    // prerequisites buttons
    const [prerequisites, setPrerequisites] = useState([]);
    const [isPrerequisitesEmpty, setIsPrerequisitesEmpty] = useState(false);

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
                            <Button variant="contained" size="small" sx={{m: 30}} onClick={(e) => courseHandler( e.currentTarget.innerText )}> 
                                <h5>{course}</h5>
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
            `${process.env.REACT_APP_SERVER_ENDPOINT}/getPrereqs/${code}`
            ).then((response) => {
                
                var data = response.data
        
                // no prerequisites
                if(data == "[]"){
                    setPrerequisites([]); 
                    setIsPrerequisitesEmpty(true);
                }
                // prerequisites
                else{
                    // clean up data
                    data = data.replace('[', "");
                    data = data.slice(0, -1);
                    
                    /* Iterate through disjunctions */
                    var leftBracketIndex = 0;
                    var rightBracketIndex = 0;
                    var arrayedData = [];
                    while(leftBracketIndex < data.length){
                        // find closing bracket for inner list 
                        while(data[rightBracketIndex] != ']'){
                            rightBracketIndex++;
                        }

                        /* obtain inner list */

                        // if item has a comma it means an OR
                        var subdata = data.substring(leftBracketIndex+1, rightBracketIndex)
                        if(subdata.includes(",")){
                            // subdata is a list of courses inside an inner list (disjunction)
                            subdata = subdata.split(",")
                            
                            // add opening bracket
                            arrayedData.push(
                                <h2 className="dynamic-text">{"( "}</h2>
                            );

                            // store jsx into an array
                            subdata.forEach((course, i,) => {
                                course = course.replaceAll('"', "");
                                arrayedData.push( 
                                    <Button variant="contained" size="small" onClick={(e) => courseHandler( e.currentTarget.innerText )}> 
                                        <h5>{course}</h5>
                                    </Button>);
                                if(i != subdata.length -1){
                                    arrayedData.push(<h2 className="dynamic-text"> OR </h2>)
                                }
                            })
                            // add closing bracket
                            arrayedData.push(
                                <h2 className="dynamic-text">{")"}</h2>
                            );
                        }
  
                        // Only one item
                        else{ 
                            subdata = subdata.replaceAll('"', "");
                            arrayedData.push(
                                <Button variant="contained" size="small" onClick={(e) => courseHandler( e.currentTarget.innerText )}> 
                                    <h5>{subdata}</h5>
                                </Button>
                            )}

                        /* insert AND if disjunctions continue */

                        leftBracketIndex = rightBracketIndex + 1;
                        // not out of bounds 
                        if (data[leftBracketIndex] !== undefined && leftBracketIndex < data.length) {
                            // another disjunction 
                            if (data[leftBracketIndex] === ","){
                                // make AND tag in course prerequisite section
                                arrayedData.push(<h2 className="dynamic-text"> AND </h2>)

                                // update both indicies
                                leftBracketIndex += 2;
                                rightBracketIndex += 2; 
                            }
                        }
                    }

                    // update state variables
                    setPrerequisites(arrayedData);
                    setIsPrerequisitesEmpty(false);
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
                            {isPrerequisitesEmpty ? <h2 className="dynamic-text">No Prerequisites</h2> : <div className="rowPrerequisites">{prerequisites}</div>} 
                    </div>

                <div className="sub"> 
                    <div className="course__subboxes">Dependencies</div>
                            {isDependenciesEmpty ? <h2 className="dynamic-text">No Dependencies</h2> : <h2>{dependencies}</h2>}        
                </div>
                <div className="course__credits">Number of Credits</div>
                    {credits == -1 ? <h2>Not Applicable</h2> : <h2>{credits}</h2>}
                <div className="course__restrictions">Restrictions</div>
                    {restrictions == None ? <h2>No Restrictions</h2> : <h2>{restrictions}</h2>}
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