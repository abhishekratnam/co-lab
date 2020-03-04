from django.shortcuts import render
from .models import Data
# Create your views here.
def home(request):
    return render(request,"informationextractor/home.html")
"""
def updater(request):
    
    if request.method == 'POST':
        data = Data.objects.create(
            fname = request.POST.get('first_name'),
            lname = request.POST.get('last_name'),
            email = request.POST.get('email'),
            )

        return render(request,"informationextractor/response.html")
"""       