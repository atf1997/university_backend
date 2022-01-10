from rest_framework import serializers


class FacultySerializer(serializers.Serializer):
    name = serializers.CharField()
