from .models import OrderItem
from django import forms

class AddToCartForm(forms.ModelForm):

    class Meta:
        model=OrderItem
        fields=[]

class UpdateCartItem(forms.ModelForm):

    class Meta:
        model=OrderItem
        fields=['quantity']


