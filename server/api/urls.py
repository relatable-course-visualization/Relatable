from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('homepage/', views.homepage), # basic django and html test page
    path('course', views.getAllCourses), # get all courses django-rest 
    re_path(r'^course/([A-za-z]{3,4}\d{3})/$', views.getCourse), # string to get a certain course (implementation not finished)
]