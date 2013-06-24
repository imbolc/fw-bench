from pysi import App, view


ROWS = [[{'row': row, 'col': col} for col in xrange(10)] for row in xrange(10)]


@view('/hello/')
def hello(rq):
    return u'Hello, World!'


@view('/table/')
@view('/table/<int:row>/<int:col>/', 'table.html')
def table(rq, row=None, col=None):
    return {'rows': ROWS}


application = App()
