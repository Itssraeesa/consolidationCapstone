from django.apps import AppConfig

"""
This file contains the application configuration for the Django project.

The `AppConfig` class is used to configure the application and its settings.
"""

class MainConfig(AppConfig):
    """
    Configuration class for the 'main' app.

    :ivar str default_auto_field: Specifies the type of primary key to use for models.
    :ivar str name: The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

