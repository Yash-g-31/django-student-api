from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "age", "course"]

def validate_age(self, value):
    if value <= 0:
        raise serializers.ValidationError("Age must be positive")
    return value