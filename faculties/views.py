
# Create your views here.

from rest_framework.response import Response

from rest_framework.views import APIView
from faculties.models import faculty
from faculties.models.faculty import Faculty

from faculties.serializers import FacultySerializer
from rest_framework import status


class FacultyView(APIView):
    def post(self, request):
        serialized_data = FacultySerializer(data=request.data)

        if serialized_data.is_valid():
            name = serialized_data.validated_data.get('name')

            try:
                Faculty.objects.get(name=name)
                return Response({'error': 'Faculty with the same name already exists'}, status=status.HTTP_400_BAD_REQUEST)
            except Faculty.DoesNotExist:
                faculty = Faculty(name=name)
                faculty.save()
                return Response({'message': 'Faculty created successfully', 'data': {'faculty': 'success'}}, status=status.HTTP_200_OK)

        return Response({'error': 'data is not valid'}, status=status.HTTP_400_BAD_REQUEST)
