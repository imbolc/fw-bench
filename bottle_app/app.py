import bottle
#from bottle import jinja2_template as template
from bottle import template


app = application = bottle.Bottle()
ROWS = [[{'row': row, 'col': col} for col in xrange(10)] for row in xrange(10)]
bottle.TEMPLATE_PATH = ['templates']


@app.route('/hello/')
def index():
    return u'Hello, World!'


@app.route('/table/')
@app.route('/table/<row:int>/<col:int>/', name='table')
def table(row=None, col=None):
    return template('table.html', url_for=app.get_url, rows=ROWS)
