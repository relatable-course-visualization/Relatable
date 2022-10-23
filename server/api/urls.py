from django.contrib import admin
from django.urls import path, re_path
from .views import homepage, course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage),
    re_path(r'^course/([A-za-z]{3,4}\d{3})/$', course)
]