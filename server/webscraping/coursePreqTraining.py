import requests
import environ
import re
from nltk.tokenize import RegexpTokenizer

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()


rawPreqs = requests.get(f"{env('SERVER_URL')}/getCoursePrereqInfo")
i = 0

preqDict = {}
# {number: [rawPreq, filteredPreq]}
for pJson in rawPreqs:
    p = pJson['prereqString']
    if p != "None":
        preqDict[i] = [p,p]

def cleanPreq(preq):
    """Replace courses with $
    """
    

