from rest_framework import serializers
from ..models import Recipe
from landing.models import CustomUser


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'favorites', 'liked_recipes')
