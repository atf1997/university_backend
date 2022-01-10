from auth_uni.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.Serializer):

    STUDENT = 'Student'
    PROFESSOR = 'Professor'
    TEACHING_ASSISTANT = 'TA'
    USER_TYPE_CHOICES = (
        (STUDENT, 'Student'),
        (PROFESSOR, 'Professor'),
        (TEACHING_ASSISTANT, 'TA'),
    )

    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class SigninSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()
