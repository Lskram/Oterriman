from django import forms
from app_foods.models import Food
from .models import Subscription
class FoodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_form_instance(self, obj):
        return obj.title

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='ชื่อ-นามสกุล')
    email = forms.EmailField(max_length=60, required=True, label='อีเมลล์')
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label='เมนูที่สนใจ',
        widget= forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True, label='ขอบคุณสำหรับการลงทะเบียน ทางเราจะเก็บข้อมูลนี้ไว้สำหรับประมวลผลโปรโมชั่น ให้แก่ท่านลูกค้า สามารถสอบถามเพิ่มเติมได้ที่แอดมินที่เกี่ยวข้องได้เลยครับ หากลูกค้าท่านใดมีข้อเสนอเเนะสามารถรายงานได้โดยตรงผ่าน เค้าท์เตอร์หน้าร้านเลยครับผม.')

class SubscriptionModelForm(forms.ModelForm):
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label='เมนูที่สนใจ',
        widget= forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True, label='ขอบคุณสำหรับการลงทะเบียน ทางเราจะเก็บข้อมูลนี้ไว้สำหรับประมวลผลโปรโมชั่น ให้แก่ท่านลูกค้า สามารถสอบถามเพิ่มเติมได้ที่แอดมินที่เกี่ยวข้องได้เลยครับ หากลูกค้าท่านใดมีข้อเสนอเเนะสามารถรายงานได้โดยตรงผ่าน เค้าท์เตอร์หน้าร้านเลยครับผม.')
    
    class Meta:
        model = Subscription
        fields = ['name', 'email', 'food_set', 'accepted']
        labels = {
            'name': 'ชื่อ-นามสกุล',
            'email': 'อีเมลล์',
            'food_set': 'เมนูที่สนใจ'
        }