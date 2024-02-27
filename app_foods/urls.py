from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name='FOODS'),
    path('<int:food_id>',views.food, name='FOOD'),
    path('<int:food_id>/favorite', views.favorite_food, name="favorite_food")
]
