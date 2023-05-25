from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [

# Active Endpoints
########################################################################################
    path('admin/', admin.site.urls), 

    # POST Endpoints
    path('postCourse2023', views.postCourse2023),
    
    # GET Endpoints



# Old Endpoints:
######################################################################################
    # GET endpoints
    path('courses', views.getAllCourses), 
    path('getCoursePrereqInfo', views.getCoursePrereqInfo),
    re_path(r'^getCourse/([A-za-z]{2,4}\d{2,3})$', views.getCourse), #path like /getCourse/CMPT141/
    re_path(r'^getPrereqs/([A-za-z]{2,4}\d{2,3})$', views.getPrereqs), 
    re_path(r'^getDependants/([A-za-z]{2,4}\d{2,3})$', views.getDependants),
    path('prerequisites', views.getAllPrereqs),

    # POST endpoints
    path('postTest', views.postTest),
    path('postCoursePrereqInfo', views.postCoursePrereqInfo),
    path('postCourse', views.postCourse),
    path('postPrerequisite', views.postPrerequisite),
    path('postDependency', views.postDependency),

    # PUT endpoints
    path('updateCourse', views.updateCourse)
]