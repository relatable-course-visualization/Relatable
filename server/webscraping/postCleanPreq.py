import requests
import environ
import re
from courseClass import *
env = environ.Env()
environ.Env.read_env()


# This will be a 3 part file:
# 1. We need to get all courses from courseTable2023 and convert store them as dictioanries in a list
# 2. For each course dictionary we need to create a cleaned string from the raw string
    # May be helpful to also do marked_string here
# 3. We need to use PUT fn updateCourse2023 on each course


def createCourseList():
    """
    Get all courses from DB, make each of them a dictionary, and store and return them in a list
    :return A complete list of course dictionaries
    """
    allCourses = requests.get(f"{env('SERVER_URL')}/getAllCourses2023")
    allCourses = allCourses.json()

    courseList = []
    # May be redundant if .json() returns a list
    for course in allCourses:
        courseList.append(course)

    return courseList