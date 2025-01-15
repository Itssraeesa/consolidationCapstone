"""
This method will be used to configure ASGI for the Starry Nights project.

    :param os.environ: The environment variable to set the Django settings module

    :returns: The ASGI application callable for the project

    :rtype: ASGI application
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starry_nights.settings')

application = get_asgi_application()

