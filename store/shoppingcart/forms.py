from .models import OrderItem,ShippingAdress
from django import forms

class AddToCartForm(forms.ModelForm):

    class Meta:
        model=OrderItem
        fields=[]

class UpdateCartItem(forms.ModelForm):

    class Meta:
        model=OrderItem
        fields=['quantity']


class ShippingForm(forms.ModelForm):

    class Meta:
        model=ShippingAdress
        fields=['adress','state','city','phone']