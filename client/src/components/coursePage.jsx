import React, { useState } from 'react';
import CourseCard from './courseCard';
import '../stylings/coursePage.css';

const courses = [];

function CoursePage() {
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

export default CoursePage;
