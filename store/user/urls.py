from django.urls import re_path,reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView


app_name='user'

urlpatterns=[
    re_path(r'^$',RedirectView.as_view(pattern_name='dj-auth:login',permanent=False)),
    re_path(r'^login/$',auth_views.LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm),name='login'),
    re_path(r'^logout/$',auth_views.LogoutView.as_view(template_name='user/logout.html',extra_context={'form':AuthenticationForm}),name='logout')

]