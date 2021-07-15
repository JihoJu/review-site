from django.db import models
from django.contrib.auth.models import AbstractUser
from categories.models import Category


class User(AbstractUser):

    """User Model Definition"""

    # preference choices

    PREFERENCE_BOOK = "book"
    PREFERENCE_MOVIE = "movie"
    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOK, "Book"),
        (PREFERENCE_MOVIE, "Movie"),
    )

    # language choices

    LANGUAGE_KR = "kr"
    LANGUAGE_EN = "en"
    LANGUAGE_CHOICES = (
        (LANGUAGE_KR, "Korean"),
        (LANGUAGE_EN, "English"),
    )

    # book genre choices

    BOOK_GENRE_1 = "fantasy"
    BOOK_GENRE_2 = "mystery"
    BOOK_GENRE_3 = "thriller"
    BOOK_GENRE_CHOICES = (
        (BOOK_GENRE_1, "Fantasy"),
        (BOOK_GENRE_2, "Mystery"),
        (BOOK_GENRE_3, "Thriller"),
    )

    # movie genre choices

    MOVIE_GENRE_1 = "action"
    MOVIE_GENRE_2 = "comedy"
    MOVIE_GENRE_3 = "horror"
    MOVIE_GENRE_CHOICES = (
        (MOVIE_GENRE_1, "Action"),
        (MOVIE_GENRE_2, "Comedy"),
        (MOVIE_GENRE_3, "Horror"),
    )

    # User Model Field

    bio = models.TextField(null=True, default="")
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=10, null=True, default=PREFERENCE_BOOK
    )
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, default=LANGUAGE_KR
    )
    favorite_book_genre = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="book_genre",
    )
    favorite_movie_genre = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="movie_genre",
    )

    def __str__(self):
        return self.username
