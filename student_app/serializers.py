from rest_framework import serializers # import serializers from DRF
from .models import Student # import Pokemon model from models.py

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','student_email','locker_number']

class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['id'] 