#from courseClass import *

from views import postAllCourses

""" Initialize the course table in the database by capturing 
    all cleaned Course objects and POSTing them into the database
"""
def initializeCourseTable():
    courses = [Course(
        "GE 210", "Probability and Statistics", "Introduces the student to the concepts of descriptive statistics, probability, continuous and discrete probability distributions, hypothesis testing, and empirical models and regression. Examples are from various fields of engineering.",
        [['MATH 124'], ['MATH 133']], "None", "https://catalogue.usask.ca/GE-210" ), 
        Course("GE 213", "Mechanics of Materials", "Building upon the concepts introduced in the courses in statics and dynamics and the properties of engineering materials, this course extends equilibrium analysis to deformable bodies. Emphasis is placed on understanding and applying the three fundamental concepts of solid mechanics - equilibrium, constitutive relationships, and geometry of deformation (compatibility). The fundamentals are introduced and reinforced in the context of specific behaviors, including axial tension and compression, pure bending, bending in combination with shear, and torsion of circular shafts. Transformation of stress in two dimensions is introduced.", 
        [['GE 123'], ['GE 124']], "None", "https://catalogue.usask.ca/GE-213")]

    postAllCourses(courses)

initializeCourseTable()
