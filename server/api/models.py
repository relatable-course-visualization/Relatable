from django.db import models

# For all tables, see documentation on /database/database_documentation.md
class CourseTable2023(models.Model):
    course_code = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    restrictions = models.TextField(null=True)
    hyperlink = models.CharField(max_length=255, null=True)
    num_credits = models.IntegerField(null=True)
    raw_preq = models.TextField(null=True)
    clean_preq = models.TextField(null=True)
    marked_preq = models.TextField(null=True)
    dependent_courses = models.TextField(null=True)


# Below are all formerly used tables
#################################################################################################################
# Course table
# class Course(models.Model):
#     course_code = models.CharField(max_length=10, null=True)
#     name = models.CharField(max_length=255, null=True)
#     description = models.TextField(null=True)
#     restrictions = models.TextField(null=True)
#     hyperlink = models.CharField(max_length=255, null=True)
#     num_credits = models.IntegerField(null=True)

# # Prerequisite table
# class Prerequisite(models.Model):
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prereq_course_id') # a course in the prerequisite table
#     conjunction_expression = models.CharField(max_length=1, null=True)
#     course_id_prereq = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id_prereq') # a perequisite course

#     class Meta:
#         indexes = [
#             models.Index(fields=['course_id',]),
#         ]

# # Dependency table
# class Dependency(models.Model):
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='depend_course_id') # a course in the depedency table
#     course_id_depend = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id_depend') # a dependent course

#     class Meta:
#         indexes = [
#             models.Index(fields=['course_id',]),
#         ]

# class CoursePreqInfo(models.Model):
#     course_code = models.CharField(max_length=10, null=True)
#     name = models.CharField(max_length=255, null=True)
#     prereqString = models.TextField(null=True)

# class TestDB(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     favColour = models.CharField(max_length=255, null=True)
#     favNumber = models.IntegerField(null=True)