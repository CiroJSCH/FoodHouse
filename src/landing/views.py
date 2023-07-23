from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(request, "landing/landing.html")


def login(request):
    return render(request, "landing/login.html")


def register(request):
    return render(request, "landing/register.html")
