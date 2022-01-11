from rest_framework import serializers


class FacultySerializer(serializers.Serializer):
    name = serializers.CharField()

class FacultyGetSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()

