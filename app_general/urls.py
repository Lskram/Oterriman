from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HOME'),
    path('about/', views.about, name='ABOUT'),
    path('subscription', views.subscription, name='subscription'),
    path('subscription/thankyou', views.subscription_thankyou, name='subscription_thankyou'),
]
