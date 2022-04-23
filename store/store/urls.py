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


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^store/',include(product)),
    re_path(r'^tag/',include(tag)),
    re_path(r'^category/',include(category)),
    re_path(r'^user/',include(user_urls,namespace='dj-auth')),
    re_path(r'^blog/',include(blog_urls)),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
