from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, 'blog/home.html', {})


@login_required(login_url='login')
def profile(request):
    return render(request, 'blog/profile.html', {})


@login_required(login_url='login')
def chat(request):
    return render(request, 'blog/chat.html', {})


@login_required(login_url='login')
def create_recipe(request):
    return render(request, 'blog/create-recipe.html', {})
