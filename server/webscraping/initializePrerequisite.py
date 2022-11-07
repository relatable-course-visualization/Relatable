from courseClass import *
from courseScraper import *
import requests

""" Initialize the prerequisite table in the database by parsing prerequites for each 
    every course in the course table and inserting. 
"""
def initializePrerequisiteTable():
    # Get all data
    web_scraper_courses = courseScraper()
    r = requests.get("http://127.0.0.1:8000/courses")
    course_table_courses = r.json() # list of dictionaries, each dictionary is a Course with key value pairs

    # Create dictionary of web_scraper_courses where key is course_code and value is the prerequisites
    web_scraper_dict = {}
    for course in web_scraper_courses:
        web_scraper_dict[course.getCode()] = [course.getPrerequisite()]

    # Iterate through all databases course and evaluate prerequisites for each
    for course in course_table_courses:
        course_id = course.get("id")
        course_code = course.get("course_code")

        prerequisites = web_scraper_dict.get(course_code)

        # Algorithm to traver prerequisite 
    

initializePrerequisiteTable()
