"""colab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from register import views as v
from account.views import (registration_view,logout_view)# login_view,account_view

urlpatterns = [
    # path('home/', include('home.urls'),name='home'),# redirect issue in registration
    # path('register/',include('register.urls')),
    # path('api/', include('api.urls')),
    # path('',include('django.contrib.auth.urls')),
    path('register/', registration_view, name='register'),
    path('home/', include('home.urls'), name='home'),# login page
    path('admin/', admin.site.urls),
    #path('profile/',include('user_profile.urls'),name='profile'), #path for profile
    path('logout/',logout_view,name='logout'),
    # path('login/',login_view,name='login'),
    # path('account/',account_view,name='account'),
]
