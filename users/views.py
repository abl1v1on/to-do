from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from list.models import Task


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(user.pk)

            if user and user.is_active:
                login(request, user)
                return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('home')


def signin_user(request):
    if request.method == "POST":
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], password=cd['password'])
            user.save()
            return redirect('users:login')
    else:
        form = RegistrationUserForm()
    return render(request, 'users/signin.html', {"form": form})
