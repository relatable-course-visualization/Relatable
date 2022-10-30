from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=7)
    description = models.CharField(max_length=100)
