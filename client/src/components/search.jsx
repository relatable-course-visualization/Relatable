import React, { useState, useEffect } from "react";
import "../stylings/search.css";
import axios from "axios";

import "../stylings/course.css";
import Course from "./course";
import { Button, Typography } from "@material-ui/core";
import TextField from "@mui/material/TextField";
import { makeStyles } from "@material-ui/core/styles";
import CourseCard from "./courseCard";

const useStyles = makeStyles({
  searchButton: {
    textTransform: "none",
    fontFamily: "var(font-family)",
    fontSize: "var(--fs-4)",
    fontWeight: "var(--fw-reg)",
    "& .MuiButton-label": {
      whiteSpace: "nowrap", // prevents text going into multiple lines
    },
    backgroundColor: "var(--clr-primary-color)",
    "&:hover": {
      backgroundColor: "var(--clr-primary-color)",
    },
  },

  searchTitle: {
    fontSize: "var(--fs-4)",
    color: "pink",

    "@media (max-width: 400px)": {
      fontSize: "var(--fs-5)",
      color: "red",
    },
  },
});

function Search() {
  const classes = useStyles();

  const [loading, setLoading] = useState(false);
  const [posts, setPosts] = useState([]);
  const [searchTitle, setSearchTitle] = useState("");
  const [numShown, setNumShown] = useState(10);

  var numFiltered = 0;

  const setNumFiltered = () => {
    numFiltered += 1;
  };

  useEffect(() => {
    const loadPosts = async () => {
      setLoading(true);
      const response = await axios.get(
        `${process.env.REACT_APP_SERVER_ENDPOINT}/getAllCourses2023`
      );
      setPosts(response.data);
      setLoading(false);
    };

    loadPosts();
  }, []);

  const morePosts = () => {
    setNumShown(numShown + 10);
    console.log(numShown);
  };

  const searchHandler = (courseName) => {
    setSearchTitle(courseName);
  };

  return (
    <div id="search">
      <>
        <Typography id="searchTitle">Search Courses</Typography>

        <TextField
          id="outlined-basic"
          label="E.g., CMPT 370"
          variant="outlined"
          color="primary"
          onChange={(e) => {
            setSearchTitle(e.target.value);
            setNumShown(10);
          }}
          value={searchTitle}
          className="searchTextField"
        />
      </>
      {loading ? (
        <h1 id="searchLoading">Loading ...</h1>
      ) : (
        posts
          .filter((value) => {
            if (searchTitle === "") {
              return;
            } else if (
              value.course_code
                .toLowerCase()
                .includes(searchTitle.toLowerCase())
            ) {
              setNumFiltered();
              return value;
            }
          })
          .slice(0, numShown)
          .map((item) => (
            <div
              className="wrapper"
              key={item.id}
              style={{ justifyItems: "center" }}
            >
              <CourseCard
                name={item.name}
                body={item.description}
                prerequisites={item.marked_preq}
                dependencies={item.dependent_courses}
                credits={item.num_credits}
                restrictions={item.restrictions}
                course_code={item.course_code}
                hyperlink={item.hyperlink}
                not_in_catalogue={item.not_in_catalogue}
                searchHandler={searchHandler}
              />
            </div>
          ))
      )}

      {numFiltered <= numShown ? (
        <></>
      ) : (
        <div id="searchButtonContainer">
          <Button
            variant="contained"
            className={classes.searchButton}
            onClick={(e) => morePosts()}
          >
            Show More
          </Button>
        </div>
      )}
    </div>
  );
}

export default Search;
