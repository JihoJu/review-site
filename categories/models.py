from django.db import models
from core.models import TimeStampedModel


class Category(TimeStampedModel):

    """Category Model Definition"""

    # Kind Field Choices

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"
    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=10, blank=True)
    kind = models.CharField(choices=KIND_CHOICES, max_length=10, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
