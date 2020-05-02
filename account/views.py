from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from account.forms import RegistrationForm #AccountAuthenticationForm,AccountUpdateForm
from django import forms

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password = raw_password)
            login(request,account)
            return redirect('/home')
        else:
            context['registeration_form'] = form
    else:#get request
        form = RegistrationForm()
        context['registeration_form'] = form
    return render(request,'account/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('home/base.html')
#
# # Create your views here.
# def login_view(request):
#     context = {}
#     user = request.user
#     if user.is_authenticated:
#         return redirect('user_profile/profile.html')
#     if request.POST:
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid():
#             password = request.POST['password']
#             email = request.POST['email']
#             user = authenticate(email=email, password=password)
#
#             if user:
#                 login(request,user)
#                 return redirect('user_profile/profile.html')
#     else:
#         form = AccountAuthenticationForm()
#     context['login_form'] = form
#     return render(request, 'account/login.html',context)
#
# def account_view(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
#     context = {}
#     if request.POST:
#         form = AccountUpdateForm(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AccountUpdateForm(initial= {
#             "email":request.user.email,
#             "username":request.user.username,
#             }
#         )
#     context['account_form'] = form
#     return render(request, 'account/account.html', context)
