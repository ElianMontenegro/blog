from .base import *

DEBUG = True

ALLOWED_HOSTS = ['blogprodigy.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'d9pok7grnkjus8',
        'USER': 'epjggjlchyjqqc',
        'PASSWORD': '21ee8e66f5ed58098b6ceb6cf65324725cfcb1871381c9bdb0bda752851a26b4',
        'HOST': 'ec2-3-95-124-37.compute-1.amazonaws.com',
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