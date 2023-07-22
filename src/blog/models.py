from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    author = models.ForeignKey('landing.CustomUser', on_delete=models.CASCADE)
    # banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    # pictures = models.ImageField(upload_to='pictures/', null=True, blank=True)

    class Meta:
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.title}"


class Conversation(models.Model):
    participant1 = models.ForeignKey(
        'landing.CustomUser', on_delete=models.CASCADE, related_name='conversations_as_participant1')
    participant2 = models.ForeignKey(
        'landing.CustomUser', on_delete=models.CASCADE, related_name='conversations_as_participant2')


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('landing.CustomUser', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
