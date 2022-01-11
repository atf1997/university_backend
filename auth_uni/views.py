from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from auth_uni.models import Instructor, Student, User
from auth_uni.serializers import RegisterUserSerializer, SigninSerializer, UserSerializer, AssignFacultyToUserSerializer
from faculties.models.faculty import Faculty
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.


class SignUpView(APIView):

    def post(self, request):

        serialized_data = RegisterUserSerializer(data=request.data)

        if serialized_data.is_valid():
            email = serialized_data.validated_data.get('email')

            try:
                User.objects.get(email=email)
                return Response({'error': 'User with the same email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                pass

            user = User()
            user.email = email
            user.username = email
            user.set_password(serialized_data.validated_data.get('password'))
            user.first_name = serialized_data.validated_data.get('first_name')
            user.last_name = serialized_data.validated_data.get('last_name')
            user.date_of_birth = serialized_data.validated_data.get(
                'date_of_birth')
            user.save()

            type = serialized_data.validated_data.get('type')
            if type == RegisterUserSerializer.STUDENT:
                student = Student()
                student.user = user
                student.save()
            else:
                instructor = Instructor()
                instructor.user = user
                instructor.type = type
                instructor.save()

            token = Token.objects.create(user=user)

            return Response({'message': 'User created successfully', 'data': {'user': UserSerializer(user).data, 'token': token.key}}, status=status.HTTP_200_OK)

        return Response({'error': 'data is not valid'}, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):

    def post(self, request):

        serialized_data = SigninSerializer(data=request.data)
        print(serialized_data)
        if serialized_data.is_valid():
            email = serialized_data.validated_data.get('email')
            password = serialized_data.validated_data.get('password')

            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    token = Token.objects.get_or_create(user=user)
                    return Response({'message': 'User signed successfully', 'data': {'user': UserSerializer(user).data, 'token': token.key}}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Pass is wrong'}, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                return Response({'error': 'User not exists'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'data is not valid'}, status=status.HTTP_400_BAD_REQUEST)


class AsssignFacultyToUserView(APIView):

    def post(self, request):
        permission_classes = [IsAuthenticated]
        serialized_data = AssignFacultyToUserSerializer(data=request.data)
        if serialized_data.is_valid():
            facultyId = serialized_data.validated_data.get('facultyId')

            try:
                # after authenticated by permission_classes user is put in request object 
                user = User.objects.get(auth_token=request.auth)
                faculty = Faculty.objects.get(pk=facultyId)
                user.faculty = faculty
                user.save()
                return Response({'message': 'Faculty added successfully', 'data': {'user': UserSerializer(user).data}}, status=status.HTTP_200_OK)
            except Faculty.DoesNotExist:
                return Response({'error': 'Faculty not exists'}, status=status.HTTP_400_BAD_REQUEST)
               

        return Response({'error': 'data is not valid'}, status=status.HTTP_400_BAD_REQUEST)
