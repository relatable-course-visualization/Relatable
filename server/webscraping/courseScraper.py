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


