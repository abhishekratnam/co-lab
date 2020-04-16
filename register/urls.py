from django.contrib import admin
from django.urls import path, include
from . import views
from home import views as article
urlpatterns = [
    path('', views.register,name='colab-register'),
]
