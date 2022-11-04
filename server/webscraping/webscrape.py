import requests
from bs4 import BeautifulSoup as bs


# api call to get the content of the usask catalogue page
catalogue = requests.get("https://catalogue.usask.ca/")
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


print(getSubjectCodes())