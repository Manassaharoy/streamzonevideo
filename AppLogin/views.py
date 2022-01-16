from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponsePermanentRedirect
from AppLogin.forms import CreateNewUser, LoginUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from AppLogin.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method=='POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponsePermanentRedirect(reverse('App_login:login'))
    return render(request, 'App_login/signup.html', context={'title':'sign up', 'form':form})

def login_page(request):
    form = LoginUser()
    if request.method=='POST':
        form = LoginUser(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_login/login.html', context={'title':'Login', 'form':form})

@login_required
def profile(request):
    return render(request, 'App_login/profile.html', context={})

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method=='POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/editprofile.html', context={'form': form, 'title': 'Edit profile'})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))