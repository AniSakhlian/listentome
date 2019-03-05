"""
WSGI config for listentome project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

import dotenv
from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv()

settings_file = 'production'
if os.environ.get('IS_LOCAL') == 'True':
    settings_file = 'local'
elif os.environ.get('IS_DEVELOPMENT') == 'True':
    settings_file = 'development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'listentome.settings.' + settings_file)
application = get_wsgi_application()
