# app_users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import Profile,CustomUser

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name")
        
class ExtendedProfileForm(forms.ModelForm):
    prefix = "extended"
    
    class Meta:
        model = Profile
        fields = ("address", "phone")
        labels = {
            "address": "ที่อยู่",
            "phone": "เบอร์โทรศัทพ์"
        }
        Widgets = {
            "address": forms.Textarea(attrs={"rows": 3})
        }