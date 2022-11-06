import React from "react";
import Button from '@material-ui/core/Button'
import "../stylings/course.css";


const Course = (props) => {
    console.log(props);
    return(
            <div className="course">  
                <div className="course__title" >{props.courseName}</div>
                <div className="course__body">{props.courseDescription}</div>
                <div className="sub">  
                    <div className="course__subboxes">Prerequisites</div>
                        <Button variant="contained">
                            {props.prerequisites}
                        </Button>
                        
                        <Button variant="contained">
                            280
                        </Button>

                        <Button variant="contained">
                            270
                        </Button>
                    </div>

                <div className="sub"> 
                    <div className="course__subboxes">Dependencies</div>
                        <Button variant="contained">
                            {props.dependencies}
                        </Button>
                        
                        <Button variant="contained">
                            410
                        </Button>

                        <Button variant="contained">
                            440
                        </Button>
                </div>
            </div>             
    )
}

export default Course;