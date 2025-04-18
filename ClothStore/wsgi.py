"""
WSGI config for ClothStore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# import accounts.management.commands.initialize as initialize
# initialize.run()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ClothStore.settings')

application = get_wsgi_application()
