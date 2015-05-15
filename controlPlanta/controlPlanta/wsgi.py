"""
WSGI config for controlPlanta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('/Volumes/DATOS/Avanzando_Juntos/Avanzando/avanzando/avanzando/')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/Volumes/DATOS/Avanzando_Juntos/Avanzando/venv/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controlPlanta.settings")

application = get_wsgi_application()
