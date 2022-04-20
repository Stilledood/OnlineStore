from django.urls import re_path
from ..views import TagList,TagDetails

urlpatterns=[
    re_path(r'^$',TagList.as_view(),name='tag_list'),
    re_path(r'^(?P<slug>[\w\-]+)/$',TagDetails.as_view(),name='tag_details'),
]