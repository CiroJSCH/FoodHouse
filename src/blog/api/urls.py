from django.urls import path
from . import views

urlpatterns = [
    path('favorites/', views.favorites),
    path('add-favorites/', views.add_favorite),
    path('delete-favorites/', views.delete_favorite)
]
