import React from "react";
import Box from '@mui/material/Box';
import Button from '@material-ui/core/Button'
import "../stylings/course.css";
import { Paper } from "@mui/material";
import { blue } from "@mui/material/colors";


const Course = (props) => {
    console.log(props);
    return(
            <div className="course">  
                <div className="course__title" >{props.courseName}</div>
                <div className="course__body">{props.courseDescription}</div>
                <Paper style={{background: blue}}>
                    <div className="course__prerequisites">Prerequisites</div>
                    <p>
                        <Button variant="contained">
                            {props.prerequisites}
                        </Button>
                        
                        <Button variant="contained">
                            280
                        </Button>

                        <Button variant="contained">
                            270
                        </Button>
                    </p>
                </Paper>

                <Paper className="paper__colour">
                    <div className="course__dependencies">dependencies</div>
                    <p>
                        <Button variant="contained">
                            {props.dependencies}
                        </Button>
                        
                        <Button variant="contained">
                            410
                        </Button>

                        <Button variant="contained">
                            440
                        </Button>
                    </p>
                </Paper>
                </div>             

    )
}

export default Course;