from urllib import response
from django.shortcuts import render
# imports for simple views (test functions really)
from django.http import HttpResponse
# imports for API views
from rest_framework import generics #View
from rest_framework.views import APIView #APIView
from rest_framework.response import Response #APIView
from rest_framework.decorators import api_view
from .models import Course
from .serializers import CourseSerializer

# following two http response funcions are used for testing url regular expressions
def homepage(request):
    return HttpResponse("Relatable Home Page Test")


# Following to are basic get methods with database
@api_view(['GET'])
def getAllCourses(request):
    """ Return all course objects in the database"""
    courses = CourseSerializer(Course)
    serializer = CourseSerializer(courses)
    return Response(serializer.data)

@api_view(['GET'])
def getCourse(request, course_id):
    """ Return a single course, given the ID if possible"""
    # leave this maybe for marmik - not sure how to most efficiently search through database
    # additional functionality to add would be get certain depth of dependant and prerquisite classes as well - maybe use secondary fn for that
    courses = CourseSerializer(Course)
    serializer = CourseSerializer(courses)
    return Response(serializer.data)




# Examples:
# this uses rest framework to add inputted data to database - not something we will use but helpful to start learning
# class TestCourseView(generics.CreateAPIView):
#     queryset = TestCourse.objects.all() # gets all TestCourse objects from database
#     serializer_class = TestCourseSerializer # Serialies ie converts model data into json data


# # this allows gets and posts to db from client side
# class TestCourseAPIView(APIView):
#     serializer_class = TestCourseSerializer

#     # get all courses from database
#     def get(self, request):
#         course = [{"course_id": TestCourse.course_id,
#                    "description": TestCourse.description}
#                    for c in TestCourse.objects.all()]
#         return Response(course)

#     # post a course to database
#     def post(self, request):
#         serializer = TestCourseSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)



