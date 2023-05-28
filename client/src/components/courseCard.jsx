import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

export default function CourseCard(props) {
  return (
    <Card
      sx={{
        maxWidth: 345,
        padding: 2,
      }}
    >
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          Course name {props.course_code}
        </Typography>
        <Typography variant="body2" color="text.secondary" noWrap>
          Principles and techniques for developing software combined with the
          practical experience of creating a mid-size software system as a
          member of a software development team. Includes: teamwork; projects,
          planning and process; users and requirements; use cases; modeling;
          quality; software architecture; testing; GUI design, design
          principles, patterns and implementation; ethics; professionalism.
          {props.body}
        </Typography>
      </CardContent>
    </Card>
  );
}
