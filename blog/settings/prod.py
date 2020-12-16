from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dbblog2',
        'USER': 'elian',
        'PASSWORD': 'OLAVARRIA18491',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

CKEDITOR_UPLOAD_PATH = 'uploads/'
TOR_IMAGE_BACKEND = 'pillow'
TOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}