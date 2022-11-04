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
    course = course_webpage.select("div h4 a")
    course_name = [str(c.find(string=re.compile(str(subject_code)))).strip() for c in course]
    course_name = [str(c).split(".", 1)[0] for c in course_name]
    return(course_name) 

def main():
    # test cases for each method

    # test case for getSubjectCodes
    getSubjectCodes()

    # test case for getCourseCodes

list_of_subjects = getSubjectCodes() 
# print(list_of_subjects[3])
# print(getCourseCodes(list_of_subjects[3]))

for course in list_of_subjects:
    print(getCourseCodes(course))