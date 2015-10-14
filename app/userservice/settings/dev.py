# pragma: no cover
''' Used for local testing. Module shouldn't use any external services like
storages or shared cached.
'''

# Standard Libs
import tempfile

# First Party Libs
from userservice.settings.base import *  # NOQA


SECRET_KEY = 'hzwld6q^9*f@_8cwl02lv=q!pdifn3e$(f^0b#j-hu*d3kjkk^'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(tempfile.mkdtemp(), 'media/')
