from django.db import models
from auth_uni.models import Instructor, Student

class Course(models.Model):
    name = models.CharField(max_length=100)
    prerequisite = models.ManyToManyField('self', blank=True)
    instructors = models.ManyToManyField(Instructor, blank=True)

class Assessment(models.Model):
    name = models.CharField(max_length=50)
    grade = models.FloatField(min=1)
    weight = models.FloatField(min=1, max=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

class AssessmentGrade(models.Model):
    assessment = models.ForeignKey(Assessment)
    student = models.ForeignKey(Student)
    grade = models.FloatField(min=0)
    added_by = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)




