# this file scrapes all the courses on the university site using, the algorithms in webscrape and courseCleaner file.
from courseClass import *
from webscrape import *
from courseCleaner import *
'''
function that creates a new course object using the arguments as attributes
'''
def createCourse(code, name, desc, preq, restriction,link ):
    new_course = Course(code, name, desc, preq, restriction, link)
    return new_course

'''
helper function that cleans the prequisite strings
'''
def preqCleaner(prerequisite):
    preq_list = courseCleaner(initialClean(prerequisite))
    return preq_list

'''
function that scrapes every single course on the usask catalogue website and returns a list of course objects with attributes
'''
def courseScraper():
    courseObjectsList = []    # list of course objects, this list would contain every course on the usask website
    listOfSubjects = getSubjectCodes() # gets the list of every subject on the usask webpage
    
    # for every subject in the list of subjects, scrape the details for every course, then create a course object for each course
    # and append to courseObjectList
    for subject in listOfSubjects:
        codeList = getCourseCodes(subject)   # list of course codes for the subject
        nameList = getCourseNames(subject)
        descList = getCourseDescriptions(subject)
        preqList = getCoursePrerequisites(subject)
        restrictionList = getCourseRestrictions(subject)
        hyperlinkList = getCourseLinks(subject)

        # create a course object for every course in the subject and store in the courseObjectList
        index = 0
        while index < len(codeList):
            cleanedPreq = preqCleaner(preqList[index])
            course1 = createCourse(codeList[index], nameList[index], descList[index], cleanedPreq, restrictionList[index], hyperlinkList[index])
            courseObjectsList.append(course1)
            index = index + 1

    return courseObjectsList
