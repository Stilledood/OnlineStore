"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from onlinestore.urls import category,product,tag
from django.contrib.flatpages import urls as flatpages_urls
from django.conf import settings
from django.conf.urls.static import static
from blog import urls as blog_urls
from user import urls as user_urls
from blog.feeds import AtomPostFeed,RssPostFeed
from .sitemaps import sitemaps
from django.contrib.sitemaps.views import index,sitemap as sitemap_view
from .views import GeneralView
from shoppingcart import urls as cart_urls
from contact import urls as contact_urls
from api import urls as api_urls
from rest_framework import urls as rest_urls



sitenews=[
    re_path(r'^atom/$',AtomPostFeed(),name='blog_atom_feed'),
    re_path(r'^rss/$',RssPostFeed(),name='blog_rss_feed'),
]

urlpatterns = [
    path('',GeneralView.as_view(),name='general_view'),
    path('admin/', admin.site.urls),
    re_path(r'^store/',include(product)),
    re_path(r'^tag/',include(tag)),
    re_path(r'^category/',include(category)),
    re_path(r'^user/',include(user_urls,namespace='dj-auth')),
    re_path(r'^blog/',include(blog_urls)),
    re_path(r'^cart/',include(cart_urls)),
    re_path(r'^contact/',include(contact_urls)),
    re_path(r'^sitenews/',include(sitenews)),
    re_path(r'^sitemap.xml$',sitemap_view,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^api/',include(api_urls)),
    path('api_auth/',include(rest_urls))






]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns+=[
        re_path(r'^__debug__/',include(debug_toolbar.urls))
    ]

admin.site.site_header='Store Admin Panel'
admin.site.site_title='Store Admin'

