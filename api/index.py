import os
import sys

# Add the Django project to the path
project_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'client web', 'webbase')
if project_path not in sys.path:
    sys.path.insert(0, project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webbase.settings')

from django.core.wsgi import get_wsgi_application
app = application = get_wsgi_application()
