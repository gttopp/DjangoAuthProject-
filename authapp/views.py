from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
        return render(request, "index.html")


def login(request):
 if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
                login(user)
                return redirect("authapp:home")
        messages.error(request, "Invalid username or password")
        return redirect(request, "authapp:login")

def register(request):
        return render(request, "register.html")
