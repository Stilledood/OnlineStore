from django.urls import re_path,path
from .views import CategoryList,CategoryDetails,ProductDetails,ProductList,TagList,TagDetails


urlpatterns=[
    re_path(r'^$',ProductList.as_view(),name='product_list'),
    re_path(r'^(?P<pk>\d+)/$',ProductDetails.as_view(),name='product_details'),
    re_path(r'^categories/$',CategoryList.as_view(),name='category_list'),
    re_path(r'^category/(?P<slug>[\w\-]+)/$',CategoryDetails.as_view(),name='category_details'),
    re_path(r'^tags/$',TagList.as_view(),name='tag_list'),
    re_path(r'tags/(?P<slug>[\w\-]+)/$',TagDetails.as_view(),name='tag_details'),
]