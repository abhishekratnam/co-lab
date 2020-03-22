from django.shortcuts import render
from django.http import HttpResponse,request
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import Studentserializer,Mentorserializer
from rest_framework.response import Response
from django.views.generic import TemplateView

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



def Registerform(request):
    if request.method == 'GET':
        template_name = 'management/home.html'
        return render(request,template_name)


    elif request.method == 'POST':
        template = 'management/response.html'
        form = Mentorform(request.POST)
        author = form.save(commit=False)
        author.save()
        return render(request,template)
"""
class Registerform(TemplateView):
    def post(self,request):
        fname, lname = self.request.post.get('phone').split(' ',1)
        email = self.request.post.get('email')
        locality = self.request.post.get('locality')
        phone = self.request.post.get('phone')
        expert = self.request.post.get('expertise')

        mentorObj = Mentors.objects.create(first_name =fname,
                    last_name =lname,email_id = email,Locality = locality,phone_no = phone,expertize = expert )

        studentObj = Students.objects.create(first_name =fname,
                    last_name =lname,email_id = email,Locality = locality,phone_no = phone,expertize = expert)
        return render(request,'management/response.html')

    def get(self, request):
        return render(request, 'management/home.html')
"""