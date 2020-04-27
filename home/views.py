from django.shortcuts import render
from home.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
<<<<<<< HEAD
    return render(request, 'home/home.html')
=======
    return render(request, 'home/base.html')
>>>>>>> 5f9c3a49477068462dfb9a81cdfc5447c4b0603b
