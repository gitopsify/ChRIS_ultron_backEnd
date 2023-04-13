# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

import ldap
from django_auth_ldap.config import LDAPSearch
from .common import *  # noqa

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w1kxu^l=@pnsf!5piqz6!!5kdcdpo79y6jebbp+2244yjm*#+k'

# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# LOGGING CONFIGURATION
# See https://docs.djangoproject.com/en/4.0/topics/logging/ for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s]'
                      '[%(name)s][%(filename)s:%(lineno)d %(funcName)s] %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] [%(levelname)s]'
                      '[%(module)s %(process)d %(thread)d] %(message)s'
        },
    },
    'handlers': {
        'console_verbose': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'console_simple': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
            'formatter': 'simple'
        }
    },
    'loggers': {
        '': {  # root logger
            'level': 'INFO',
            'handlers': ['console_simple'],
        },
    }
}

for app in ['collectionjson', 'core', 'feeds', 'plugins', 'plugininstances', 'pipelines',
            'pipelineinstances', 'uploadedfiles', 'pacsfiles', 'servicefiles', 'users',
            'filebrowser', 'workflows']:
    LOGGING['loggers'][app] = {
            'level': 'DEBUG',
            'handlers': ['console_verbose', 'file'],
            'propagate': False  # required to avoid double logging with root logger
        }

# Swift service settings
# DEFAULT_FILE_STORAGE = 'swift.storage.SwiftStorage'
# SWIFT_AUTH_URL = 'http://swift_service:8080/auth/v1.0'
AWS_S3_HOST = "127.0.0.1"
AWS_S3_PORT = "4566"
AWS_S3_ENDPOINT_URL = f"http://{AWS_S3_HOST}:{AWS_S3_PORT}"

AWS_ACCESS_KEY_ID = 'foobar'
AWS_SECRET_ACCESS_KEY = 'foobar'
AWS_STORAGE_BUCKET_NAME = 'chrisbucket'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_VERIFY = False
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    'ACL': 'public-read-write',
}
AWS_QUERYSTRING_AUTH = False

AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'core.swiftmanager.StaticStorage'
STATIC_URL = "http://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

AWS_PUBLIC_MEDIA_LOCATION = ''
MEDIA_URL = "http://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_PUBLIC_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'core.swiftmanager.SwiftManager'

# SWIFT_USERNAME = 'chris:chris1234'
# SWIFT_KEY = 'testing'
# SWIFT_CONTAINER_NAME = 'users'
# SWIFT_CONNECTION_PARAMS = {'user': SWIFT_USERNAME,
#                            'key': SWIFT_KEY,
#                            'authurl': SWIFT_AUTH_URL}
# try:
#     SwiftManager(SWIFT_CONTAINER_NAME, SWIFT_CONNECTION_PARAMS).create_container()
# except Exception as e:
#     raise ImproperlyConfigured(str(e))

# ChRIS store settings
CHRIS_STORE_URL = 'http://chris-store.local:8010/api/v1/'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
import sys

if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['NAME'] = 'mydatabase'
else:
    # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
    DATABASES['default']['NAME'] = 'chris_dev'
    DATABASES['default']['USER'] = 'chris'
    DATABASES['default']['PASSWORD'] = 'Chris1234'
    DATABASES['default']['TEST'] = {'NAME': 'test_chris_dev'}
    DATABASES['default']['HOST'] = 'chris_dev_db'
    DATABASES['default']['PORT'] = '5432'

#DATABASES['default']['NAME'] = 'chris_dev'
#DATABASES['default']['USER'] = 'chris'
#DATABASES['default']['PASSWORD'] = 'Chris1234'
#DATABASES['default']['TEST'] = {'NAME': 'test_chris_dev'}
#DATABASES['default']['HOST'] = 'chris_dev_db'
#DATABASES['default']['PORT'] = '5432'

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar']

INTERNAL_IPS = ['127.0.0.1',]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions']

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

COMPUTE_RESOURCE_URL = 'http://pfcon.remote:30005/api/v1/'

# corsheaders
# ------------------------------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True
CORS_EXPOSE_HEADERS = ['Allow', 'Content-Type', 'Content-Length']


# Celery settings

#CELERY_BROKER_URL = 'amqp://guest:guest@localhost'
CELERY_BROKER_URL = 'amqp://queue:5672'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Worker settings
# messages to prefetch at a time multiplied by the number of concurrent processes
# default is 4 (four messages for each process)
CELERYD_PREFETCH_MULTIPLIER = 2


# LDAP auth configuration
AUTH_LDAP = False
if AUTH_LDAP:
    AUTH_LDAP_SERVER_URI = 'ldap://192.168.0.29:389'
    AUTH_LDAP_BIND_DN = 'cn=admin,dc=fnndsc,dc=org'
    AUTH_LDAP_BIND_PASSWORD = 'admin1234'
    AUTH_LDAP_USER_SEARCH_ROOT = 'dc=fnndsc,dc=org'

    AUTH_LDAP_USER_SEARCH = LDAPSearch(AUTH_LDAP_USER_SEARCH_ROOT, ldap.SCOPE_SUBTREE,
                                       '(uid=%(user)s)')
    AUTH_LDAP_USER_ATTR_MAP = {
        'first_name': 'givenName',
        'last_name': 'sn',
        'email': 'mail'
    }
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )