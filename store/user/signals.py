from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.contrib.messages import success
from django.dispatch import receiver

@receiver(user_logged_in)
def display_login_message(sender,**kwargs):
    '''Function to create a signal to display a succes message when the user log in'''

    request=kwargs.get('request')
    user=kwargs.get('user')
    success(request,'Successfully logged in as {}'.format(user.get_username()),fail_silently=True)


@receiver(user_logged_out)
def display_logout_message(sender,**kwargs):
    '''Function to create a signal to display a succes message when the user log out'''

    request=kwargs.get('request')
    success(request,'Successfully logged out',fail_silently=True)


