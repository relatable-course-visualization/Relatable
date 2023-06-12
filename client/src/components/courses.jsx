import React, { useState } from 'react';
import CourseCard from './courseCard';
import '../stylings/courses.css';

const courses = [];

function Courses() {
  return (
    <div className="coursepage-div">
      <div className="courses-div">
        {courses.map((course, index) => (
          <div key={index}>
            <CourseCard props={course} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Courses;
