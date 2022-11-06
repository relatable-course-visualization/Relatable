from urllib import response
from django.shortcuts import render

# imports for API views
from rest_framework import generics #View
from rest_framework.views import APIView #APIView
from rest_framework.response import Response #APIView
from rest_framework.decorators import api_view
from .models import Course
from .serializers import CourseSerializer


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
def getCourse(request, course_id):
    """ Return a single course, given the ID if possible"""
    # may need to slightly edit
    course = Course.objects.get(id=course_id)
    serializer = CourseSerializer(course)

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








