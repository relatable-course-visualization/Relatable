# A class for a course
from webscrape import *

class Course:
    def __init__(self, code, name, description, prerequisite, restriction, link, credit_units):
        self.course_code = code
        self.name = name
        self.description = description
        self.prerequisite = prerequisite
        self.restrictions = restriction
        self.hyperlink = link
        self.num_credits = credit_units

    def getCode(self):
        return '{}'.format(self.course_code)
    
    def getName(self):
        return '{}'.format(self.name)

    def getDescription(self):
        return '{}'.format(self.description)

    def getPrerequisite(self):
        return (self.prerequisite)

    def getRestriction(self):
        return '{}'.format(self.restrictions)
    
    def getLink(self):
        return '{}'.format(self.hyperlink)

    def getCredit(self):
        return (int(self.num_credits))

    def getInfo(self): # change how you return Prerequisite, should be a string
        return 'Code: {}\n Name: {} \n Description: {}\n Prerequisite(s): {}\n Restriction:{}\n Link: {}\n Credit Units: {}\n'.format(self.course_code, self.name, self.description, self.prerequisite, self.restrictions, self.hyperlink, self.num_credits)






