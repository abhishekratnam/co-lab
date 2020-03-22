from rest_framework import serializers
from .models import Students, Mentors


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class Mentorserializer(serializers.ModelSerializer):
    class Meta:
        model = Mentors
        fields = '__all__'
