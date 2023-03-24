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
       
       Note, March 15th inspection yielded 11 strings remaining, all of which made sense
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
            count += 1

    # Count on March 15, 2023 = 11
    print(count)
    return count
    


allCourses = requests.get(f"{env('SERVER_URL')}/getCoursePrereqInfo")
allCourses = allCourses.json()
# Testing for Form.formalize course names:
count = 0
countCourseForms = 0
originalPreqList = []
modifiedPreqList = []
replacedPreqList = []
k = 0

for course in allCourses:
    preq = course['prereqString']
    originalPreqList.append(preq)
    form = Form(preq)
    modifiedPreqList.append(form.transformForms())
    form.characterizeForm()
    # form.replaceCourseCodes()
    if form.type == 'Normal-Simple':
        # print(form.workingPreq)
        k+= 1
        # if form.dollarCoursePreq not in replacedPreqList:
        #     replacedPreqList.append(form.dollarCoursePreq)
        # print(f'{form.originalPreq}\n{form.workingPreq}\n{form.dollarCoursePreq}\n{form.finalPreq}\n')
    # print(f'{form.type}: {form.workingPreq}')
# form = Form('BIOL 323.3 and/or BIOL 326.3 or equivalent, or instructor’s authorization.')
# form.transformForms()

print(k)
# print(len(replacedPreqList))

f = open('New_Forms.txt', 'w+')

nl = '\n'
for forms in replacedPreqList:
    f.write(f'{forms}{nl}')
# checkSimplePreqs(modifiedPreqList)
# print(modifiedPreqList)
# checkImplicit(modifiedPreqList)















