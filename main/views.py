from django.shortcuts import render
from .models import Song

def home(request):
    """
    This method will be used to render the home page of the website

        :param request: The HTTP request object

        :returns: The rendered home page

        :rtype: HttpResponse
    """
    return render(request, 'main/home.html')

def about(request):
    """
    This method will be used to render the about page of the website

        :param request: The HTTP request object

        :returns: The rendered about page

        :rtype: HttpResponse
    """
    return render(request, 'main/about.html')

def songs(request):
    """
    This method will be used to retrieve all the songs from the database and render the songs page

        :param request: The HTTP request object

        :returns: The rendered songs page with a list of songs

        :rtype: HttpResponse
    """
    songs = Song.objects.all()
    return render(request, 'main/songs.html', {'songs': songs})

