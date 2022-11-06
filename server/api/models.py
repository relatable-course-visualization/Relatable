from django.db import models

# Course table. See documentation on /database/database_documentation.md
class Course(models.Model):
    course_code = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    restrictions = models.TextField(null=True)
    hyperlink = models.CharField(max_length=255, null=True)
    num_credits = models.IntegerField(null=True)
