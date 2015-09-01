# noqa

# Standard Libs
import tempfile

# First Party Libs
from userservice.settings.base import *  # NOQA


SECRET_KEY = 's3cr3t k3y'

# CELERY_ALWAYS_EAGER = True
# CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

MEDIA_ROOT = tempfile.mkdtemp('media')

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
DEBUG = False
TEMPLATE_DEBUG = False
TESTS_IN_PROGRESS = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
