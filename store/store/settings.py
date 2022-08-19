"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from .log_filters import ManagementFilter
from django.urls import reverse_lazy
import mimetypes

mimetypes.add_type("application/javascript", ".js", True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--7=l&93#ko*m-vaz=-v1_t09!x-2#j#pinuiw10b8fp&ca)i#_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'debug_toolbar',
    'crispy_forms',
    'onlinestore',
    'blog',
    'contact',
    'core',
    'user',
    'cart',
    'shoppingcart',



]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]


ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shoppingcart.context_procesor_file.get_cart_items',
            ],
        },
    },
]

FIXTURE_DIRS=(os.path.join(BASE_DIR,'fixtures'),)

WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
]
STATIC_ROOT='staticfiles'

#Media files setings
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL='contact@store.com'
DEFAULT_FROM_EMAIL='no_reply@store.com'
EMAIL_SUBJECT_PREFIX='[Store]'
MANAGERS=(
    ('Us','ourselves@store.com'),
)
# Flatpages and sites
SITE_ID=1

verbose=("[%(asctime)] %(levelname)s"
         "[%(name)s:%(lineno)s] %(message)s")

#LOGGING={
    #'version':1,
    ##'filters':{
        #'remove_migration_sql':{
            #'()':ManagementFilter

        #},
    #},
    #'handlers':{
        #'console':{
            #'class':'logging.StreamHandler'
       # }
   # },
    #'formatters':{
        #'verbose':{
            #'format':verbose,
            #'datefmt':"%Y-%b-%d %H:%M:%S"
        #}
    #},
    #'loggers':{
        #'django':{
            #'handlers':['console'],
            #'level':'DEBUG',
           # 'formatter':'verbose'
       # }
    #}
#}

# Authentification settings
LOGIN_URL=reverse_lazy('dj-auth:login')
LOGOUT_URL=reverse_lazy('dj-auth:logout')
LOGIN_REDIRECT_URL=reverse_lazy('general_view')
INTERNAL_IPS=[
    'localhost',
]

DEBUG_TOOLBAR_PATCH_SETTINGS = False


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}