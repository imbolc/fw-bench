#!../var/env/bin/python
from gevent import wsgi
from app import application


wsgi.WSGIHandler.log_request = lambda *args, **kwargs: None
wsgi.WSGIServer(('', 8000), application).serve_forever()
