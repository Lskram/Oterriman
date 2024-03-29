# Generated by Django 5.0.1 on 2024-02-27 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0003_food_image_relative_url_alter_food_description_and_more'),
        ('app_users', '0002_userfavoritefood_customuser_favorite_food_set'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userfavoritefood',
            constraint=models.UniqueConstraint(fields=('user', 'food'), name='unique_user_food'),
        ),
    ]
