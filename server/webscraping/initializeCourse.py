from courseClass import *
from courseScraper import *
import requests

""" Initialize the course table in the database by capturing 
    all cleaned Course objects and POSTing them into the database
"""
def initializeCourseTable():
    list_of_courses = courseScraper()
    for course in list_of_courses:
        course_object = {'course_code': str(course.getCode()), 'name': str(course.getName()), 'description': str(course.getDescription())
        , 'restrictions': str(course.getRestriction()), 'hyperlink': str(course.getLink()), 'num_credits': '0'}

        requests.post("http://127.0.0.1:8000/postCourse", data=course_object)

initializeCourseTable()
