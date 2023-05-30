

# Steps:
# 1. Need to get all courses from DB ans store in list
# 2. We will need a dictionary with course codes as keys and dependent course list as values, initially all empty
# 3. For each course c:
#       - Use clean/marked preq to find all of its preq courses p. 
#       - For each of those preq courses p, append c to its dependancy list using dictionary from step 2
# 4. For each dependancy list, convert into a (marked) string and then put into database

def createPreqList(preq: str):
    """
    Given a marked preq, return a list of prerequisite courses
    """
    preqList = []
    i = 0
    while i < len(preq) - 1:
        if preq[i] == '$' and preq[i+1] == '[':
            course_code = ''
            i += 2
            while preq[i] != ']':
                course_code += preq[i]
                i+=1
                preqList.append(course_code)
        i += 1
    
    return preqList
            



