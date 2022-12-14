from courseClass import *
from courseScraper import *
import requests

""" Initialize the course table in the database by capturing 
    all cleaned Course objects and POSTing them into the database
"""
def updateCourseTable():
    list_of_courses = courseScraper()
    for course in list_of_courses:
        # checking for no credits
        try:
            course_object = {'course_code': str(course.getCode()), 'name': str(course.getName()), 'description': str(course.getDescription())
        , 'restrictions': str(course.getRestriction()), 'hyperlink': str(course.getLink()), 'num_credits': int(course.getCredit())}
        except ValueError:
            course_object = {'course_code': str(course.getCode()), 'name': str(course.getName()), 'description': str(course.getDescription())
        , 'restrictions': str(course.getRestriction()), 'hyperlink': str(course.getLink()), 'num_credits': -1}

        requests.put("http://127.0.0.1:8000/updateCourse", data=course_object)

updateCourseTable()
