from urllib import response
from django.shortcuts import render
from rest_framework import status

# imports for API views
from rest_framework import generics #View
from rest_framework.views import APIView #APIView
from rest_framework.response import Response #APIView
from rest_framework.decorators import api_view
from .models import Course
from .serializers import *


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
        :param: none
        :return: none
    """
    # course object = request.data
    course_code = request.data.get("course_code")
    course_code_without_spaces = course_code.replace(" ", "")
    # course_db = getCourse(course_code=course_code_without_spaces) # views get does NOT have space
    course_db = Course.objects.get(course_code=course_code) # database does HAVE space

    # need to make sure course corresponds correctly to the request.data course. Note only updating course_code and course_credits
    serialized_course = CourseSerializer(course_db, request.data, partial=True) 
    if serialized_course.is_valid():
        serialized_course.save()
        return Response(serialized_course)
    
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
def getPrereqs(request, course_id):
    """ Return prerequisites in logical form of given course
        :param: course_id - course ID in the form [A-Z]{2,4}\d{2,3}
        :return: the prerequisites for the given course
    """
    # ** need to set up prerequisite table **
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDependants(request, course_id):
    """ Return dependant courses of given course
        :param: course_id - course ID in the form [A-Z]{2,4}\d{2,3}
        :return: all dependant courses of the given course
    """
    # ** need to set up dependant table **
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)








