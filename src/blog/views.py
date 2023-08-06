from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from landing.models import CustomUser
from .models import Recipe, Category

# Create your views here.


@login_required(login_url='login')
def home(request):

    search = request.GET.get('search', '')

    is_favorite = True if request.path == '/blog/favorites/' else False

    if is_favorite:
        recipes = Recipe.objects.filter(favorites=request.user)

    else:
        recipes = Recipe.objects.filter(
            title__icontains=search) if search else Recipe.objects.all()

    recipes_count = {
        "Breakfast": 0,
        "Lunch": 0,
        "Snack": 0,
        "Dinner": 0,
    }

    for category_name in recipes_count.keys():
        category = Category.objects.filter(name=category_name).first()
        if category:
            recipes_count[category_name] = Recipe.objects.filter(
                categories=category).count()

    duration_count = {
        "15": 0,
        "30": 0,
        "45": 0,
        "60": 0,
    }

    for duration in duration_count.keys():
        duration_count[duration] = Recipe.objects.filter(
            duration__lte=int(duration)).count()

    return render(request, 'blog/home.html', {
        'recipes': recipes,
        'is_favorite': is_favorite,
        'recipes_count': recipes_count,
        'duration_count': duration_count,
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
