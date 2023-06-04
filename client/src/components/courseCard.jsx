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
      }}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      className="course-card"
    >
      <CardContent className="course-card-content">
        <div className="course-title">
          <p>Course name {props.name}</p>
        </div>
        <div noWrap={!isHovered} className="course-body">
          <p>
            Principles and techniques for developing software combined with the
            practical experience of creating a mid-size software system as a
            member of a software development team. Includes: teamwork; projects,
            planning and process; users and requirements; use cases; modeling;
            quality; software architecture; testing; GUI design, design
            principles, patterns and implementation; ethics; professionalism.
            {props.body}
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
