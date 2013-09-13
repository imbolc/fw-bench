import logging

from django.http import HttpResponse
from django.shortcuts import render


logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')


ROWS = [[{'row': row, 'col': col} for col in xrange(10)] for row in xrange(10)]


def hello(request, count):
    return HttpResponse(u'Hello, World!')


def table(request, row, col):
    return render(request, 'table.html', {
        'rows': ROWS })
