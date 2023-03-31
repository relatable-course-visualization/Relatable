import requests
import environ
import re
from formClass import *

env = environ.Env()
environ.Env.read_env()

def checkSimplePreqs(preqList):
    """Want to see how many forms only contain courses and logic
    """
    count_Simple = 0
    simpleList = []
    count_None = 0
    count_complicated = 0
    complicatedList = []
    for preq in preqList:
        if preq != 'None':
            # remove punctuation
            mod = re.sub(r'[^\w\s]', '', preq)
            mod = re.sub('[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}', '$', mod)
            rep = re.sub('[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}', '$', preq)
            # print(mod)
            acceptedRegex = '[Aa]nd|[Oo]ne|of|or|\$'
            accept = True
            preqTokens = mod.split(' ')
            # print(preqTokens)
            for w in preqTokens:
                
                if re.search(acceptedRegex, w) == None:
                    
                    accept = False
                    count_complicated += 1
                    if preq not in complicatedList:
                        print(preq)
                        complicatedList.append(preq)
                    break

            if accept:
                
                if rep not in simpleList:
                    simpleList.append(rep)
                count_Simple += 1
        else:
            count_None += 1
    
    print(f'None Count: {count_None}\nSimple Count: {count_Simple}, Unique: {len(simpleList)}\nComplicated Count: {count_complicated}, Unique: {len(complicatedList)}')
    returnDict = {'counts': [count_None, count_Simple, count_complicated],
                  'lists': [['None'], simpleList, complicatedList]}
    return returnDict



def checkImplicit(preqList):
    """Perform a check to see how many (and which) prerequisite forms still contain
       3-digit numbers that are unnassociated with a course code. Tests Form.formalizeCourseNames
       param: p: a list of prerequisite strings
       
       Note, March 30th inspection yielded 9 strings remaining, all of which made sense
    """
    count = 0
    for preq in preqList:
        form1 = Form(preq)
        mod = form1.formalizeCourseNames()
        
        # Want to see which implicit courses we may have missed
        # Ignore things like 200-level (which there are many)
        mod = re.sub('[0-9]{3}.(l|L)evel|', '', mod)
        # find numbers
        r2 = '(?<![A-Z]{2}\s)[0-9]{3}'
        r3 = '(?<![A-Z]{3}\s)[0-9]{3}'
        r4 = '(?<![A-Z]{4}\s)[0-9]{3}'
        if re.search(r2, mod) and re.search(r3, mod) and re.search(r4, mod):
            # visual will have to analyze to see if there are any unrecognized courses
            print(preq)
            print(form1.workingPreq)
            count += 1

    # Count on March 15, 2023 = 11
    print(count)
    return count
    
def visualInspection(preqs: list, type: str):
    """Given a list of orginal prerequisites, it will print preq, dollar preq and final preq
       Note, does not print 'None' strings
    """
    for p in preqs:    
        form = Form(p)
        form.transformForms()
        if form.type == type or type == 'All':
            print(f'{form.originalPreq}\n{form.dollarCoursePreq}\n{form.finalPreq}\n')

def normalFormTest():
    """Tests 6 normal form examples. Only prints if there is an error."""
    inputs = ['CMPT 214.3 and one of MATH 104.3, MATH 110.3, MATH 123.3, MATH 125.3, MATH 133.4, MATH 176.3, or STAT 245.3 (or equivalent).',
              'One of CMPT 145.3, CMPT 146.3, CMPT 115.3, or CMPT 117.3; and one of MATH 110.3, or MATH 123.3, or MATH 133.4, or MATH 176.3.',
              'CMPT 214.3, and CMPT 280.3, and (one of CMPT 215.3 or CME 331.3).',
              'CMPT 260 and 270, or CMPT 275.',
              'One of ASTR 113.3, PHYS 115.3, PHYS 155.3 or PHYS 156.3.',
              'ASTR 113.3, ASTR 213.3, or ASTR 214.3; and PHYS 252.3; and MATH 224.3, MATH 226.3 or MATH 238.3.']
    
    outputs = ['CMPT 214 and (MATH 104 or MATH 110 or MATH 123 or MATH 125 or MATH 133 or MATH 176 or STAT 245)',
              '(CMPT 145 or CMPT 146 or CMPT 115 or CMPT 117) and (MATH 110 or MATH 123 or MATH 133 or MATH 176)',
              'CMPT 214 and CMPT 280 and (CMPT 215 or CME 331)',
              '(CMPT 260 and CMPT 270) or CMPT 275',
              'ASTR 113 or PHYS 115 or PHYS 155 or PHYS 156',
              '(ASTR 113 or ASTR 213 or ASTR 214) and PHYS 252 and (MATH 224 or MATH 226 or MATH 238)']
    incorrect = 0
    for j in range(len(inputs)):
        form = Form(inputs[j])
        form.transformForms()
        if form.finalPreq.rstrip() != outputs[j]:
            incorrect+=1
            print(f'Error with input: {inputs[j]}\nExpected: {outputs[j]}\nGot:      {form.finalPreq}')
    
    print(f'Normal Form tests: {6-incorrect}/6')

def normalSimpleTest():
    """Tests 6 selected normal-simple preqs"""
    inputs = ['WGST 112.3 and 9 credit units university courses; or 24 credit units university courses; or permission of instructor.',
              'WGST 112.3 or WGST 201.3 or permission of the WGST Coordinator.',
              'VTPA 342 & 343 or equivalent, or TOX 402 & PATH 205, or permission of the instructor.',
              'COMM 395, STAT 345 and STAT 845 or permission of the department.',
              'STAT 342, STAT 344, and STAT 442 or by permission of the instructor.']
    
    outputs = ['WGST 112 and 9 credit units university courses; or 24 credit units university courses; or permission of instructor',
              'WGST 112 or WGST 201 or permission of the WGST Coordinator',
              '(VTPA 342 and VTPA 343) or (TOX 402 and PATH 205) or permission of the instructor',
              '(COMM 395 and STAT 345 and STAT 845) or permission of the department',
              '(STAT 342 and STAT 344 and STAT 442) or by permission of the instructor']
    incorrect = 0
    for j in range(len(inputs)):
        form = Form(inputs[j])
        form.transformForms()
        if form.finalPreq != outputs[j]:
            incorrect+=1
            print(f'Error with input: {inputs[j]}\nExpected: {outputs[j]}\nGot:      {form.finalPreq}')
    
    print(f'Normal-Simple tests: {6-incorrect}/6')            

allCourses = requests.get(f"{env('SERVER_URL')}/getCoursePrereqInfo")
allCourses = allCourses.json()
allPreqs = []
normalPreqs = []
normalSimplePreqs = []
complexPreqs = []
simplePreqs = []
for course in allCourses:
    allPreqs.append(course['prereqString'])
# Testing Script:
# Note: it is difficult to capture all cases in testing since there are so many variations in the prerequisite string.
# The functions that have been creating for testing and their purposes are:
#   1. Check Implicit - Checks if there are any errant implicit course codes that are missed -
#        - needs visual inspection of the few preqs that have 3-digit numbers without course code still
#   2. NormalFormTest and NormalSimpleTest - both have limited examples to test exact string conversion
#   3. visualInspection - will print original preq, dollar preq, and final preq of given form type to see if they are correct
#        - although informal, it is a good way to see if form conversion as a whole is working well
print('Check Implicit Cases:')
print("--------------------------")
checkImplicit(allPreqs)
print("--------------------------\n")
print('Normal and Normal-Simple case tests:')
normalFormTest()
print("--------------------------\n")
normalSimpleTest()
print("--------------------------\n")

# Uncomment below to do visual test:
# visualInspection(allPreqs, 'All') # change 'All' to any form type

formtest = Form('CMPT 214.3, and CMPT 280.3, and (one of CMPT 215.3 or CME 331.3).')
formtest.transformForms()

















