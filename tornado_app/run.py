#!../var/env/bin/python
import tornado.ioloop
from app import application

application.listen(8000)
tornado.ioloop.IOLoop.instance().start()
