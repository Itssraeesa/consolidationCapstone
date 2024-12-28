from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Song

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def songs(request):
    songs = Song.objects.all()
    return render(request, 'main/songs.html', {'songs': songs})