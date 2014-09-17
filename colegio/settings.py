"""
Django settings for colegio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
 


import os
from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e8c#54y2w8$&kzuhd6f(4c1510k4)xw#bw^!v(qaym$rrd8f0+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'apps.principal',
    'apps.configuracion', 
    'apps.finanzas',
    'apps.maestro',
    'apps.trasporte',
    'djrill',    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'colegio.urls'

WSGI_APPLICATION = 'colegio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-Mex'
 
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
#TEMPLATE_DIRS = os.path.join(BASE_DIR,'templates')


STATIC_URL = '/static/'
TEMPLATE_DIRS = [BASE_DIR.child('templates')]
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
 
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = 'http://localhost:8000/media/'


STATIC_ROOT = 'staticfiles'             

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY ='WeikEnaOZGN5itibGAs_0g'
 