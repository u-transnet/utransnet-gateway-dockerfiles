import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "utransnetgateway.settings")
django.setup()

from auth_custom.models import User
User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'change_me', phone='+79771319799')