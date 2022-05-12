from django.db import models
from django.shortcuts import render,redirect
from onlinestore.models import Product


class CartItem(models.Model):
    '''Class to create a model for each item in shopping cart'''

    cart_id=models.CharField(max_length=50)
    date_added=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,unique=False)

    class Meta:
        ordering=['date_added']

    def total(self):
        return self.product.price * self.quantity

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self,quantity):
        self.quantity=self.quantity+int(quantity)
        self.save()
