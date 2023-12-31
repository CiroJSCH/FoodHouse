# Generated by Django 4.2.3 on 2023-08-01 00:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_remove_recipe_description_recipe_banner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="categories",
            field=models.ManyToManyField(
                blank=True,
                choices=[
                    ("breakfast", "Desayuno"),
                    ("lunch", "Almuerzo"),
                    ("snack", "Merienda"),
                    ("dinner", "Cena"),
                ],
                to="blog.recipe",
            ),
        ),
    ]
