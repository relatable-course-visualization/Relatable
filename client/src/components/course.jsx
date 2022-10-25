import React from "react";

const Course = (props) => {
    console.log(props);

    return(
        <div>
            <h2>{props.aCourse} </h2>
            <p>{props.aCourseDesctiption}</p>
        </div>
    )

}

export default Course;