from .models import Order,OrderItem
from django.views.generic import View
from django.shortcuts import render,get_object_or_404,redirect
from onlinestore.models import Product


class Cart(View):
    '''Class to construct a view to display'''
    template_name='shoppingcart/cart_details.html'

    def get(self,request):
        user=request.user
        order,created=Order.objects.get_or_create(user=user,complete=False)
        items=order.orderitem_set.all()
        total=order.get_total()
        context={
            'product_list':items,
            'total':total
        }

        return render(request,self.template_name,context=context)








