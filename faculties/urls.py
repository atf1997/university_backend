from django.urls import path
from faculties.views import FacultyView

urlpatterns = [
    path('create', FacultyView.as_view()),
    path('getall', FacultyView.as_view()),
]