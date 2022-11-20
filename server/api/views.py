from http.client import HTTPResponse
import json
from urllib import response
from django.shortcuts import render
from rest_framework import status
import requests
import environ
# imports for API views
from rest_framework import generics #View
from rest_framework.views import APIView #APIView
from rest_framework.response import Response #APIView
from rest_framework.decorators import api_view
from .models import Course
from .serializers import *
# setting up environmental variables
env = environ.Env()
environ.Env.read_env()


@api_view(['POST'])
def postCourse(request):
    """ Insert course object into Course table
    """
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def postPrerequisite(request):
    """ Insert prerequisite entry into Prerequisite table 
    """
    if request.method == 'POST':
        serializer = PrerequisiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def postDependency(request):
    """ Insert dependency entry into Depedency table 
    """
    if request.method == 'POST':
        serializer = DependencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateCourse(request):
    """ Update each record in course table.
        :param none
        :postcond: an entry in postTable is updated
        :return: Response - either successfully posted or bad request
    """
    course_code = request.data.get("course_code")
    try:
        course_db = Course.objects.get(course_code=course_code) # database does HAVE space
    except Exception as e:
        print("Error updating course with exception: " + e)

    # need to make sure course corresponds correctly to the request.data course. 
    serialized_course = CourseSerializer(course_db, request.data) 
    if serialized_course.is_valid():
        serialized_course.save()
        return Response(serialized_course.data)
    
    return Response(serialized_course.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllCourses(request):
    """ Return all course objects from DB
        :param: none
        :return: serialized course objects OR serialized course ids depending on need
    """
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCourse(request, course_code):
    """ Return a single course, given the ID if possible"""
    #add space to course code
    course_code_with_space = list(course_code)
    course_code_with_space.insert(-3," ")
    course_code_with_space = ''.join(course_code_with_space)
    course_code_with_space = str(course_code_with_space)
    try:
        course = Course.objects.get(course_code=course_code_with_space)
    except:
        course = None
    serializer = CourseSerializer(course)
    
    return Response(serializer.data)


@api_view(['GET'])
def getAllPrereqs(request):
    """ Return all prerequisite objects from DB
        :param: none
        :return: serialized Prerequisite objects
    """
    prerequisites = Prerequisite.objects.all()
    serializer = PrerequisiteSerializer(prerequisites, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPrereqs(request, course_code):
    """ Return prerequisites in logical form of given course
        :param: course_id - course ID in the form [A-Z]{2,4}\d{2,3}
        :return: the prerequisites for the given course
    """
    # find course in course table corresponding to course_code
    req = requests.get(f"{env('DATABASE_URL')}/getCourse/{course_code}")
    if (req == None):
        return
    course = req.json()
    course_id = course.get("id")
    # get all the prerequisite records with course_id matching with the above course_id
    prerequisites = Prerequisite.objects.filter(course_id_id=course_id) # SELECT * FROM prerequisite WHERE course_id=course_id
    # create a list of lists, where each inner list is a disjuction. Each entry is a course_code
    data = []
    current_char = None
    current_inner_list_index = 0
    for prerequisite1 in prerequisites:
        prerequisite = PrerequisiteSerializer(prerequisite1)
        prerequisite_courses = Course.objects.get(id=prerequisite['course_id_prereq'].value)
        course_serializer = CourseSerializer(prerequisite_courses)
        serialized_course_code = course_serializer["course_code"].value
        if current_char == None:
            current_char = prerequisite['conjunction_expression'].value
            data.append([serialized_course_code])
        else:
            if prerequisite['conjunction_expression'].value == current_char:
                data[current_inner_list_index].append(serialized_course_code)
            else:
                data.append([serialized_course_code])
                current_inner_list_index = current_inner_list_index + 1
                current_char = prerequisite['conjunction_expression'].value
    # convert python list into json
    data_json = json.dumps(data)
    return Response(data_json)

    
@api_view(['GET'])
def getDependants(request, course_code):
    """ Return dependant courses of given course
        :param: course_id - course ID in the form [A-Z]{2,4}\d{2,3}
        :return: all dependant courses of the given course
    """
    # find course in course table corresponding to course_code
    req = requests.get(f"{env('DATABASE_URL')}/getCourse/{course_code}")
    if (req == None):
        return
    course = req.json()
    course_id = course.get("id")
    # get a querySet that contains all dependant records such that course_id=course_id
    dependancy_records = Dependency.objects.filter(course_id_id=course_id) # SELECT * FROM dependancy WHERE course_id=course_id
    # for each record, use the course_id_depend to find its course_code in course table
    data = []
    for record in dependancy_records:
        serialized_record = DependencySerializer(record)
        dependant_course = Course.objects.get(id=serialized_record['course_id_depend'].value) # get course object corresponding to 
        dependant_serializer = CourseSerializer(dependant_course)
        dependant_course_code = dependant_serializer["course_code"].value
        data.append(dependant_course_code)
    # convert python list into json
    data_json = json.dumps(data)
    return Response(data_json)
