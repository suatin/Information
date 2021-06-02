"""
WSGI config for ProjectList project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('path/to/yourprojectenv/lib/python3.8/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectList.settings')

application = get_wsgi_application()
