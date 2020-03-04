from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage,name='home'),
    path('api/mentor/', views.Mentorview.as_view(), name="mentors"),
    path('api/student/', views.Studentview.as_view(), name="students"),
]
