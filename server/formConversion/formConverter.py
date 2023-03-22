import requests
import environ
import re
from nltk.tokenize import RegexpTokenizer

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()

# We want to be more formulaic this time
# Get a string in
#	1. Recognize courses
#	2. Recognize things like CMPT 101 and 102
#	3. Any seq of strings without a keyword or important punctuation can be abstracted

# Categorize unique strings - in batches of 5 maybe
#	pervasive data including:
#		unique strings
#		conversion of unique strings record ie how to classify them
#		for checking a form like this string in -> string out


allCourses = requests.get(f"{env('SERVER_URL')}/getCoursePrereqInfo")
allCourses = allCourses.json()

fullCourseRegEx = '[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}'
courseRegEx = '[A-Z]{2,4}'
courseNumRegEx = '[0-9]{2,3}.[0-9]|[0-9]{2,3}'
# for course in allCourses:
#     originalPS = course['prereqString']
#     modifiedPS = originalPS.copy()
    
#     courseList = []
    
#     # find and replace all occurances like CMPT 140 and 145 with CMPT 140 and CMPT 145
#     implAnd = re.findall('{courseRegEx}\sand\s{courseNumRegEx}')
#     for imp in implAnd:
#     	course = re.search(courseRegEx, imp)[0]

count = 0
for course in allCourses:
    preq = course['prereqString']
    preq = re.sub('[0-9]{3}.(l|L)evel|', '', preq)
    s1 = '([A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3})\sand\s([0-9]{2,3}|[0-9]{2,3}.[0-9])'
    s2 = '([A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3})\sor\s([0-9]{2,3}|[0-9]{2,3}.[0-9])'
    s3 = '([A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}),\s([0-9]{2,3}|[0-9]{2,3}.[0-9])\sand\s([0-9]{2,3}|[0-9]{2,3}.[0-9])'
    s4 = '([A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}),\s([0-9]{2,3}|[0-9]{2,3}.[0-9])'
    s5 = '([A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3})\s\&\s([0-9]{2,3}|[0-9]{2,3}.[0-9])'
    s6 = fullCourseRegEx+'\sand\s('+courseNumRegEx+'\sor\s'+courseNumRegEx+')'
    s7 = fullCourseRegEx+'\s\(or\s'+courseNumRegEx+'\)'
    s8 = 'Art\s316.6'
    finalS = s1+'|'+s2+'|'+s3+'|'+s4+'|'+s5+'|'+s6+'|'+s7+'|'+s8
    if re.search(finalS, preq):
        # print(preq)
        # count+=1
        pass
    else:
        r2 = '(?<![A-Z]{2}\s)[0-9]{3}'
        r3 = '(?<![A-Z]{3}\s)[0-9]{3}'
        r4 = '(?<![A-Z]{4}\s)[0-9]{3}'
        if re.search(r2, preq) and re.search(r3, preq) and re.search(r4, preq):
            print(preq)
            count += 1



    
        
print(count)
        

