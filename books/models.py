from django.db import models
from core.models import TimeStampedModel
from categories.models import Category
from people.models import Person


class Book(TimeStampedModel):

    """Book Model Definition"""

    title = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(null=True, upload_to="book_images")
    rating = models.IntegerField(null=True)
    writer = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
