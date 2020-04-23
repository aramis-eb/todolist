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

DB_FROM_ENV = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(DB_FROM_ENV)

# INSTALLED_APPS += [  # noqa
#     'whitenoise.runserver_nostatic'
# ]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEBUG = False
