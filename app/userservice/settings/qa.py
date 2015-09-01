# noqa
# Standard Libs
import os

# First Party Libs
from userservice.settings.base import *  # NOQA


SECRET_KEY = 'hzwld6q^9*f@_8cwl02lv=q!pdifn3e$(f^0b#j-hu*d3kjkk^'

DEBUG = True
TEMPLATE_DEBUG = False
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SECURE_URLS = os.environ.get('AWS_S3_SECURE_URLS')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': os.environ.get('REDIS'),
        'OPTIONS': {
            'DB': 1,
        },
    },
}
