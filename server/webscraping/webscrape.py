import requests
from bs4 import BeautifulSoup as bs
import re

catalogue_link = "https://catalogue.usask.ca/"
# api call to get the content of the usask catalogue page
catalogue = requests.get(catalogue_link)
# scrape the webpage with beautiful soup library
webpage = bs(catalogue.content, features="html.parser")

# get the course codes from the webpage

def getSubjectCodes():
    '''
    desc: function that returns the a list of subject codes(e.g CMPT, BIOL, CHEM) from the catalogue.
    param: none
    return: a list of subject codes from the course catalogue
    '''
    # get the csubject codes from the webpage
    subject_code_raw = webpage.select('option[value]')
    subject_code = [subject.get('value') for subject in subject_code_raw]
    subject_code1 = [subject for subject in subject_code]
    subject_code_refined = [str(c).split(" ", 1)[0] for c in subject_code1]
    subject_code_refined.pop(0)
    return subject_code_refined

def getCourseCodes(subject_code):
    '''
    desc: function that gets all the course codes for a particular subject code 
    param: subject code
    return: a list of course codes from the subject passed in (e.g for the input CMPT, a list that has CMPT 100, CMPT 140...)
    '''
    # api call to get the content of the catalogie for a specific subject e.g CMPT
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content, features="html.parser")
    # select the particular html tag/component that has the course code
    course = course_webpage.select("div h4 a")
    # use regex to get only the string that includes the Course information in every course without the unneccessary tag elements
    course_code = [str(c.find(string=re.compile(str(subject_code)))).strip() for c in course]
    # split the string by fullstop to get only the course code.
    course_code = [str(c).split(".", 1)[0] for c in course_code]
    return(course_code) 

def getCourseNames(subject_code):
    '''
    desc: function that returns the course name for each course in a subject 
    param: subject code
    return: a list of course names from the subject passed in (e.g for the input CMPT, a list that has 'Intro to computer science', 'Data Structures and Algorithms'...)
    '''
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content, features="html.parser")
    course = course_webpage.select("div h4 a")
    course_name = [str(c.find(string=re.compile(str(subject_code)))).strip() for c in course]
    course_name = [str(c).split(":", 1)[1] for c in course_name]
    return (course_name)

def getCourseDescriptions(subject_code):
    '''
    desc: function that takes a subject code as an input and returns the description for every course in the subject
    param: subject code
    return: a list of course descriptions from the subject passed in
    '''
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content, features="html.parser")
    course = course_webpage.select("div.col-md-7 p")
    # remove the <p> tag from the string so that we have only the description text.
    course_description = [str(c).strip("</p>") for c in course]
    return course_description


def getCoursePrerequisites(subject_code):
    '''
    desc: function that takes a subject code as an input and returns the prerequisites for every course in the subject
    param: subject code
    return: a list of prerequisites for every course in the input subject
    '''
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content, features="html.parser")
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
    '''
    desc: function that takes a subject code as an input and returns the restricition for every course in the subject
    param: subject code
    return: a list of course restrictions for every course from the subject passed in
    '''
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content, features="html.parser")
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
    '''
    desc: function that takes a subject code as an input and returns the catalogue hyperlinks for every course that belongs to the subjects
    param: subject code
    return: a list of hyperlinks for every course from the subject passed in
    '''
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content, features="html.parser")
    course = course_webpage.select("div h4 a")
    # grab only the href links in the string
    course_links = [link['href'] for link in course]
    return course_links
            
def getCourseCredits(subject_code):
    '''
    desc: function that takes a subject code as an input and returns the number of credits for every course that belongs to the subjects
    param: subject code
    return: a list of credit units for every course from the subject passed in
    '''
    # api call to get the content of the catalogie for a specific subject e.g CMPT
    course_weblink = catalogue_link+"?subj_code="+str(subject_code)+"&cnum="
    course_catalogue = requests.get(course_weblink)
    course_webpage = bs(course_catalogue.content, features="html.parser")
    # select the particular html tag/component that has the course code
    course = course_webpage.select("div h4 a")
    # use regex to get only the string that includes the Course information in every course without the unneccessary tag elements
    course_credit = [str(c.find(string=re.compile(str(subject_code)))).strip() for c in course]
    # split the string by fullstop and colon to get only the course credit
    course_credit = [str(c).split(".", 1)[1] for c in course_credit]
    course_credit = [str(c).split(":", 1)[0] for c in course_credit]
    return(course_credit) 


def main():
    '''
    # Test cases for getSubjectCodes()
    '''
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

    '''
    #Test cases for getCourseCodes()
    '''
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

    '''
    getCourseNames()
    '''
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

    
    '''
    getCourseDescriptions()
    '''
    listOfCourseDescriptions = getCourseDescriptions('CMPT')
    if (len(listOfCourseDescriptions) != 103):
        print("Error in getCourseDescriptions, got " + str(len(listOfCourseDescriptions)) + "  CMPT course descriptions rather than 103 " )

    if (listOfCourseDescriptions[2] != 'Concepts in Computing such as algorithms, problem solving, and programming are explored using interactive multimedia systems as the creative focus. Basic skills in problem solving, programming, design and interaction, event-based behaviour, and prototyping are developed.'):
        print("Error in getCourseDescriptions expected a different output from " + listOfCourseDescriptions[2])

    if (listOfCourseDescriptions[102] != 'Students writing a Ph.D. thesis must register for this course.'):
        print("Error in getCourseDescriptions expected a different output from " + listOfCourseDescriptions[102])
    
    if (listOfCourseDescriptions[55] != 'This course presents a requirements engineering (RE) approach to usability engineering (UE) by providing in depth coverage of Usability Centered Development (UCD). UE and UCD provide a structured approach to developing usable user interface designs. UE helps integrate human-computer interaction (HCI) requirements and design approaches within development projects managed by software engineering (SE) methodologies.'):
        print("Error in getCourseDescriptions expected a different output from " + listOfCourseDescriptions[55])

    if (listOfCourseDescriptions[23] != 'Lectures, assignments and projects dealing with the management, storage, and retrieval of large volumes of data. Concentrates on the relational data model, and relational data base management systems. Topics include: temporal data, recovery and concurrency, integrity and security, normalization, and semantic modelling. Additional topics include multimedia databases and other paradigms.'):
        print("Error in getCourseDescriptions expected a different output from " + listOfCourseDescriptions[23])    

    if (listOfCourseDescriptions[90] != 'Concerns selected design issues in distributed and parallel computer systems, particularly those most relevant to the goal of achieving high performance. In the parallel systems areas, such design issues arise in operating systems, run-time support software, compilers, and architecture. Topics concerning distributed systems may include interprocess communications, file systems, and load sharing, with emphasis on support for advanced parallel or multimedia applications.'):
        print("Error in getCourseDescriptions expected a different output from " + listOfCourseDescriptions[90])

    '''
    getCoursePrerequisites
    '''
    listOfCoursePrerequisites = getCoursePrerequisites('ECON')
    # check to make sure it is the right size
    if (len(listOfCoursePrerequisites) != 74):
        print("Error in getCoursePrerequisites expected 74 prerequisites from ECON classes but got " + len(listOfCoursePrerequisites))
    
    # test if the prerequisites at the index valuees are valid
    if (listOfCoursePrerequisites[1] != 'None'):
        print("Error in getCoursePrerequisites() expected prerequisite to be none but got " + listOfCoursePrerequisites[1])
    
    if (listOfCoursePrerequisites[42]!= ' ECON 214 or ECON 274; and one of MATH 104, MATH 110, MATH 121, MATH 123, MATH 125, or MATH 176.'):
        print("Error in getCoursePrerequisites() expected prerequisite to be ECON 214 or ECON 274; and one of MATH 104, MATH 110, MATH 121, MATH 123, MATH 125, or MATH 176. but got " + listOfCoursePrerequisites[42])

    if (listOfCoursePrerequisites[72] != 'None'):
        print("Error in getCoursePrerequisites() expected prerequisite to be None but got " + listOfCoursePrerequisites[72])


    listOfCourseRestricitions = getCourseRestrictions('MATH')

    if (len(listOfCourseRestricitions) != 69):
        print("Error in getCourseRestricitions expected 69 prerequisites from MATH classes but got " + len(listOfCourseRestricitions))
    
    # check aat random indexes to make sure the values are correct
    if (listOfCourseRestricitions[6] != ' Restricted to students in the College of Engineering.' ):
        print("Error in getCourseRestricitions, expected the restriction to be Restricted to students in the College of Engineering. but got " + listOfCourseRestricitions[6])

    if (listOfCourseRestricitions[65] != 'None' ):
        print("Error in getCourseRestricitions, expected the restriction to be None. but got " + listOfCourseRestricitions[65])

    if (listOfCourseRestricitions[52] != 'None' ):
        print("Error in getCourseRestricitions, expected the restriction to be None. but got " + listOfCourseRestricitions[52])

    if (listOfCourseRestricitions[32] != 'None' ):
        print("Error in getCourseRestricitions, expected the restriction to be None. but got " + listOfCourseRestricitions[32])

    listOfCourseRestricitions = getCourseRestrictions('INDG')

    if (listOfCourseRestricitions[48] != ' Restricted to students in the College of Graduate Studies and Research' ):
            print("Error in getCourseRestricitions, expected the restriction to be Restricted to students in the College of Graduate Studies and Research.. but got " + listOfCourseRestricitions[48])
    if (listOfCourseRestricitions[3] != 'None' ):
            print("Error in getCourseRestricitions, expected the restriction to be None. but got " + listOfCourseRestricitions[3])

    '''
    getCourseLinks()
    '''
    listOfCourseLinks = getCourseLinks('GEOG')
    if (len(listOfCourseLinks) != 69):
        print("Error in getCourseLinks expected 69 links from GEOG classes but got " + len(listOfCourseLinks)) 

     # check at random indexes to make sure the values are correct 
    if (listOfCourseLinks[5] != 'https://catalogue.usask.ca/GEOG-204' ):
        print("Error in getCourseLinks expected course link to be https://catalogue.usask.ca/GEOG-204 but got " + listOfCourseLinks[5] ) 
    
    if (listOfCourseLinks[16] != 'https://catalogue.usask.ca/GEOG-299' ):
        print("Error in getCourseLinks expected course link to be https://catalogue.usask.ca/GEOG-299 but got " + listOfCourseLinks[16] ) 

    if (listOfCourseLinks[51] != 'https://catalogue.usask.ca/GEOG-825' ):
        print("Error in getCourseLinks expected course link to be https://catalogue.usask.ca/GEOG-825 but got " + listOfCourseLinks[51] ) 

   
    '''
    getCourseCredits()
    '''

    listOfCourseCredits = getCourseCredits('EP')
    if (len(listOfCourseCredits) != 21):
        print("Error in getCourseCredits expected 21 from EP classes but got " + str(len(listOfCourseCredits))) 

    if (listOfCourseCredits[3] != '1'):
        print("Error in getCourseCredits expected the course credit for the class to be 1 but got " + str(listOfCourseCredits[3])) 

    if (listOfCourseCredits[14] != '3'):
        print("Error in getCourseCredits expected the course credit for the class to be 3 but got " + str(listOfCourseCredits[15])) 
    
    if (listOfCourseCredits[18] != '6'):
        print("Error in getCourseCredits expected the course credit for the class to be 6 but got " + str(listOfCourseCredits[26])) 


