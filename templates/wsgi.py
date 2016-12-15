import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'graphite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
