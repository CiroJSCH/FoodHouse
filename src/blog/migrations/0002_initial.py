# Generated by Django 4.2.3 on 2023-07-22 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="conversation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="blog.conversation",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="conversation",
            name="participant1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conversations_as_participant1",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="conversation",
            name="participant2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conversations_as_participant2",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
