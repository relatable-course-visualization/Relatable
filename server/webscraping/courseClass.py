# A class for a course
from webscrape import *
from courseCleaner import *

class Course:
    def __init__(self, code, name, description, prerequisite, restriction, link):
        self.code = code
        self.name = name
        self.description = description
        self.prerequisite = prerequisite
        self.restriction = restriction
        self.link = link

    def getCode(self):
        return '{}'.format(self.code)
    
    def getName(self):
        return '{}'.format(self.name)

    def getDescription(self):
        return '{}'.format(self.description)

    def getPrerequisite(self):
        return '{}'.format(self.prerequisite)

    def getRestricition(self):
        return '{}'.format(self.restriction)
    
    def getLink(self):
        return '{}'.format(self.link)

    def getInfo(self):
        return 'Code: {}\n Name: {} \n Description: {}\n Prerequisite(s): {}\n Restriction:{}\n Link: {}'.format(self.code, self.name, self.description, self.prerequisite, self.restriction, self.link)



lis = getCoursePrerequisites('CMPT')[8]
lis1 = courseCleaner(initialClean(lis))
# print(lis)
# print(lis1)
course1 = Course(getCourseCodes('CMPT')[8], getCourseNames('CMPT')[8], (getCourseDescriptions('CMPT')[8]), lis1,  getCourseRestrictions('CMPT')[8], getCourseLinks('CMPT')[8] )
print(course1.getName())
print(course1.getInfo())

