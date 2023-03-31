from rest_framework import serializers
from schools.models import schoolregister
from students.models import student
from .models import Grades
class schoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=schoolregister

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

class gradesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grades
        fields='__all__'