from django.shortcuts import render,redirect
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import get_user,logout
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect


class DisableAccount(View):
    '''Class to build a view to disable a user account'''

    success_url=settings.LOGIN_REDIRECT_URL
    template_name='user/disable_account.html'

    @method_decorator(login_required)
    @method_decorator(csrf_protect)
    def get(self,request):
        return TemplateResponse(request,self.template_name)

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def post(self,request):
        user=get_user(request)
        user.set_unusable_password()
        user.is_active=False
        user.save()
        logout(request)
        return redirect(self.success_url)

    


