from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 

    # Client endpoints
    path('courses', views.getAllCourses), 
    re_path(r'^getCourse/([A-za-z]{2,4}\d{2,3})/$', views.getCourse), #path like /getCourse/CMPT141/
    re_path(r'^getPrereqs/([A-za-z]{2,4}\d{2,3})/$', views.getPrereqs), 
    re_path(r'^getDependants/([A-za-z]{2,4}\d{2,3})/$', views.getDependants),

    # Database endpoints
    path('postCourse', views.postCourse),
    path('postPrerequisite', views.postPrerequisite)
]