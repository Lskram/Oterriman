from django.contrib import admin
from app_foods.models import Food



class FoodAdmin(admin.ModelAdmin):
    list_display = ['title','price','is_premium','promotion_end_at']
    search_fields = ['title']
    list_filter = ['is_premium']
    
admin.site.register(Food, FoodAdmin)