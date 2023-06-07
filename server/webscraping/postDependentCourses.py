import requests
import environ

env = environ.Env()
environ.Env.read_env()

def createCourseRecords():
    """
    Get all courses from DB, make each of them a dictionary, and return a record with keys as course codes mapped to entire dictionary of course. 
    Also, create a dictionary mapping course codes to empty list (to be dependency list)
    :return A tuple: A course record of course codes to course dictionary and a dictionary of course codes to empty lists
    """
    allCourses = requests.get(f"{env('SERVER_URL')}/getAllCourses2023")
    allCourses = allCourses.json()

    courseRecord = {}
    dependDict = {}
    # May be redundant if .json() returns a list
    for course in allCourses:
        courseRecord[course['course_code']] = course
        dependDict[course['course_code']] = []

    return courseRecord, dependDict

def createPreqList(preq: str):
    """
    Given a marked preq, return a list of prerequisite courses
    """
    if preq is None:
        return []
    preqList = []
    i = 0
    while i < len(preq) - 1:
        if preq[i] == '$' and preq[i+1] == '[':
            course_code = ''
            i += 2
            while preq[i] != ']':
                course_code += preq[i]
                i += 1
            preqList.append(course_code)
        i += 1

    return preqList

def createDependStr(dependList: list):
    """
    Given a list of dependent courses, convert it into a marked string
    """
    dependStr = ''
    for i in range(len(dependList)):
        if i == len(dependList) - 1:
            dependStr += '$['+dependList[i]+']$'
        else:
            # May want to rework how these are seperated in the string
            dependStr += '$['+dependList[i]+']$, '

    return dependStr

def main():
    """
    Steps:
    1. Need to get all courses from DB and store in list
    2. We will need a dictionary with course codes as keys and dependent course list as values, initially all empty
    3. For each course c:
          - Use clean/marked preq to find all of its preq courses p. 
          - For each of those preq courses p, append c to its dependancy list using dictionary from step 2
    4. For each dependancy list, convert into a (marked) string and then put into database
    5. For each course that is notInCatalogue, add to database with marker indicating that the course does not exist
    """

    courseRecord, dependDict = createCourseRecords()
    notInCatalogue = []

    # for each course find its preqs and put it in a list
    for course_code in courseRecord.keys():
        preqList = createPreqList(courseRecord[course_code]['marked_preq'])

        # for each preq in list, append course_code to its dependent courses
        for preq in preqList:
            try:
                dependDict[preq].append(course_code)
            except:
                # these are courses that are mentioned as prerequisites but are no longer offered at USask
                if preq not in notInCatalogue:
                    notInCatalogue.append(preq)

    for course_code in courseRecord.keys():
        # create a dependent sting from its dependent list, then update the course record
        dependStr = createDependStr(dependDict[course_code])
        courseRecord[course_code]['dependent_courses'] = dependStr

        # then post the updated course information
        requests.put(f"{env('SERVER_URL')}/updateCourse2023",
                     data=courseRecord[course_code])

    # Add courses not in catalogue into db with marker indicating so
    for course_code in notInCatalogue:
        course_object = {'course_code': str(course_code), 'not_in_catalogue': True}
        print(course_object)

        requests.post(f"{env('SERVER_URL')}/postCourse2023", data=course_object)

if __name__ == '__main__':
    main()
