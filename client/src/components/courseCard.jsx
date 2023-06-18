import React, { useState } from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";

export default function CourseCard(props) {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  return (
    <Card
      sx={{
        "@media (max-width: 768px)": {
          height: isHovered ? "auto" : 110,
          width: isHovered ? "100%" : 220,
        },
        transition: "height 0.3s ease-in-out",
        height: isHovered ? "auto" : 150,
        width: isHovered ? 750 : 450,
        backgroundColor: "var(--clr-secondary-color)",
      }}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      className="course-card"
    >
      {!props.not_in_catalogue ? (
        <CardContent className="course-card-content">
          <div className="course-title">
            <p>{props.course_code}</p>
          </div>
          <div className="course-title">
            <p>{props.name}</p>
          </div>
          <div noWrap={!isHovered}>
            <p>{props.body}</p>
          </div>
          <div>
            {props.prerequisites === "None" ? (
              <p>
                <u>Prerequisites</u>: No Prerequisites
              </p>
            ) : (
              <p>
                <u>Prerequisites</u>: {props.prerequisites}
              </p>
            )}
          </div>

          <div>
            {props.dependencies === null ? (
              <p>
                <u>Dependencies</u>: No Dependencies
              </p>
            ) : (
              <p>
                <u>Dependencies</u>: {props.dependencies}
              </p>
            )}
          </div>

          <div>
            {props.credits == -1 ? (
              <p>Number of Credits: Not Applicable</p>
            ) : (
              <p>Number of Credits: {props.credits}</p>
            )}
          </div>

          <div>
            {props.restrictions == "None" ? (
              <p>Restrictions: No Restrictions</p>
            ) : (
              <p>Restrictions: {props.restrictions}</p>
            )}
          </div>

          <a
            className="course-hyperlink"
            href={props.hyperlink}
            target="_blank"
            rel="noreferrer"
          >
            Link To Course
          </a>
        </CardContent>
      ) : (
        <>Not in-Catalogue</>
      )}
    </Card>
  );
}
