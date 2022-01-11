from django.contrib import admin

from faculties.models.course import Course
from faculties.models.faculty import Faculty
from faculties.models.course import Assessment, AssessmentGrade

# Register your models here.
admin.site.register(AssessmentGrade)
admin.site.register(Assessment)
admin.site.register(Course)
admin.site.register(Faculty)
