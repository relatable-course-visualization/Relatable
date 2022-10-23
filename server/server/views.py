from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Relatable Home Page Test")

def course(request, courseStr):
    return HttpResponse(courseStr)
