from django.urls import path
from auth_uni.views import SignUpView, SigninView

urlpatterns = [
    path('users/signup', SignUpView.as_view()),
    path('users/signin', SigninView.as_view()),
]