"""
WSGI config for openshift project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openshift.settings")
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],'openshift'))

PYTHON_VERSION = os.environ['OPENSHIFT_PYTHON_VERSION']

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    if PYTHON_VERSION == '2.7':
         execfile(virtualenv, dict(__file__=virtualenv))
    else:
         exec(compile(open(virtualenv).read(), virtualenv, 'exec'),dict(__file__ = virtualenv))
except IOError:
    pass


from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
