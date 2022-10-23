from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Relatable Home Page Test")

def course(request, courseStr):
    # urlconfig checks that it is a correctly formatted string ie 3-4 letters follwed by 3 digits
    # need some place to check if it matches an actual course in the database
    return HttpResponse(courseStr)


# We need to connect to React and connect to the DB here with get and post methods
