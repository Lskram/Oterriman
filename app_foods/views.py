from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponse
from.models import Food
from app_foods.forms import FavoriteFoodForm
from django.http import HttpRequest,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_users.models import UserFavoriteFood
from django.urls import reverse
# Create your views here.

def foods(request):
    all_foods = Food.objects.all().order_by('-is_premium')
    context = { 'foods': all_foods }
    return render(request, 'app_foods/foods.html', context)

def food(request:HttpRequest, food_id):
    one_food = None
    is_favorite_food = False
    try:
        one_food =Food.objects.get(id=food_id)
        if request.user.is_authenticated:
            user_favorite_food = UserFavoriteFood.objects.get(
                user=request.user,
                food=one_food
            )
            is_favorite_food = user_favorite_food is not None
    except:
        print('หาไม่เจอ หรือเธอลืม')
    
    form = FavoriteFoodForm()
    context = {
        'food': one_food,
        "form": form,
        "is_favorite_food": is_favorite_food
    }
    return render(request, 'app_foods/food.html', context)


@login_required
def favorite_food(request: HttpRequest, food_id):
    if request.method == "POST":
        form = FavoriteFoodForm(request.POST)
        if form.is_valid():
            boj, is_created = UserFavoriteFood.objects.update_or_create(
                defaults={"level": form.cleaned_data.get("level")},
                user=request.user,
                food=Food(id=food_id)
            )
            print("Create Favorite" if is_created else "Update Favorite")
            
    return HttpResponseRedirect(request.headers.get("referer"))



@login_required
def unfavorite_food(request: HttpRequest, food_id):
    if request.method =="POST":
        request.user.favorite_food_set.remove(Food(id=food_id))
    return HttpResponseRedirect(reverse("dashboard"))