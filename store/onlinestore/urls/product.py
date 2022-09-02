from django.urls import re_path,include
from ..views import ProductList,ProductDetails,ProductAdd,ProductUpdate,ProductDelete,search_products
from ..feeds import AtomFeed,RssFeed

storenews=[
    re_path(r'^atom/$',AtomFeed(),name='products_atom_feed'),
    re_path(r'^rss/$',RssFeed(),name='products_rss_feed'),

]

urlpatterns=[
    re_path(r'^$',ProductList.as_view(),name='product_list'),
    re_path(r'^(?P<pk>\d+)/$',ProductDetails.as_view(),name='product_details'),
    re_path(r'^add/$',ProductAdd.as_view(),name='product_add'),
    re_path(r'^(?P<pk>\d+)/change/$',ProductUpdate.as_view(),name='product_update'),
    re_path(r'^(?P<pk>\d+)/delete/$',ProductDelete.as_view(),name='product_delete'),
    re_path(r'^search/$',search_products,name='search'),
    re_path(r'^storenews/',include(storenews))
]