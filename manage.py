#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """
    Run administrative tasks for the Django project.

    This function sets the default Django settings module, checks if Django
    is installed, and executes the command-line utility to handle various
    management commands like running the development server, migrations, etc.

    If Django is not installed or not found in the Python environment, an
    ImportError is raised with instructions to resolve the issue.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starry_nights.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
