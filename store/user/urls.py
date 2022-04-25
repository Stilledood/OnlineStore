from django.urls import re_path,reverse_lazy,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView
from .views import DisableAccount


app_name='user'

#Password related url's
password_urls=[
    re_path(r'^change/$',auth_views.PasswordChangeView.as_view(template_name='user/password_change.html',success_url=reverse_lazy('dj-auth:password_change_done')),name='password_change'),
    re_path(r'^change/done/$',auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html',extra_context={'form':AuthenticationForm}),name='password_change_done'),
    re_path(r'^reset/$',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html',email_template_name='user/email_template.txt',subject_template_name='user/subject_template.txt',success_url=reverse_lazy('dj-auth:password_reset_done')),name='password_reset'),
    re_path(r'^reset/done/$',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    re_path(r'^reset/'
            r'(?P<uidb64>[0-9A-Za-z-\-]+)/'
            r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',success_url=reverse_lazy('dj-auth:password_reset_complete')),name='password_reset_confirm'),
    re_path(r'^reset/complete/$',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html',extra_context={'form':AuthenticationForm}),name='password_reset_complete'),



]


#User url's
urlpatterns=[
    re_path(r'^$',RedirectView.as_view(pattern_name='dj-auth:login',permanent=False)),
    re_path(r'^login/$',auth_views.LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm),name='login'),
    re_path(r'^logout/$',auth_views.LogoutView.as_view(template_name='user/logout.html',extra_context={'form':AuthenticationForm}),name='logout'),
    re_path(r'^password/',include(password_urls)),
    re_path(r'^dissable/$',DisableAccount.as_view(),name='dissable_account'),


]