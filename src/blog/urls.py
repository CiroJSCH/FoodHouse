from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('favorites/', views.home, name='favorites'),
    path('chat/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
]
