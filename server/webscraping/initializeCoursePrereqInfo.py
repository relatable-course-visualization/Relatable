from courseClass import *
from courseScraper import *
import requests
import environ

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()


'''
function that scrapes every single course on the usask catalogue website and returns a list of course objects with attributes
'''
def coursePartScraper():
    courseDictList = []    # list of course objects, this list would contain every course on the usask website
    listOfSubjects = getSubjectCodes() # gets the list of every subject on the usask webpage
    
    # for every subject in the list of subjects, scrape the details for every course, then create a course object for each course
    # and append to courseObjectList
    for subject in listOfSubjects:
        codeList = getCourseCodes(subject)   # list of course codes for the subject
        nameList = getCourseNames(subject)
        preqList = getCoursePrerequisites(subject)

        # create a course object for every course in the subject and store in the courseObjectList
        index = 0
        while index < len(codeList):
            course1 = {'course_code':codeList[index], 'name':nameList[index], 'prereqString':preqList[index]}
            courseDictList.append(course1)
            index = index + 1

    return courseDictList


""" Initialize course prereq info table in db. 
    This db is for testing purposes.
"""
def initializeCoursePrereqInfoTable():
    list_of_courses = coursePartScraper()
    
    for course in list_of_courses:
        requests.post(f"{env('SERVER_URL')}/postCoursePrereqInfo", data=course)



initializeCoursePrereqInfoTable()
