import React, { useState } from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

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
        '@media (max-width: 768px)': {
          height: isHovered ? 'auto' : 110,
          width: isHovered ? '100%' : 220,
        },
        transition: 'height 0.3s ease-in-out',
        height: isHovered ? 'auto' : 150,
        width: isHovered ? 750 : 450,
        backgroundColor: 'var(--clr-secondary-color)',
      }}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      className="course-card"
    >
      <CardContent className="course-card-content">
        <div className="course-title">
          <p>{props.name}</p>
        </div>
        <div noWrap={!isHovered} className="course-body">
          <p>{props.body}</p>
        </div>
        <div className="course-prerequisites">
          <p className="course-subtitle">Prerequisites:</p>
          {props.prerequisites == '[]' ? (
            <h2>No Prerequisites</h2>
          ) : (
            <span>{props.prerequisites}</span>
          )}
        </div>

        <div className="course-dependencies">
          <p className="course-subtitle">Dependencies:</p>
          {props.dependencies == '[]' ? (
            <h2>No Dependencies</h2>
          ) : (
            <span>{props.dependencies}</span>
          )}
        </div>

        <div className="course-credits">
          {props.credits == -1 ? (
            <p>Number of Credits: Not Applicable</p>
          ) : (
            <p>Number of Credits: {props.credits}</p>
          )}
        </div>

        <div className="course-restrictions">
          {props.restrictions == 'None' ? (
            <p>Restrictions: No Restrictions</p>
          ) : (
            <p>Restrictions: {props.restrictions}</p>
          )}
        </div>

        <a className="course-hyperlink" href={props.hyperlink}>
          Link To Course
        </a>
      </CardContent>
    </Card>
  );
}
