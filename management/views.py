from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import Studentserializer,Mentorserializer
from rest_framework.response import Response

# Create your views here.
def homepage(request):
    return HttpResponse("Hello")


class Studentview(APIView):
    def get(self,request):
        queryset = Students.objects.all()
        serialized = Studentserializer(queryset, many=True)
        return Response(serialized.data)
    def post(self,request):
        serializer = Studentserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"data saved in database"})
        return Response({"message":"error"})

class Mentorview(APIView):
    def get(self,request):
        queryset = Mentors.objects.all()
        serialized = Mentorserializer(queryset, many=True)
        return Response(serialized.data)
    def post(self,request):
        serializer = Mentorserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"data saved in database"})
        return Response({"message":"error"})
