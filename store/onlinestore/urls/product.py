from django.urls import re_path
from ..views import ProductList,ProductDetails

urlpatterns=[
    re_path(r'^$',ProductList.as_view(),name='product_list'),
    re_path(r'^(?P<pk>\d+)/$',ProductDetails.as_view(),name='product_details'),
]