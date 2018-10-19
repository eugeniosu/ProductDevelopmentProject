# flake8: noqa
from ProductDevelopmentProject.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['[ALLOWED_HOST]',]
CORS_ORIGIN_ALLOW_ALL=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '[DBName]',
        'USER': '[DBUsername]',
        'PASSWORD': '[DBPassword]',
        'HOST': '[DBEndpoint]',
        'PORT': '5432',
    }
}
