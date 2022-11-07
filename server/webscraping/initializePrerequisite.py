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

        prerequisites = web_scraper_dict.get(course_code)  # prerequisites is a list of lists where each list contains a course's prerequisites in a logical form

        # Algorithm to traverse prerequisite 

        # for every disjunction(inner list) in the list of list
        # for every prerequisite in the disjunction, set the conjunction_expression in the database prerequiste table to the variable conjunction_expression
        # get the course_id of that prerequiste and place in the database table as well.
        # this makes sure all prerequisite with the OR relationship have the same conjunction letter and those with AND have different conjunction letters
        # e.g consider (103 OR 31) AND (12 OR 11 OR 66)
        # 103 and 31 would have the conjunction letter, a because of the OR expression
        # 12, 11 and 66 would have the same conjunction letter, b because of their OR expression
        # but between these two sets, there is an AND hence why they have different conjunction letters
        conjunction_expression = 'a'
        for disjunction in prerequisites:
            for prerequisite in disjunction:
                print(" ")
                # set the conjunction_expression in the table to conjunctio_expression
                # set the course_Id in the preq table to be prerequisite.get("id")
            conjunction_expression = chr(ord(conjunction_expression) + 1)
                

    

initializePrerequisiteTable()
