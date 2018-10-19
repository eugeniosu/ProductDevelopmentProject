from ProductDevelopmentProject.settings.common import *

CORS_ORIGIN_ALLOW_ALL=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '[dev_database_name]',
        'USER': '[dev_database_user]',
        'PASSWORD': 'dev_database_password',
        'HOST': 'dev_database_endpoint',
        'PORT': '5432',
    }
}
