from django.urls import path,re_path,include
from .views import CategoryList

urlpatterns=[
    re_path(r'^categories/$',CategoryList.as_view(),name='category-list'),
]