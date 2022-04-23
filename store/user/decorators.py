from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required,permission_required
from django.core.exceptions import ImproperlyConfigured


def custom_login_required(cls):
    '''Function to create a custom login to decorate class dispatch method'''
    if (not isinstance(cls,type) or not issubclass(cls,View)):
        raise ImproperlyConfigured('custom_login_required must be applied on View subclass')

    decorator=method_decorator(login_required)
    cls.dispatch=method_decorator(cls.dispatch)
    return cls


def custom_permission_required(permission):
    '''Function to create a custom permission required '''

    def decorator(cls):
        if (not isinstance(cls,type) or not issubclass(cls,View)):
            raise ImproperlyConfigured('custom_permission_required must be applied on subclass of View class')
        check_auth=method_decorator(login_required)
        check_perm=method_decorator(permission_required(permission,raise_exception=True))
        cls.dispatch=check_auth(check_perm(cls.dispatch))
        return cls

    return decorator


