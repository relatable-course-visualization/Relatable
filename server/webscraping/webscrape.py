import requests
from bs4 import BeautifulSoup as bs


# api call to get the content of the usask catalogue page
catalogue = requests.get("https://catalogue.usask.ca/")
webpage = bs(catalogue.content)

# get the course codes from the webpage

# function that returns the a list of course codes from the webpage.
def getCourseCode():
    # get the course codes from the webpage
    course_code_raw = webpage.select('option[value]')
    course_code = [c.get('value') for c in course_code_raw]
    course_code1 = [c for c in course_code]
    course_code2 = [str(c).split(" ", 1)[0] for c in course_code1]
    course_code2.pop(0)
    return course_code2


print(getCourseCode())