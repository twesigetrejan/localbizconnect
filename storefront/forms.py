from .models import Order, Item
from django import forms
from django.contrib.auth.models import User

class  OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user','item','order_status','confirmation_token']
        widgets = {
            'total_price': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make the total price field read-only
        }
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title','picture','price','category','short_description','label','quantity']
        