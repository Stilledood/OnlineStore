from .models import Order
from django.shortcuts import get_object_or_404


def get_cart_items(request):
    user=request.user
    order=[]
    if user.is_authenticated:
        order=get_object_or_404(Order,user=user)
    cart_items=[]
    try:
        cart_items=order.orderitem_set.all()
    except:
        pass

    return {
        'order':order,
        'cart_items':cart_items
    }
