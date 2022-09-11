from django.urls import path,re_path,include
from .views import CategoryList,ProductDetails,CategoryDetails,ProductList,PostList,PostDetails,ApiRootView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import  include_docs_urls




urlpatterns=[


    re_path(r'^$',ApiRootView.as_view(),name='api_root'),
    re_path(r'^categories/$',CategoryList.as_view(),name='category-list'),
    path('categories/<int:pk>/',CategoryDetails.as_view(),name='category-detail'),
    path('<int:pk>/',ProductDetails.as_view(),name='product-detail'),
    re_path('^products/$',ProductList.as_view(),name='product-list'),
    re_path('^blogs/$',PostList.as_view(),name='post-list'),
    path('blogs/<int:pk>',PostDetails.as_view(),name='post-detail')
]