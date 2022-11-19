from courseClass import *
from courseScraper import *
import requests

""" Initialize the course table in the database by capturing 
    all cleaned Course objects and POSTing them into the database
"""
def updateCourseTable():
    # list_of_courses = courseScraper()
    # for course in list_of_courses:
    #     course_object = {'course_code': str(course.getCode()), 'num_credits': int(course.getCredit())}

    #     requests.put("http://127.0.0.1:8000/updateCourse", data=course_object)

    # For testing:
    course_object = {'course_code': "ACB 221", 'num_credits': 100}
    requests.put("http://127.0.0.1:8000/updateCourse", data=course_object)

updateCourseTable()
