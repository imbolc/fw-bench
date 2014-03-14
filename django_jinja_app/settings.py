DEBUG = False
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'urls'
SECRET_KEY = 'key'

TEMPLATE_LOADERS = (
    'jingo.Loader',
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
    )),
)

TEMPLATE_DIRS = (
    'templates',
)

INSTALLED_APPS = (
)

ALLOWED_HOSTS = '*'

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
            },
        }
    }
