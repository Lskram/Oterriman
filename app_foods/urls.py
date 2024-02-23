from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name='FOODS'),
    path('<int:food_id>',views.food, name='FOOD'),
]
