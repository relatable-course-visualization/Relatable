from http.client import HTTPResponse
import json
from urllib import response
from django.shortcuts import render
from rest_framework import status
import requests

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
    req = requests.get(f"http://127.0.0.1:8000/getCourse/{course_code}")
    if (req == None):
        return

    course = req.json()
    course_id = course.get("id")

    #add space to course code
    course_code_with_space = list(course_code)
    course_code_with_space.insert(-3," ")
    course_code_with_space = ''.join(course_code_with_space)
    course_code_with_space = str(course_code_with_space)

    # course = Course.objects.filter(course_code=str(course_code_with_space))
    # course_id = course.get("id")
    print("course_id: " + str(course_id))




    

    

     



@api_view(['GET'])
def getDependants(request, course_code):
    """ Return dependant courses of given course
        :param: course_id - course ID in the form [A-Z]{2,4}\d{2,3}
        :return: all dependant courses of the given course
    """
    # ** need to set up dependant table **
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
