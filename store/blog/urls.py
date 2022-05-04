from django.urls import re_path
from .views import PostList,PostDetails,PostAdd,PostUpdate,PostDelete



urlpatterns=[
    re_path(r'^$',PostList.as_view(),name='post_list'),
    re_path(r'^(?P<pk>\d+)/$',PostDetails.as_view(),name='post_details'),
    re_path(r'^add/$',PostAdd.as_view(),name='post_add'),
    re_path(r'^(?P<pk>\d+)/chnage/$',PostUpdate.as_view(),name='post_change'),
    re_path(r'^(?P<pk>\d+)/delete/$',PostDelete.as_view(),name='post_delete'),
]