"""
WSGI config for ntavelos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import sys
import os

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                'ntavelos')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ntavelos.settings")

application = get_wsgi_application()
