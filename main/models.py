from django.db import models

"""
This file contains the database models for the application.

Models define the structure of the database tables and provide an interface to interact
with the database using Django's ORM (Object-Relational Mapping).
"""

class Song(models.Model):
    """
    A model to represent a song in the music catalog.

    Attributes:
    title (str): The title of the song.
    artist (str): The artist who performed the song.
    release_date (date): The release date of the song.
    """
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        """
        Return a string representation of the Song instance, which is its title.

        :returns: The title of the song.
        :rtype: str
        """
        return self.title
