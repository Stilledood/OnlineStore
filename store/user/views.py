from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import get_user,logout
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm,ProfileForm
from .models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import account_activation
from django.contrib import messages
from django.contrib.auth.models import User

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



class SignUp(View):
    '''Class to construct a view for Sign Up Process'''

    form_class=SignUpForm
    template_name='user/signup.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})



    def post(self,request,*args,**kwargs):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            user=bound_form.save(commit=False)
            user.is_active=False
            user.save()
            Profile.objects.update_or_create(user=user,defaults={'username':user.get_username()})
            current_site=get_current_site(request)
            subject='Activate your account'
            message=render_to_string('user/account_activation_email.html',
                                     {'user':user,
                                      'domain':current_site.domain,
                                      'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                      'token':account_activation.make_token(user)})
            user.email_user(subject,message)
            messages.success(request,'Please Confirm your email')
            return redirect('dj-auth:login')
        else:
            return render(request,self.template_name,{'form':bound_form})


class AccountActivation(View):
    '''Class to construct a view for account activation'''

    def get(self,request,uidb64,token,*args,**kwargs):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except (TypeError,ValueError,OverflowError):
            user=None

        if (user != None and account_activation.check_token(user,token)):
            user.is_active=True
            user.profile.email_confirmed=True
            user.save()
            Profile.objects.update_or_create(user=user,defaults={''})
            return redirect('dj-auth:login')
        else:
            messages.warning(request,'Confirmation link is no longer valid')
            return redirect('dj-auth:signup')

class ProfileDetails(View):
    '''Class to create a view to display user profile'''

    model=Profile
    template_name='user/profile.html'

    def get(self,request,username):
        profile=get_object_or_404(self.model,username=username)
        return render(request,self.template_name,{'profile':profile})


class ProfileUpdate(View):
    '''Class to create a view to update profile informations'''

    model=Profile
    template_name='user/profile_change.html'
    form_class=ProfileForm

    def get(self,request,username):
        profile=get_object_or_404(self.model,username=username)
        return  render(request,self.template_name,{'form':self.form_class(instance=profile)})

    def post(self,request,username):

        profile=get_object_or_404(self.model,username=username)
        bound_form=self.form_class(request.POST,request.FILES,instance=profile)

        if bound_form.is_valid():
            print(True)


            new_profile=bound_form.save()
            return redirect(new_profile.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form})






