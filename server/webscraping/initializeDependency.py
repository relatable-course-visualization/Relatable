from courseClass import *
from courseScraper import *
import requests

""" Initialize the dependency table in the database by parsing the prerequite table
    and inverting the relationship. 
"""
def initializeDependencyTable():
    r = requests.get("http://127.0.0.1:8000/prerequisites")
    prerequisites_table = r.json()

    for prerequisite in prerequisites_table:
        course_id = prerequisite.get("course_id")
        course_id_prereq = prerequisite.get("course_id_prereq")

        # POST request to store records in dependency table
        dependency_object = {'course_id': course_id_prereq, 'course_id_depend' : str(course_id)}
        requests.post("http://127.0.0.1:8000/postDependency", data=dependency_object)
        
initializeDependencyTable()