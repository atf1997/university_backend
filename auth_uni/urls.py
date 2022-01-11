from django.urls import path
from auth_uni.views import AsssignFacultyToUserView, SignUpView, SigninView

urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('signin', SigninView.as_view()),
    path('assign_faculty', AsssignFacultyToUserView.as_view()),
]