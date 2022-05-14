from django.db import models
from onlinestore.models import Product
from django.conf import settings

class Order(models.Model):
    '''Class to create a model for each order'''
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)

    def get_total(self):
        products=self.orderitem_set.all()
        total_amount=sum([item.total() for item in products])
        return float(total_amount)


class OrderItem(models.Model):
    '''Class to construct a model for each item in a order'''

    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=1)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def total(self):
        return self.product.price*self.quantity


class ShippingAdress(models.Model):
    '''Class to construct a model for all shipping informations'''

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    adress=models.TextField()
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.adress











