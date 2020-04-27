from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.homepage,name='home'),
    path('mentor/', views.Mentorview.as_view(), name="mentors"),
    path('student/', views.Studentview.as_view(), name="students"),
]
