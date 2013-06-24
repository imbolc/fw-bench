#!../var/env/bin/python
import os
from gevent import wsgi
import django.core.handlers.wsgi


wsgi.WSGIHandler.log_request = lambda *args, **kwargs: None
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
wsgi.WSGIServer(('', 8000), application).serve_forever()
