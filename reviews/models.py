from django.db import models
from core.models import TimeStampedModel
from users.models import User
from books.models import Book
from movies.models import Movie


class Review(TimeStampedModel):

    """Review Model Definition"""

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, blank=True, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.text} - {self.created_by.username}"
