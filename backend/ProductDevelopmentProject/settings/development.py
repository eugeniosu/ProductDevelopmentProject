# flake8: noqa
from ProductDevelopmentProject.settings.common import *

CORS_ORIGIN_ALLOW_ALL=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'dbname.c4vuzuooz2fe.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
