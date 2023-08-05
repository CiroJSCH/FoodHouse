from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from landing.models import CustomUser
from .models import Recipe

# Create your views here.


@login_required(login_url='login')
def home(request):

    recipes = Recipe.objects.all()

    return render(request, 'blog/home.html', {
        'recipes': recipes,
    })


@login_required(login_url='login')
def recipe(request, id):
    return render(request, 'blog/recipe.html', {})


@login_required(login_url='login')
def profile(request):
    user_recipes = CustomUser.objects.get(id=request.user.id).recipes.all()
    return render(request, 'blog/profile.html', {
        'user_recipes': user_recipes,
    })


@login_required(login_url='login')
def chat(request):
    return render(request, 'blog/chat.html', {})


@login_required(login_url='login')
def create_recipe(request):
    return render(request, 'blog/create-recipe.html', {})
