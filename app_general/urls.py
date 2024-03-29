from django.urls import path
from app_general import views

urlpatterns = [
    path('', views.home, name='HOME'),
    path('about/', views.about, name='ABOUT'),
    path('subscription/', views.subscription, name='subscription'),
    path('subscription/thankyou/', views.subscription_thankyou, name='subscription_thankyou'),
    path("change-theme/",views.change_theme, name="change_theme"),
]
