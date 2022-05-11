from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    '''Class to create a form for sign up process'''

    first_name=forms.CharField(max_length=64,required=False,help_text='optional')
    last_name=forms.CharField(max_length=64,required=False,help_text='optional')
    email=forms.EmailField(max_length=255)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']



class ProfileForm(forms.ModelForm):
    '''Class to construct a form for Profile model'''

    class Meta:
        model=Profile
        fields='__all__'

