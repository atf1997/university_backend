from django.contrib import admin

from auth_uni.models import Instructor, Student, User, UserMobileNumber

# Register your models here.
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(UserMobileNumber)
admin.site.register(User)

