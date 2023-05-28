import React, { useState } from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

export default function CourseCard() {
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
        maxWidth: 345,
        height: isHovered ? 'auto' : 150,
        transition: 'height 0.3s ease-in-out',
      }}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      className="course-card"
    >
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          Course name
        </Typography>
        <Typography variant="body2" color="text.secondary" noWrap={!isHovered}>
          Principles and techniques for developing software combined with the
          practical experience of creating a mid-size software system as a
          member of a software development team. Includes: teamwork; projects,
          planning and process; users and requirements; use cases; modeling;
          quality; software architecture; testing; GUI design, design
          principles, patterns and implementation; ethics; professionalism.
        </Typography>
      </CardContent>
    </Card>
  );
}
