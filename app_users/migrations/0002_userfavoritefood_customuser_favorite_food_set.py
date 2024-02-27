# Generated by Django 5.0.1 on 2024-02-27 21:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0003_food_image_relative_url_alter_food_description_and_more'),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavoriteFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(choices=[(1, 'ชอบ'), (2, 'ชอบมาก'), (3, 'ชอบโคตรๆ')], default=1)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_user_pivot_set', to='app_foods.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_food_pivot_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_food_set',
            field=models.ManyToManyField(related_name='favorited_user_set', through='app_users.UserFavoriteFood', to='app_foods.food'),
        ),
    ]