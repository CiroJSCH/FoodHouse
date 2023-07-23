from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(request, "landing/landing_page.html")


def login(request):
    return render(request, "landing/login.html")
