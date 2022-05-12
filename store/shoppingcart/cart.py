from .models import CartItem
from onlinestore.models import Product
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.db.models import Max
from datetime import datetime,timedelta
import decimal import random

CART_ID_SESSION_KEY='cart_id'


def _cart_id(request):
    '''Get the curent user cart id ,if no cart iid exists sets new one to blank'''

    if request.session.get(CART_ID_SESSION_KEY) == '':
        request.session[CART_ID_SESSION_KEY]= _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]


def _generate_cart_id():
    '''function to generate random cart id numbers'''
    cart_id=''
    characters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_lenght=50
    for y in range(cart_id_lenght):
        cart_id+=characters.[random.randint(0,len(characters)-1)]
    return cart_id

def get_cart_items(request):
    '''Return all items from cart'''

    return CartItem.objects.filter(cart_id=_cart_id(request))



def add_to_cart(request):
    '''Fynction that takes a POST request and adds a product to the cart'''

    postdata=request.POST.copy()
    product_pk=postdata.get('product_pk','')
    quantity=postdata.get('quantity',1)
    product=get_object_or_404(Product,pk=pk)
    cart_products=get_cart_items(request)
    product_in_cart=False

    for cart_product in cart_products:
        if cart_product.id == p.id:
            # Update de quantity
            cart_product.augment_qunayity(quantity)
            product_in_cart=True
        if not product_in_cart:
            ci=CartItem()
            ci.product=product
            ci.quantity=quantity
            ci.cart_id= _cart_id(request)
            ci.save()


def get_single_item(request,item_id):
    return get_object_or_404(CartItem,id=item_id,cart_id=_cart_id(request))


def update_cart(request):
    '''Function that take a POST request and updates quantity for a single item in cart'''

    postdata=request.POST.copy()
    quantity=postdata['quantity']
    item_id=postdata['item_id']
    cart_item=get_single_item(request,item_id)
    if cart_item:
        if int(quantity) >0:
            cart_item.quantity=int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request)

def remove_from_cart(request):
    '''Function to remove a single item from cart'''
    postdata=request.POST.copy()
    item_id=postdata['item_id']
    cart_item=get_single_item(request,item_id)
    if cart_item:
        cart_item.delete()

def cart_subtotal(request):
    '''Subtotal of curent cart'''
    cart_total=decimal.Decimal('0.00')
    cart_products=get_cart_items(request)
    for cart_item in cart_products:
        cart_total+=cart_item.product.price*cart_item.quantity
    return cart_total

def empty_cart(request):
    '''Empties the shopping cart'''
    user_cart=get_cart_items(request)
    user_cart.delete()






