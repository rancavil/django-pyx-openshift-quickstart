<<<<<<< HEAD
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

=======
#!/usr/bin/python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'openshift.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'openshift'))
>>>>>>> a85645bdc0a5b48fbaa72357a846ea1a408c3737

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
<<<<<<< HEAD


from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
=======
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

import django.core.wsgi
from dj_static import Cling

application = Cling(django.core.wsgi.get_wsgi_application())
>>>>>>> a85645bdc0a5b48fbaa72357a846ea1a408c3737
