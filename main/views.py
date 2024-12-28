from django.shortcuts import render
from .models import Song

def home(request):
    """
    Renders the home page of the website.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'main/home.html')

def about(request):
    """
    Renders the about page of the website.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered about page.
    """
    return render(request, 'main/about.html')

def songs(request):
    """
    Retrieves all the songs from the database and renders the songs page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered songs page with a list of songs.
    """
    songs = Song.objects.all()
    return render(request, 'main/songs.html', {'songs': songs})

