from django.urls import re_path
from ..views import ProductList,ProductDetails,ProductAdd,ProductUpdate,ProductDelete

urlpatterns=[
    re_path(r'^$',ProductList.as_view(),name='product_list'),
    re_path(r'^(?P<pk>\d+)/$',ProductDetails.as_view(),name='product_details'),
    re_path(r'^add/$',ProductAdd.as_view(),name='product_add'),
    re_path(r'^(?P<pk>\d+)/change/$',ProductUpdate.as_view(),name='product_update'),
    re_path(r'^(?P<pk>\d+)/delete/$',ProductDelete.as_view(),name='product_delete'),
]