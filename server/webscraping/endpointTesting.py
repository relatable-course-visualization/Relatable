import requests
import environ

# setting up environmental variables
env = environ.Env()
environ.Env.read_env()


# print(r.json())

def testGetCourse():
    # Test A1
    r = requests.get(f"{env('SERVER_URL')}/getCourse/CMPT145")
    correctData = {'id': 786, 'course_code': 'CMPT 145', 'name': 'Principles of Computer Science', 'description': 'This course builds on CMPT 141 by introducing additional problem solving methods and computer science principles, to solve larger problems that are more data intensive, or require more sophisticated techniques. These principles include data structures for efficient storage and retrieval of data, selection of appropriate data structures, algorithmic paradigms for solving difficult problems, and analysis of algorithms time and space requirements. This course also emphasizes fundamental principles of coding style, testing, and top-down design for writing robust, maintainable software.', 'restrictions': 'None', 'hyperlink': 'https://catalogue.usask.ca/CMPT-145', 'num_credits': 3}
    if(r.json() != correctData):
        print("Fail - Test Case A1 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

    # Test A2
    r = requests.get(f"{env('SERVER_URL')}/getCourse/CMPT142")
    correctData = {'id': 785, 'course_code': 'CMPT 142', 'name': 'Introduction to Computer Science for Engineers', 'description': 'Introduces essential computer science and computer programming concepts and principles, with application to problems relevant to all Engineering disciplines. Presents the context in which computational problem solving is done, including historical and elementary technical aspects. Emphasizes fundamental programming constructs, including data and data types, variables and expressions, conditional branching, repetition, functions, recursion, as well as data structures such as strings, lists, and dictionaries. Presents searching and sorting algorithms as an introduction to concepts in computer science.  Emphasis throughout on the practice of basic skills needed for writing robust software, including formal design processes and documentation, internal code documentation, testing, and debugging.', 'restrictions': 'Restricted to students in the College of Engineering.', 'hyperlink': 'https://catalogue.usask.ca/CMPT-142', 'num_credits': 3}
    if(r.json() != correctData):
        print("Fail - Test Case A2 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

    # Test A3
    r = requests.get(f"{env('SERVER_URL')}/getCourse/ACB990")
    correctData = {'id': 18, 'course_code': 'ACB 990', 'name': 'Scientific Communication', 'description': 'Graduate students in the Anatomy and Cell Biology program will receive practical training in written and oral scientific communication. Topics include scientific writing technique and style, effective oral communication, electronic research tools and electronic presentation tools. Graduate students will also attend a student-run seminar series, and make one presentation in that series each year they are enrolled in the program.', 'restrictions': 'None', 'hyperlink': 'https://catalogue.usask.ca/ACB-990', 'num_credits': -1}
    if(r.json() != correctData):
        print("Fail - Test Case A3 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

    # Test A4
    r = requests.get(f"{env('SERVER_URL')}/getCourse/ENVE201")
    correctData = {'id': 1713, 'course_code': 'ENVE 201', 'name': 'Principles of Environmental Engineering', 'description': 'Population, economic growth, industrialization, urbanization and energy-use, as causes of environmental pollution. Mass and energy balance for environmental engineering systems under steady state and unsteady state conditions. Contaminant partitioning and transport in air, water and solids. Application of environmental principles (technical and non-technical) to: water resource management, water and wastewater treatment, air pollution control, solid waste management, environmental impact assessment, and environmental ethics. Thermal pollution, noise pollution, greenhouse effect, acid precipitation, ozone depletion, air toxics, and ground-level ozone and fine particulates (photochemical smog). Sustainable development and life cycle analysis. Review of the principles of environmental quality objectives, standards and guidelines.', 'restrictions': 'Restricted to students in the Environmental Engineering program. Approval of the department must be obtained for students not in the Environmental Engineering program.', 'hyperlink': 'https://catalogue.usask.ca/ENVE-201', 'num_credits': 3}
    if(r.json() != correctData):
        print("Fail - Test Case A4 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

    # Test A5
    r = requests.get(f"{env('SERVER_URL')}/getCourse/COMM380")
    correctData = {'id': 944, 'course_code': 'COMM 380', 'name': 'Business Cooperative Education I', 'description': "The first four-month work placement for B.Comm. students admitted into the Edwards Co-operative Education option. If a work placement is secured, the focus of the work experience will be for the student to gain experience is their chosen field of study. Evaluation will be based on the student's performance in the work placement, course assignments and the employer's performance evaluation. This course is graded on a Pass/Fail basis.", 'restrictions': 'None', 'hyperlink': 'https://catalogue.usask.ca/COMM-380', 'num_credits': 0}
    if(r.json() != correctData):
        print("Fail - Test Case A5 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

    # Test A6
    r = requests.get(f"{env('SERVER_URL')}/getCourse/CORR840")
    correctData = {'id': 1003, 'course_code': 'CORR 840', 'name': 'Incorporating Effective Correctional Principles and Practices into Case Management', 'description': "This course will examine the development case management of offenders from social service models of the late 1960's to the present day practice of incorporating the Risk, Need, Responsively principles and linking assessment with case management. Important concepts of assessment, risk management and rehabilitation will be explored.", 'restrictions': 'Restricted to students enrolled in the P.G.D.S.C. in Corrections program.', 'hyperlink': 'https://catalogue.usask.ca/CORR-840', 'num_credits': 3}
    if(r.json() != correctData):
        print("Fail - Test Case A6 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

    # Test A7
    r = requests.get(f"{env('SERVER_URL')}/getCourse/FABS110")
    correctData = {'id': 1898, 'course_code': 'FABS 110', 'name': 'The Science of Food', 'description': "This interdisciplinary course provides a comprehensive introduction to the principles and practice of food science and technology in today's society. Major themes are the chemistry and composition of food; preservation and processing; food safety and the role of food in health and wellness. Contemporary issues including organic foods, GMOs, nanotechnology, nutrition trends, food ingredients, and molecular gastronomy. Food security will also be addressed. Each lecture will focus on popular questions(s) related to food facts and fads using a scientific approach and discussion.", 'restrictions': 'None', 'hyperlink': 'https://catalogue.usask.ca/FABS-110', 'num_credits': 3}
    if(r.json() != correctData):
        print("Fail - Test Case A7 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

    # Test A8
    r = requests.get(f"{env('SERVER_URL')}/getCourse/AGMD800")
    correctData = {'id': 27, 'course_code': 'AGMD 800', 'name': 'Public Health and Agricultural Rural Ecosystem PHARE', 'description': 'Provides the foundation knowledge for issues related to rural health, public health and agricultural rural ecosystems. This PHARE course provides an overview of the major health issues, general health, and health service delivery issues facing persons in rural and remote areas of Canada. It provides an overview of the environmental health challenges for rural and agricultural populations in the areas of risk management, injury control, workplace safety, food safety, and protection of the biosphere.', 'restrictions': 'None', 'hyperlink': 'https://catalogue.usask.ca/AGMD-800', 'num_credits': 3}
    if(r.json() != correctData):
        print("Fail - Test Case A8 for getCourse() failed. Expected {} but got {}.".format(correctData, r.json()))

def testGetPrereqs():
    print()

def testGetDependants():
    print()

# Running functions
testGetCourse();