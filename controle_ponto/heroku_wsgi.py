"""WSGI module."""

import os

from django.core import wsgi
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controle_ponto.settings")
application = DjangoWhiteNoise(wsgi.get_wsgi_application())
