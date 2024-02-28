from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    favorite_food_set = models.ManyToManyField(
        to="app_foods.Food", 
        through="app_users.UserFavoriteFood",
        related_name ="favorited_user_set"
    )
    
class Profile(models.Model):
    address = models.TextField(default="")
    phone = models.CharField(max_length=15, default="")
    user = models.OneToOneField("app_users.CustomUser", on_delete=models.CASCADE)

class UserFavoriteFood(models.Model):
    LEVELS = [
        (1,"ชอบ"),
        (2,"ชอบมาก"),
        (3,"ชอบโคตรๆ")
    ]
    level = models.SmallIntegerField(choices=LEVELS,default=1)
    user = models.ForeignKey(
        "app_users.CustomUser", 
        on_delete=models.CASCADE,
        related_name= "favorite_food_pivot_set"
    )
    food = models.ForeignKey(
        "app_foods.Food", 
        on_delete=models.CASCADE,
        related_name= "favorite_user_pivot_set"
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user","food"],
                name="unique_user_food"
            )
        ]
    
    def level_label(self):
        selected_level = [l for l in self.LEVELS if l[0] == self.level][0]
        return selected_level[1]
        