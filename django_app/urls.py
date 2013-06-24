from django.conf.urls import url, patterns


urlpatterns = patterns('views',
    url(r'^hello/$', 'hello', {'count': 1}, name='hello'),
    url(r'^table/$', 'table', {'col': None, 'row': None}, name='table'),
    url(r'^table/(?P<row>\d+)/(?P<col>\d+)/$', 'table', name='table'),
)
