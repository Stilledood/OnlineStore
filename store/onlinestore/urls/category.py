from django.urls import re_path
from ..views import CategoryList,CategoryDetails,CategoryAdd,CategoryChange,CategoryDelete

urlpatterns=[
    re_path(r'^$',CategoryList.as_view(),name='category_list'),
    re_path(r'^(?P<slug>[\w\-]+)/$',CategoryDetails.as_view(),name='category_details'),
    re_path(r'^add/$',CategoryAdd.as_view(),name='category_add'),
    re_path(r'^(?P<slug>[\w\-]+)/change/$',CategoryChange.as_view(),name='category_change'),
    re_path(r'^(?P<slug>[\w\-]+)/delete/$',CategoryDelete.as_view(),name='category_delete'),
]