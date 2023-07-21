from django.db import models
from landing.models import CustomUser

# Create your models here.


class Recipe():
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    # pictures = models.ImageField(upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Conversation():
    participant1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='conversations_as_participant1')
    participant2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='conversations_as_participant2')


class Message():
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
