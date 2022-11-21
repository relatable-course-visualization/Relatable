from courseClass import *
from courseScraper import *
import requests
import environ

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()

""" Initialize the dependency table in the database by parsing the prerequite table
    and inverting the relationship. 
"""
def initializeDependencyTable():
    r = requests.get(f"{env('SERVER_URL')}/prerequisites")
    prerequisites_table = r.json()

    for prerequisite in prerequisites_table:
        course_id = prerequisite.get("course_id")
        course_id_prereq = prerequisite.get("course_id_prereq")

        # POST request to store records in dependency table
        dependency_object = {'course_id': course_id_prereq, 'course_id_depend' : str(course_id)}
        requests.post(f"{env('SERVER_URL')}/postDependency", data=dependency_object)
        
initializeDependencyTable()