from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('favorites/', views.home, name='favorites'),
    path('chat/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('create-recipe/', views.create_recipe, name='create-recipe'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
]
