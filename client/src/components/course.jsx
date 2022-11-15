import React, {useState} from "react";
import Button from '@material-ui/core/Button'
import "../stylings/course.css";
import NewSearch from "./newSearch";


const Course = (props) => {
    
    const [course] = useState("");
    const courseHandler =()=>{
        return {course}
    }

    console.log(props);
    return(
        <div className="wrapper">
            <div className="course">  
                <div className="course__title" >{props.title}</div>
                <div className="course__body">{props.body}</div>
                <div className="sub">  
                    <div className="course__subboxes">Prerequisites</div>
                        <Button variant="contained" onClick={(e) => courseHandler(e.target.value)}>
                            {props.title}
                        </Button>
                    </div>

                <div className="sub"> 
                    <div className="course__subboxes">Dependencies</div>
                        <Button variant="contained"  onClick={(e) => courseHandler( e.currentTarget.innerText )}>
                            {props.id}
                        </Button>
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