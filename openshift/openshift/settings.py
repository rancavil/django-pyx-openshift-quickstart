"""
Django settings for openshift project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import imp

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
     ON_OPENSHIFT = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
default_keys = {'SECRET_KEY' : '^0fh6^_hm7gozkps9k#n#c)pyxemws41^83%od_-ni3cfps9#-'}
use_keys = default_keys
if ON_OPENSHIFT:
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

TEMPLATE_DEBUG = DEBUG

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
STATICFILES_DIRS = (
     os.path.join(BASE_DIR,'..','static'),
)
STATIC_ROOT = os.path.join(BASE_DIR,'..','static')
STATIC_URL = '/static/'
