from django.db import models
from core.models import TimeStampedModel
from users.models import User
from books.models import Book
from movies.models import Movie


class FavList(TimeStampedModel):

    """FavList Model Definition"""

    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    movies = models.ManyToManyField(Movie)

    class Meta:
        verbose_name_plural = "Favorite Lists"

    def __str__(self):
        return self.created_by.username

    def books_count(self):
        return self.books.count()

    def movies_count(self):
        return self.movies.count()
