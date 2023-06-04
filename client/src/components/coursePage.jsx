import React, { useState } from 'react';
import CourseCard from './courseCard';
import '../stylings/courseCard.css';

const courses = [
  {
    name: 'CMPT 370',
    body: 'Principles and techniques for developing software combined with the practical experience of creating a mid-size software system as a member of a software development team. Includes: teamwork; projects, planning and process; users and requirements; use cases; modeling; quality; software architecture; testing; GUI design, design principles, patterns and implementation; ethics; professionalism. Prerequisite(s): CMPT 280',
  },
  {
    name: 'CMPT 370',
    body: 'Principles and techniques for developing software combined with the practical experience of creating a mid-size software system as a member of a software development team. Includes: teamwork; projects, planning and process; users and requirements; use cases; modeling; quality; software architecture; testing; GUI design, design principles, patterns and implementation; ethics; professionalism. Prerequisite(s): CMPT 280',
  },
  {
    name: 'CMPT 370',
    body: 'Principles and techniques for developing software combined with the practical experience of creating a mid-size software system as a member of a software development team. Includes: teamwork; projects, planning and process; users and requirements; use cases; modeling; quality; software architecture; testing; GUI design, design principles, patterns and implementation; ethics; professionalism. Prerequisite(s): CMPT 280',
  },
  {
    name: 'CMPT 370',
    body: 'Principles and techniques for developing software combined with the practical experience of creating a mid-size software system as a member of a software development team. Includes: teamwork; projects, planning and process; users and requirements; use cases; modeling; quality; software architecture; testing; GUI design, design principles, patterns and implementation; ethics; professionalism. Prerequisite(s): CMPT 280',
  },
];

function NewCourse() {
  return (
    <div className="courses-div">
      {courses.map((course, index) => (
        <div key={index}>
          <CourseCard props={course} />
        </div>
      ))}
    </div>
  );
}

export default NewCourse;
