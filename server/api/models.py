from django.db import models

# For all tables, see documentation on /database/database_documentation.md

# Course table
class Course(models.Model):
    course_code = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    restrictions = models.TextField(null=True)
    hyperlink = models.CharField(max_length=255, null=True)
    num_credits = models.IntegerField(null=True)

# Prerequisite table
class Prerequisite(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id')
    conjunction_expression = models.CharField(max_length=1, null=True)
    course_id_prereq = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id_prereq')