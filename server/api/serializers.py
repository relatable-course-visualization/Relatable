from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_code', 'name', 'description', 'restrictions', 'hyperlink', 'num_credits']

class PrerequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequisite
        fields = ['id', 'course_id', 'conjunction_expression', 'course_id_prereq']

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = ['id', 'course_id', 'course_id_depend']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDB
        fields = ['name', 'favColour', 'favNumber']

class CoursePreqInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePreqInfo
        fields = ['course_code', 'name', 'prereqString']