"""
Django settings for openshift project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import imp, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# If ON_OPEJNSHIFT is True , run on production!
ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
     ON_OPENSHIFT = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
default_keys = {'SECRET_KEY':'6m3z#_st@jp)(8gd4tt@l%%6e-$00237zd+m#gcnbx!en)=8t('}
use_keys = default_keys
if ON_OPENSHIFT:
     sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],'openshift','openshift'))
     imp.find_module('openshiftlibs')
     import openshiftlibs
     use_keys = openshiftlibs.openshift_secure(default_keys)  

SECRET_KEY = use_keys['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
if ON_OPENSHIFT:
     DEBUG = False
     ALLOWED_HOSTS = ['*']
else:
     DEBUG = True
     ALLOWED_HOSTS = []

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
     os.path.join(BASE_DIR,'templates'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'openshift.urls'

WSGI_APPLICATION = 'openshift.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if ON_OPENSHIFT:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'db.sqlite3'),
         }
     }
else:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         }
     }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
