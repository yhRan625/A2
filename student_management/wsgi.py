"""
WSGI config for student_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# Importing the os module
import os

# Importing the get_wsgi_application function from Django's core WSGI module
from django.core.wsgi import get_wsgi_application

# Setting the default value for the DJANGO_SETTINGS_MODULE environment variable to 'student_management.settings'
# This tells Django where to find the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')

# Creating a WSGI application object using the get_wsgi_application function
# This application object is used by WSGI servers to forward requests to
application = get_wsgi_application()
