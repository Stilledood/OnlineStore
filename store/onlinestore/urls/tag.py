from django.urls import re_path
from ..views import TagList,TagDetails,TagAdd,TagUpdate,TagDelete

urlpatterns=[
    re_path(r'^$',TagList.as_view(),name='tag_list'),
    re_path(r'^(?P<slug>[\w\-]+)/$',TagDetails.as_view(),name='tag_details'),
    re_path(r'^add/$',TagAdd.as_view(),name='tag_add'),
    re_path(r'^(?P<slug>[\w\-]+)/change/$',TagUpdate.as_view(),name='tag_update'),
    re_path(r'^(?P<slug>[\w\-]+)/delete/$',TagDelete.as_view(),name='tag_delete'),
]