from django.urls import path
from . import views

"""
URL configuration for the main app.

This file maps URLs to the appropriate view functions in the `views.py` file.
Each entry in `urlpatterns` connects a specific URL pattern to a corresponding
view function, enabling navigation and functionality within the application.
"""

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs, name='songs'),
]

