# flake8: noqa
from ProductDevelopmentProject.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['w4iug6fbrf.execute-api.us-east-1.amazonaws.com',]
CORS_ORIGIN_ALLOW_ALL=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatahack',
        'USER': 'mydatahack',
        'PASSWORD': 'mydatahackrocks',
        'HOST': 'postgres-rds.c4vuzuooz2fe.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
