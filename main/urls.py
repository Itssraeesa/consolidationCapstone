from django.urls import path
from . import views

# URL configuration for the main app.
# This file maps URLs to the appropriate view functions.

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs, name='songs'),
]

