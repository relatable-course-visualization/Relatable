import requests
from bs4 import BeautifulSoup as bs
import re


catalogue_link = "https://catalogue.usask.ca/"
# api call to get the content of the usask catalogue page
catalogue = requests.get(catalogue_link)
# scrape the webpage with beautiful soup library
webpage = bs(catalogue.content)

# get the course codes from the webpage

# function that returns the a list of subject codes from the webpage.
def getSubjectCodes():
    # get the csubject codes from the webpage
    subject_code_raw = webpage.select('option[value]')
    subject_code = [subject.get('value') for subject in subject_code_raw]
    subject_code1 = [subject for subject in subject_code]
    subject_code_refined = [str(c).split(" ", 1)[0] for c in subject_code1]
    subject_code_refined.pop(0)
    return subject_code_refined

'''
gets all the course codes for a particular subject code 
'''
def getCourseCodes(subject_code):
    # api call to get the content of the catalogie for a specific subject e.g CMPT
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content)
    # select the particular html tag/component that has the course code
    course = course_webpage.select("div h4 a")
    # use regex to get only the string that includes the Course information in every course without the unneccessary tag elements
    course_code = [str(c.find(string=re.compile(str(subject_code)))).strip() for c in course]
    # split the string by fullstop to get only the course code.
    course_code = [str(c).split(".", 1)[0] for c in course_code]
    return(course_code) 

'''
function that returns the course name for each course in a subject
'''
def getCourseNames(subject_code):
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content)
    course = course_webpage.select("div h4 a")
    course_name = [str(c.find(string=re.compile(str(subject_code)))).strip() for c in course]
    course_name = [str(c).split(":", 1)[1] for c in course_name]
    return (course_name)

    
'''
function that takes a course as a subject code as an input and returns the description for every course in the subject
'''
def getCourseDescriptions(subject_code):
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content)
    course = course_webpage.select("div.col-md-7 p")
    # remove the <p> tag from the string so that we have only the description text.
    course_description = [str(c).strip("</p>") for c in course]
    return course_description


def getCoursePrerequisites(subject_code):
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content)
    course = course_webpage.select("div.col-md-5 p")
    course_preq_list = []
    for c in course:
        c1 =  c.find("b", string=re.compile("Pre"))
        if c1 == None:
            course_preq_list.append("None")
        else:
            course_preq_list.append(c1.next_element.next_element)
    return course_preq_list


def getCourseRestrictions(subject_code):
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content)
    course = course_webpage.select("div.col-md-5 p")
    course_restriction_list = []
    for c in course:
        c1 =  c.find("b", string=re.compile("Restriction"))
        if c1 == None:
            course_restriction_list.append("None")
        else:
            course_restriction_list.append(c1.next_element.next_element)
    return course_restriction_list
'''
function that return the web links for every course in a particlar subject
'''
def getCourseLinks(subject_code):
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content)
    course = course_webpage.select("div h4 a")
    # grab only the href links in the string
    course_links = [link['href'] for link in course]
    return course_links
            

def getCourseCredits(subject_code):
    # api call to get the content of the catalogie for a specific subject e.g CMPT
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content)
    # select the particular html tag/component that has the course code
    course = course_webpage.select("div h4 a")
    # use regex to get only the string that includes the Course information in every course without the unneccessary tag elements
    course_credit = [str(c.find(string=re.compile(str(subject_code)))).strip() for c in course]
    # split the string by fullstop and colon to get only the course credit
    course_credit = [str(c).split(".", 1)[1] for c in course_credit]
    course_credit = [str(c).split(":", 1)[0] for c in course_credit]
    return(course_credit) 



def main():
    
    # Test cases for getSubjectCodes()
    listOfSubjectCodes = getSubjectCodes()
    # black box tests
    # test that the number of courses gotten is correct
   
    if (len(listOfSubjectCodes) != 170):
        print("Error in subjectCodes(), scraped "+str(len(listOfSubjectCodes)) + " instead of 170")
    # test that there is no duplicate course
    for subject in listOfSubjectCodes:
        if (listOfSubjectCodes.count(subject) > 1):
            print("Error in getSubjectCodes, there is a duplication in the list")
            return
    # test that the value returned is a list
    if (type(listOfSubjectCodes) != list):
        print("Error in getSubjectCodes, expected return type to be a list but got back " + str(type(listOfSubjectCodes)))


    #Test cases for getCourseCodes()

    #test when the input passed in null
    listOfCourseCodes = getCourseCodes(None)
    # test when the input passed does not exist
    listOfCourseCodes = getCourseCodes('BMPT')
    #test when the input passed in of the wrong variable type
    listOfSubjectCodes = getCourseCodes(2)

    # check the number of course codes returned is the right one
    #using CMPT, MUS, and HIST
    listOfCourseCodes = getCourseCodes('CMPT')
    if (len(listOfCourseCodes) != 103):
        print("Error in getCourseCodes, got " + str(len(listOfCourseCodes)) + "  CMPT courses rather than 103 " )

    # test for duplicates 
    for course in listOfCourseCodes:
        if (listOfCourseCodes.count(course) > 1):
            print("Error in getCourseCodes, there is a duplication in the list")

     # check the for different index values if the course code is consistent with the one of the website
    if (listOfCourseCodes[0] != 'CMPT 100'):
        print("Error in getCourseCodes, expected CMPT 100 got " + str(listOfCourseCodes[0]))
    if (listOfCourseCodes[13] != 'CMPT 298'):
        print("Error in getCourseCodes, expected CMPT 298 got " + str(listOfCourseCodes[13]))
    if (listOfCourseCodes[37] != 'CMPT 404'):
            print("Error in getCourseCodes, expected CMPT 404 got " + str(listOfCourseCodes[37]))

    # MUS
    listOfCourseCodes = getCourseCodes('MUS')
    if (len(listOfCourseCodes) != 81):
        print("Error in getCourseCodes, got " + str(len(listOfCourseCodes)) + "  MUS courses rather than 81 " )
    # test for duplicates 
    for course in listOfCourseCodes:
        if (listOfCourseCodes.count(course) > 1):
            print("Error in getCourseCodes, there is a duplication in the list")
    if (listOfCourseCodes[4] != 'MUS 120'):
        print("Error in getCourseCodes, expected MUS 120 got " + str(listOfCourseCodes[4]))
    if (listOfCourseCodes[13] != 'MUS 180'):
        print("Error in getCourseCodes, expected MUS 180 got " + str(listOfCourseCodes[13]))
    if (listOfCourseCodes[37] != 'MUS 364'):
        print("Error in getCourseCodes, expected MUS 364 got " + str(listOfCourseCodes[37]))

    # HIST
    listOfCourseCodes = getCourseCodes('HIST')
    if (len(listOfCourseCodes) != 153):
        print("Error in getCourseCodes, got " + str(len(listOfCourseCodes)) + "  HIST courses rather than 153 " )
    # test for duplicates 
    for course in listOfCourseCodes:
        if (listOfCourseCodes.count(course) > 1):
            print("Error in getCourseCodes, there is a duplication in the list")
    if (listOfCourseCodes[8] != 'HIST 193'):
        print("Error in getCourseCodes, expected HIST 193 got " + str(listOfCourseCodes[8]))
    if (listOfCourseCodes[19] != 'HIST 212'):
        print("Error in getCourseCodes, expected HIST 212 got " + str(listOfCourseCodes[19]))
    if (listOfCourseCodes[152] != 'HIST 996'):
        print("Error in getCourseCodes, expected HIST 996 got " + str(listOfCourseCodes[152]))
   
    # search for a course code in the list
    listOfCourseCodes = getCourseCodes('CMPT')
    if (listOfCourseCodes.count('CMPT 370') != 1):
        print("Error in getCourseCode() did not find CMPT 370")
    if (listOfCourseCodes.count('CMPT 215') != 1):
        print("Error in getCourseCode() did not find CMPT 215")
    if (listOfCourseCodes.count('CMPT 400') != 1):
        print("Error in getCourseCode() did not find CMPT 400")

    # search for one that does not exist
    if (listOfCourseCodes.count('CMPT 444') > 0 ):
        print("Error in getCourseCode(), found a course that does not exist")


    # getCourseNames()
    listOfCourseNames = getCourseNames('AGRC')
    if (len(listOfCourseNames) != 10):
        print("Error in getCourseNames, got " + str(len(listOfCourseNames)) + "  AGRIC course names rather than 10 " )

    # there are actually duplicates names in course like AGRC 298, 398 and 498

    # test at random that the course name returns the right thing
    if (listOfCourseNames[6] != ' International Study Tour'):
        print ("Error in getCourseNames() expected to return the name: International Study Tour but got " + str(listOfCourseNames[6]))

    listOfCourseNames = getCourseNames('ENG')
    if (len(listOfCourseNames) != 110 ):
        print("Error in getCourseNames, got " + str(len(listOfCourseNames)) + "  AGRIC course names rather than 110 " )
    if (listOfCourseNames[6] != ' An Introduction to Cultural Studies'):
        print ("Error in getCourseNames() expected to return the name: An Introduction to Cultural Studies " + str(listOfCourseNames[6]))

    #getCourseDescriptions()
    

# To do:
# add try catch statments or if != null

main()