from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png')
    bio = models.TextField(null=True, blank=True)
    recipes = models.ManyToManyField('blog.Recipe', related_name='recipes')
    favorites = models.ManyToManyField('blog.Recipe', related_name='favorites')
    liked_recipes = models.ManyToManyField(
        'blog.Recipe', related_name='liked_recipes')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"
