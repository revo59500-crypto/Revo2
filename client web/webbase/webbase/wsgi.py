"""
WSGI config for webbase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add the project directory and parent directories to the sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
root_dir = os.path.dirname(os.path.dirname(project_dir))

for path in [current_dir, project_dir, root_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webbase.settings')

application = get_wsgi_application()

# Vercel requires the app variable
app = application
