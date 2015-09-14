# pragma: no cover
''' Used for QA the module is most similar to production environment.
'''

# First Party Libs
from userservice.settings.base import *  # NOQA


SECRET_KEY = 'hzwld6q^9*f@_8cwl02lv=q!pdifn3e$(f^0b#j-hu*d3kjkk^'

DEBUG = True
TEMPLATE_DEBUG = False
