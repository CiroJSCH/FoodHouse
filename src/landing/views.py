from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser

# Create your views here.


def landing(request):
    return render(request, "landing/landing.html")


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = CustomUser.objects.get(email=email)

            if user.check_password(password):
                login(request, user)
                return redirect("blog:home")
            else:
                form.add_error('password', "Incorrect password")
    else:
        form = UserLoginForm()

    return render(request, "landing/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")

            user = CustomUser.objects.create_user(
                email=email, username=username, password=password1
            )
            login(request, user)
            return redirect("blog:home")
        else:
            request.session["valid_email"] = form.cleaned_data.get("email")
            request.session["valid_username"] = form.cleaned_data.get(
                "username")
    else:
        valid_email = request.session.get("valid_email") or ""
        valid_username = request.session.get("valid_username") or ""

        form = UserRegisterForm(
            initial={"email": valid_email, "username": valid_username})

    context = {"form": form}

    return render(request, "landing/register.html", context)
