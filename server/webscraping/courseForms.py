import requests
import environ
import re
from nltk.tokenize import RegexpTokenizer

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()

def splitPreq(s: str):
    j = 1
    # pattern = re.compile('((one)*(of)*(and)*(\s)*(\$)*\(*\)*)*')
    s = s.split(' ')
    acceptedStrings = ['One', 'one', 'and', 'or', 'of', '$', ')', '(', '($', '$)', '$;']
    transitionStrings = ['and', 'or']
    found = False
    space = ' '

    while not found:
        left = s[:j]
        right = s[j:]
        # We only want strings that contain 'One' 'of' 'and' '$' '!' '(' ')' or spaces
        # any order and any number of repetitions of above
        # regex would be like: '((one)*(of)*(and)*(\s)*(\$)**\(*)*)*'
        # Also we wanr the LARGEST
        accepted = True
        for word in left:
            if word not in acceptedStrings:
                accepted = False
                break

        while accepted:
            j += 1
            left = s[:j]
            # right = s[j:]
            for word in left:
                if word not in acceptedStrings:
                    accepted = False
                    if s[j-2] in transitionStrings:
                        return(space.join(s[:j-2]), space.join(s[j-1:]), 0, s[j-2])
                    else: 
                        return (space.join(s[:j-1]), space.join(s[j-1:]), 0, None)
            
            if j >= len(s):
                return (space.join(s), ' ', 0, None)
        
        
        # if right is all correct we can return
        accepted = True
        for word in right:
            if word not in acceptedStrings:
                accepted = False
                break

        if accepted == True:
            if j < len(s):
                if s[j-1] in transitionStrings:
                    return(space.join(s[:j-1]), space.join(s[j:]), 1, s[j-1])
            else:
                return(space.join(s[:j]), space.join(s[j:]), 1, None)

        
        j+=1


    return 'No String Accepted'


normalForms = []
specialForms = []

courseList = []
# for id in range(2, 10):
test = requests.get(f"{env('SERVER_URL')}/getCoursePrereqInfo")

test = test.json()
total = 0
courseCount = 0
noCourseCount = 0

for x in test:
    total+=1
    preqStr = x['prereqString']
    course_id_tokenizer = RegexpTokenizer('[A-Z]{2,4}\s[0-9]{2,3}')
    courseList = course_id_tokenizer.tokenize(preqStr)
    if preqStr != 'None':
        cleanPreq = re.sub('[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}', '$', preqStr)
        # if cleanPreq != preqStr:
        cleanPreq = re.sub('\$\sor\s[0-9]{2,3}.[0-9]|\$\sor\s[0-9]{2,3}', '$ or $', cleanPreq)
        cleanPreq = re.sub('\$\sand\s[0-9]{2,3}.[0-9]|\$ and [0-9]{2,3}', '$ and $', cleanPreq)
        cleanPreq = re.sub('permission of the instructor|permission from the instructor|permission of the department', '!', cleanPreq)

        cleanPreq = re.sub('[s,S]uccessful completion of', 'SC', cleanPreq)
        cleanPreq = re.sub('credit units', 'CU', cleanPreq)
        cleanPreq = re.sub('university level courses|university-level courses', 'UL', cleanPreq)
        
        # Write now, we somehow want to remove anything that is not a keyword
        cleanPreq = re.sub('\.|\,', '', cleanPreq)
        cleanPreq = re.sub('\&', 'and', cleanPreq)

        j = splitPreq(cleanPreq)
    
        if j[2] == 1:
            print(f'Original: {cleanPreq}')
            print(f'Left: {j[0]}')
            print(f'Connector: {j[3]}')
            print(f'Right: {j[1]}')


        if j[2] == 0:
            if j[0] not in normalForms:
                normalForms.append(j[0])
            if j[1] not in specialForms:
                specialForms.append(j[1])
        else:
            if j[1] not in normalForms:
                normalForms.append(j[1])
            if j[0] not in specialForms:
                specialForms.append(j[0])





        

        
    
        courseCount+= 1
        # if k == 1000:
        #     break

print(f'Total Courses: {total}, Course Count: {courseCount}, Normal Forms: {len(normalForms)}, Special Forms: {len(specialForms)}')



# want to put courses in form maybe like this:
# {courseCode: 'CMPT 215',
#  prereqStr: 'ETC ETC',
#  normal: '[CMPT 145, MATH 176] # Need to nail down exactly how we want this
#  joiner: null
#  special: null # Probably want this nailed down to
#  specialGuess: null # guess which course we should redirect to
# }

# Any two of $ $ $; or 18 CU at the university level
# Jump to AAA BBB CCC