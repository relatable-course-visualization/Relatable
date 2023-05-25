from courseClass import *
from courseScraper import *
import requests
import environ

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()

""" Initialize the course table in the database by capturing 
    all cleaned Course objects and POSTing them into the database
"""
def initializeCourseTable():
    list_of_courses = courseScraper()
    i = 0
    for course in list_of_courses:
        try:
            course_object = {'course_code': str(course.getCode()), 'name': str(course.getName()), 'description': str(course.getDescription())
            , 'restrictions': str(course.getRestriction()), 'hyperlink': str(course.getLink()), 'num_credits': int(course.getCredit()),
            'raw_preq': course_object.getPrerequisite(), 'clean_preq': '', 'marked_preq': '', 'dependent_courses': ''}
        except ValueError:
            course_object = {'course_code': str(course.getCode()), 'name': str(course.getName()), 'description': str(course.getDescription())
            , 'restrictions': str(course.getRestriction()), 'hyperlink': str(course.getLink()), 'num_credits': -1, 
            'raw_preq': course_object.getPrerequisite(), 'clean_preq': '', 'marked_preq': '', 'dependent_courses': ''}

        requests.post(f"{env('SERVER_URL')}/postCourse2023", data=course_object)

initializeCourseTable()
