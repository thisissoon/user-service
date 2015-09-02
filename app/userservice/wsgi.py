"""
WSGI config for userservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# Standard Libs
import os

# Third Party Libs
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "userservice.settings.dev")

application = get_wsgi_application()
