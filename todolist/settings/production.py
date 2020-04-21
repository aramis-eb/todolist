from .base import *
import dj_database_url

ALLOWED_HOSTS = [
    'todo-list-app-ar.herokuapp.com'
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todolist',
        'USER': 'name',
        'PASSWORD': '',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static_prod')

INSTALLED_APPS += [  # noqa
    'whitenoise.runserver_nostatic'
]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DB_FROM_ENV = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(DB_FROM_ENV)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

DEBUG = False
