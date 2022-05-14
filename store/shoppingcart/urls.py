from .views import Cart,EditCart,DeleteItem,CartDelete
from django.urls import re_path

urlpatterns=[
    re_path(r'^$',Cart.as_view(),name='cart_details'),
    re_path(r'^(?P<pk>\d+)/edit/$',EditCart.as_view(),name='item_update'),
    re_path(r'^(?P<pk>\d+)/delete/$',DeleteItem.as_view(),name='item_delete'),
    re_path(r'^delete/$',CartDelete.as_view(),name='empty_cart'),

]