from lib2to3.pgen2.tokenize import tokenize
from queue import Empty
from typing import final
import nltk
from nltk.tokenize import RegexpTokenizer, word_tokenize
import string



def initialClean(course_str):
    """From a course prerequisite str, returns a list containing only course and keywords
    :param: course_str - a courses prerequisite string from USask course catalogue
    :precond: 
        i. course_str - courses are all formated as 'AA|AAA|AAAA \d{2,3}' ie 2-4 capitol letters followed 
                        by a space and then 2-3 digits (Dental assisting has 2 digits). *current implementation misses BIO 227 and 278. 
                        ie 278 is not recognized as a class
        ii. keywords - Currently 'and'. Further implementation may include ';', 'one of', 'or', **'; or' etc
    :return: course tokens - a list where each item is a str that must be a keyword or course id
    """
    # create our unique tokenizer based on given regular expression
    course_id_tokenizer = RegexpTokenizer('[A-Z]{2,4}\s[0-9]{2,3}|[a][n][d]')
    # tokenize our course str
    course_tokens = course_id_tokenizer.tokenize(course_str)
    return course_tokens




def courseCleaner(courseList):
    """Given a ordered list of keywords and course id's, re-represent the list in a logical matter so that:
        we have a list of lists where the seperation on internal lists means a 'or' and items withi each list 
        are seperated by 'and'. Thus;
            Currently working formats:
                A and B = [[A,B]]
                A or B = [[A], [B]]
                (A or B) and c = [[A,B], [C]]
            To be implemented later:
                (A and B) or c = [ [[A,B], [C]] ]
        :param: courseList - a list of courses formated as per initialClean() fn
        :return: a logically seperated list of course_ids    
    """
    # and index will be all the indices where an and operator is
    and_index = []

    for i in range(len(courseList)):
        if courseList[i] == "and":
                and_index.append(i)

    # final_list will be the list we return
    final_list = []

    # if there are no ands then we return each item wrapped in its own list
    if len(and_index) == 0:
        for k in courseList:
            final_list.append([k])
    # if length is 1 then split in half, given the two parts are not empty
    elif len(and_index) == 1:
        if len(courseList[:and_index[0]]) > 0:
            final_list.append(courseList[:and_index[0]])
        if len(courseList[and_index[0]+1:]) > 0:
            final_list.append(courseList[and_index[0]+1:])
    else:
        if len(courseList[:and_index[0]]) > 0:
            final_list.append(courseList[:and_index[0]])

        i = 1
        while i < len(and_index):
            if len(courseList[and_index[i-1]+1: and_index[i]]) > 0:
                final_list.append(courseList[and_index[i-1]+1: and_index[i]])
            i = i+1

        # print(and_index[i-1])
        # print(courseList)
        # if courseList[and_index[i]:] is not Empty:
        #     final_list.append(courseList[and_index[i]:])
    
    return final_list



def main():
    test_cases = ["CMPT 141.3 or CMPT 142.3", 
              "CMPT 145 or CMPT 115 or CMPT 117.", 
              "CMPT 214 and one of MATH 104, MATH 110, MATH 121, MATH 123, MATH 125, MATH 176 or STAT 245 (or equivalent).", 
              "MATH 110 or MATH 176; and one of CMPT 145, CMPT 115, or CMPT 117.",
              "CMPT 145 or CMPT 115 or CMPT 117; and one of MATH 104, MATH 110, MATH 121, MATH 123, MATH 125, MATH 176 or STAT 245 (or equivalent).",
              "MATH 110 or MATH 176; and one of CMPT 145, CMPT 115, or CMPT 117.",
              "Mathematics A30 or B30 or C30; or Foundations of Mathematics 30; or Pre-Calculus 30.",
              "One of (Computer Science 30, CMPT 105.3, CMPT 140.3, BINF 151.3) and one of (Mathematics B30, Foundations of Mathematics 30, Pre-Calculus 30); or MATH 110.3, MATH 123.3, MATH 133.4 or MATH 176.3 (can be taken concurrently).",
              "CMPT 280, and CMPT 215 or CME 331.",
              "CMPT 260 and CMPT 270, or CMPT 275.",
              "One of MATH 100, MATH 104, MATH 110, MATH 121, MATH 123, MATH 125, MATH 176, or STAT 103.",
              "Foundations of Mathematics 30 or Pre-Calculus 30; and BIOL 120 and 121 or permission of the department.",
              "MATH 110 and MATH 116; or MATH 176 and MATH 177."]
            #   "MATH 225 or 276; STAT 241 and 242."]
            # "MATH 110 and MATH 116; or MATH 176 and MATH 177."
    # for i in range (0, len(test_cases)):
    #     print(test_cases[i])
    #     print(initialClean(test_cases[i]))
    #     print(courseCleaner(initialClean(test_cases[i])))
    #     print("\n")

    inital_test_number = 1
    final_test_number = 1
    initial_fail = 0
    final_fail = 0


    # Test A1 and B1:
    course_data = ""
    prereq_str = "CMPT 141.3 or CMPT 142.3"
    expected_IR = ['CMPT 141', 'CMPT 142']
    expected_FR = "[['CMPT 141'], ['CMPT 142']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)

    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("Fail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
    else:
        print("Fail - Test Case {} for initialClean failed. Expected {}} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test A2 and B2:
    course_data = "Art 216"
    prereq_str = "ART 161.3"
    expected_IR = ['ART 161']
    expected_FR = "[['ART 161']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)

    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("Fail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
    else:
        print("Fail - Test Case {} for initialClean failed. Expected {}} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test A3 and B3:
    course_data = "BMSC 320"
    prereq_str = "BMSC 210.3 and BMSC 220.3"
    expected_IR = ['BMSC 210', 'and', 'BMSC 220']
    expected_FR = "[['BMSC 210'], ['BMSC 220']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)

    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("Fail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
    else:
        print("Fail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test A4 and B4:
    course_data = "CE 319"
    prereq_str = "GE 210, CE 225 (taken) and MATH 224 (taken)."
    expected_IR = ['GE 210', 'CE 225', 'and', 'MATH 224']
    expected_FR = [['GE 210'], ['CE 225'], ['MATH 224']]
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)

    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("Fail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
    else:
        print("Fail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test A5 and B5:
    course_data = "CE 464"
    prereq_str = "CE 319, CE 315 (taken), and GE 348 (taken)."
    expected_IR = ['CE 319', 'CE 315', 'and', 'GE 348']
    expected_FR = [['GE 319'], ['CE 315'], ['GE 348']]
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)

    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    
    # Test A6 and B6:
    course_data = "CE 495"
    prereq_str = "CE 295, CE 318, CE 320, GE 348, CE 327 (taken), CE 330 (taken), CE 329 (taken), CE 319 (taken), CE 321 (taken)."
    expected_IR = ['CE 295', 'CE 318', 'CE 320', 'GE 348', 'CE 327', 'CE 330', 'CE 329', 'CE 319', 'CE 321']
    expected_FR = [['CE 295', 'CE 318', 'CE 320', 'GE 348', 'CE 327', 'CE 330', 'CE 329', 'CE 319', 'CE 321']]
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)

    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1
            
    
    # Test A7 and B7:
    course_data = "CHEM 112"
    prereq_str = "Chemistry 30 or CHEM 90 or CHEM 100; and (Mathematics B30 or Foundations of Mathematics 30 or Pre-Calculus 30)."
    expected_IR = ['CHEM 100', 'and']
    expected_FR = "[['CHEM 100']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test A8 and B8:
    course_data = "CHEM 242"
    prereq_str = "CHEM 115.3 or CHEM 146.3; and one of MATH 110.3, MATH 123.3, MATH 133.4 or MATH 176.3"
    expected_IR = ['CHEM 115', 'CHEM 146', 'and', 'MATH 110', 'MATH 123', 'MATH 133', 'MATH 176']
    expected_FR = "[['CHEM 115', 'CHEM 146'], ['MATH 110', 'MATH 123', 'MATH 133', 'MATH 176']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 9:
    course_data = "CMPT 214"
    prereq_str = "CMPT 145 or CMPT 115 or CMPT 117."
    expected_IR = ['CMPT 145', 'CMPT 115', 'CMPT 117']
    expected_FR = "[['CMPT 145'], ['CMPT 115'], ['CMPT 117']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 10:
    course_data = "CMPT 332"
    prereq_str = "CMPT 280, and CMPT 215 or CME 331."
    expected_IR = ['CMPT 280', 'and', 'CMPT 215', 'CME 331']
    expected_FR = "[['CMPT 280'], ['CMPT 215', 'CME 331']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 11:
    course_data = "CMPT 355"
    prereq_str = "CMPT 260 and 270, or CMPT 275."
    expected_IR = ['CMPT 260', 'CMPT 270', 'and', 'CMPT 275']
    expected_FR = "[[['CMPT 260' 'CMPT 270'], ['CMPT 275']]]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 12:
    course_data = "DENA 50"
    prereq_str = "DENA 11, DENA 14, DENA 15, DENA 17, DENA 18, DENA 20, DENA 37"
    expected_IR = ['DENA 11', 'DENA 14', 'DENA 15', 'DENA 17', 'DENA 18', 'DENA 20', 'DENA 37']
    expected_FR = "[['DENA 11', 'DENA 14', 'DENA 15', 'DENA 17', 'DENA 18', 'DENA 20', 'DENA 37']]]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 13:
    course_data = "EE 216"
    prereq_str = "MATH 134 or (MATH 123 and MATH 124)."
    expected_IR = ['MATH 134', 'MATH 123', 'and', 'MATH 124']
    expected_FR = "[['MATH 134', ['MATH 123', 'MATH 124']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 14:
    course_data = "KIN 222"
    prereq_str = "KIN 121 and 122; MATH 104 or MATH 110."
    expected_IR = ['KIN 121', 'KIN 122', 'and', 'MATH 104', 'MATH 110']
    expected_FR = "[['KIN 121'], ['KIN 122'], ['MATH 104', 'MATH 110']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 15:
    course_data = "KIN 232"
    prereq_str = "KIN 146; OR both of KIN 121 and KIN 122."
    expected_IR = ['KIN 146', 'KIN 121', 'and', 'KIN 122']
    expected_FR = "[['KIN 146'], ['KIN 121', 'KIN 122']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 16:
    course_data = "MATH 134"
    prereq_str = "MATH 133.4; or [(MATH 110.3 or MATH 123.3 or MATH 176.3) and (MATH 164.3 or MATH 264.3 or MATH 266.3)]."
    expected_IR = ['MATH 133', 'MATH 110', 'MATH 123', 'MATH 176', 'and', 'MATH 164', 'MATH 264', 'MATH 266']
    expected_FR = "[ [ [MATH 133], [ ['MATH 133', 'MATH 110', 'MATH 123', 'MATH 176'], ['MATH 164', 'MATH 264', 'MATH 266'] ] ] ]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1


    # Test Suite 17:
    course_data = "PSY 315"
    prereq_str = "PSY 213.3, PSY 214.3, or PSY 216.3; and PSY 233.3; and PSY 235.3 (or HLST 210.3); and 3 credit units of 200-level PSY courses."
    expected_IR = ['PSY 213', 'PSY 214', 'PSY 216', 'and', 'PSY 233', 'and', 'PSY 235', 'HLST 210', 'and']
    expected_FR = "[['PSY 213', 'PSY 214', 'PSY 216'], ['PSY 233'], ['PSY 235', 'HLST 210']]"
    initial_result = initialClean(prereq_str)
    final_result = courseCleaner(initial_result)


    if len(expected_IR) == len(initial_result):
        for i in range(len(expected_IR)):
            if expected_IR[i] != initial_result[i]:
                print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
                initial_fail = initial_fail + 1
                break
    else:
        print("\nFail - Test Case {} for initialClean failed. Expected {} but got {}.".format(inital_test_number, expected_IR, initial_result))
        initial_fail = initial_fail + 1

    inital_test_number += 1

    if expected_FR != str(final_result):
        print("Fail - Test Case {} for courseCleaner failed. Expected {} but got {}.\n".format(final_test_number, expected_FR, final_result))
        final_fail += 1

    final_test_number +=1



if __name__ == "__main__":
    main()







# courses in the same list are ANDs
# Lists in a list are ORs
# need to pass in a list with a single string
# def recursiveClean(courseList):
#     # if we see 'and one of' then:
#         # all classes following that until the next "and" will be placed into a special list
#     # if we 'or' then split into two lists and call function recursively
#     or_index = []
#     and_one_index = []
#     for i in range(len(courseList)):
#         if courseList[i] == "or" and (len(and_one_index) == 0):
#             or_index.append(i)
#         elif courseList[i] == "and one of":
#             and_one_index.append(i)
#             # or_index.append(i) # this is for the case when the is Class A and one of ...


#     # all classes after "and one of into its seperate list"
#     # ** assume there is only one "and one of" fro now
#     # need to remove ors from this list
#     and_one_list = []
#     if len(and_one_index) == 1:
#         and_one_list = courseList[and_one_index[0]+1:]
#         courseList = courseList[0:and_one_index[0]]

#     # print("And one list:")
#     # print (and_one_list)
#     # assume at this point we just have ors and courses
#     or_list = []
#     # come back to later
#     # print(or_index)
#     # print(courseList)
#     if len(or_index) == 0:
#         or_list = [courseList]
#     elif len(or_index) > 0:
#         if or_index[0] != 0:
#             or_list.append(courseList[:or_index[0]])
#         i = 1
#         if len(or_index) > 1:
#             while i < len(or_index):
#                 if or_index[i-1]+1 != or_index[i]:
#                     or_list.append(courseList[or_index[i-1]+1:or_index[i]])
#                 i += 1
#         if or_index[i-1]+1 != len(courseList):
#             or_list.append(courseList[or_index[i-1]+1:])

#     # print("Or Index")
#     # print(or_index)
#     # print("Or List:")
#     final_list = []
#     if len(and_one_list) == 0:
#         for c in or_list:
#             final_list.append(c)
#     else:
#         # print(and_one_list)
#         # print(or_list)
#         for k in and_one_list:
#             for l in or_list:
#                 if k != "or":
#                     newList = l+ [k]

#                     final_list.append(newList)

#     return final_list