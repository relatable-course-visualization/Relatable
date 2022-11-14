from courseClass import *
from courseScraper import *
import requests
import environ

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()

""" Initialize the prerequisite table in the database by parsing prerequites for each 
    every course in the course table and inserting. 
"""
def initializePrerequisiteTable():
    # Get all data
    web_scraper_courses = courseScraper()
    r = requests.get(f"{env('DATABASE_URL')}/courses")
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

        '''
        for every disjunction(inner list) in the list of list
        for every prerequisite in the disjunction, set the conjunction_expression in the database prerequiste table to the variable conjunction_expression
        get the course_id of that prerequiste and place in the database table as well.
        this makes sure all prerequisite with the OR relationship have the same conjunction letter and those with AND have different conjunction letters
        e.g consider (103 OR 31) AND (12 OR 11 OR 66)
        103 and 31 would have the conjunction letter, a because of the OR expression
        12, 11 and 66 would have the same conjunction letter, b because of their OR expression
        but between these two sets, there is an AND hence why they have different conjunction letters
        '''
        conjunction_expression = 'a'
        prerequisites = prerequisites[0]
        if prerequisites != []:
            for disjunction in prerequisites:
                for prerequisite in disjunction:

                    # Get course corresponding to prerequisite
                    prerequisite_without_space = prerequisite.replace(" ", "")
                    req = requests.get(f"{env('DATABASE_URL')}/getCourse/{prerequisite_without_space}")
                    # skips to the next prerequisite if the prerequisite course does not exist
                    if (req == None):
                        return

                    prerequisite_course = req.json()
                    course_id_prereq = prerequisite_course.get("id")

                    # POST request to store records in prerequisite table
                    prerequisite_object = {'course_id': str(course_id), 'conjunction_expression': str(conjunction_expression), 
                        'course_id_prereq': course_id_prereq}
                    requests.post(f"{env('DATABASE_URL')}/postPrerequisite", data=prerequisite_object)

                conjunction_expression = chr(ord(conjunction_expression) + 1)
    
initializePrerequisiteTable()
