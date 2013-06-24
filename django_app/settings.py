DEBUG = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'urls'
SECRET_KEY = 'key'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
    )),
)

TEMPLATE_DIRS = (
    'templates',
)

INSTALLED_APPS = (
)
