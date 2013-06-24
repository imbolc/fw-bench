#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, jsonify

app = application = Flask(__name__)
ROWS = [[{'row': row, 'col': col} for col in xrange(10)] for row in xrange(10)]

@app.route('/hello/')
def hello(count=1):
    return u'Hello, World!'


@app.route('/table/')
@app.route('/table/<int:row>/<int:col>/')
def table(row=None, col=None):
    return render_template('table.html', rows=ROWS)


if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
