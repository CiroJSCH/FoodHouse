from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from landing.models import CustomUser
from .models import Recipe

# Create your views here.


@login_required(login_url='login')
def home(request):

    search = request.GET.get('search', '')

    recipes = Recipe.objects.filter(
        title__icontains=search) if search else Recipe.objects.all()

    return render(request, 'blog/home.html', {
        'recipes': recipes,
    })


@login_required(login_url='login')
def recipe(request, id):
    return render(request, 'blog/recipe.html', {})


@login_required(login_url='login')
def profile(request):
    user_recipes = Recipe.objects.filter(author=request.user)
    recipes_count = user_recipes.count()
    favorites_count = user_recipes.filter(favorites=request.user).count()

    likes_received = 0
    for recipe in user_recipes:
        likes_received += recipe.likes_count
    return render(request, 'blog/profile.html', {
        'user_recipes': user_recipes,
        'recipes_count': recipes_count,
        'favorites_count': favorites_count,
        'likes_received': likes_received,
    })


@login_required(login_url='login')
def chat(request):
    return render(request, 'blog/chat.html', {})


@login_required(login_url='login')
def create_recipe(request):
    return render(request, 'blog/create-recipe.html', {})
