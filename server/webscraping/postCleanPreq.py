import requests
import environ
import re
from courseClass import *
from formConversion.formClass import *


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

def createCleanPreq(raw_preq: str):
    """
    Given a a courses raw_preq, return its clean_preq
    :return clean_preq - cleaned string that makes all the course_codes explicit
    """
    form = Form(raw_preq)
    clean_preq = form.formalizeCourseNames()
    return clean_preq


# The following lines update each course in courseTable2023, adding in new entry for 'clean_preq' column
courseList = createCourseList()
for course in courseList:
    if course['raw_preq'] is not None:
        course['clean_preq'] = createCleanPreq(course['raw_preq'])
    else:
        course['clean_preq'] = ''
    requests.put(f"{env('SERVER_URL')}/updateCourse2023", data=course)
