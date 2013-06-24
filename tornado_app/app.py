from tornado import web


ROWS = [[{'row': row, 'col': col} for col in xrange(10)] for row in xrange(10)]


class HelloHandler(web.RequestHandler):
    def get(self):
        self.write('Hello, World!')


class TableHandler(web.RequestHandler):
    def get(self, row=None, col=None):
        self.render('templates/table.html', rows=ROWS)


handlers = [
    (r"/hello/", HelloHandler),
    (r'^/table/$', TableHandler),
    web.URLSpec(r'^/table/(\d+)/(\d+)/$', TableHandler, name='table'),
]


application = web.Application(handlers)
