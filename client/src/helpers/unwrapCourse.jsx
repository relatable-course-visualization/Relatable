import { Button, Typography } from "@mui/material";
import React from "react";

const COURSE_CODE_PATTERN = /([A-Z]{2,4}\s[0-9]{3})/g;
const START_MARKER_PATTERN = /\$\[/g;
const END_MARKER_PATTERN = /\]\$/g;

/**
 * Replaces course codes with searchable buttons, and remove the markings
 *
 * @param {course} marked string representing prerequisites or dependencies
 * @param {courseHandler} courseHandler function used to search for a course when clicked on it
 * @returns an unmarked string representing prerequisites or dependencies, where courses are replaced
 *        with re-searchable buttons
 */
export function unwrapCourse(course, courseHandler) {
  // create an array from the string, where where even-numbered elements are non-course code parts,
  // and odd-numbered elements are course codes
  const parts = course.split(COURSE_CODE_PATTERN);

  return parts.map((part, index) => {
    if (index % 2 === 1) {
      // Wrap course code with searchable button
      return (
        <React.Fragment key={index}>
          <Button
            style={{
              color: "black",
              borderColor: "#F9F5F6",
              borderRadius: "13px",
              borderWidth: "3px",
              marginLeft: "5px",
              marginRight: "5px",
              marginBottom: "5px",
              padding: "4px",
              boxShadow: "var(--bs)",
            }}
            variant="outlined"
            size="small"
            onClick={() => courseHandler(part)}
          >
            {part}
          </Button>
        </React.Fragment>
      );
    } else {
      return (
        // Remove markings
        <React.Fragment key={index}>
          {part
            .replace(START_MARKER_PATTERN, "")
            .replace(END_MARKER_PATTERN, "")}
        </React.Fragment>
      );
    }
  });
}
