from django.db import models
from core.models import TimeStampedModel


class Person(TimeStampedModel):

    """Person Model Definition"""

    # kind choices

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"
    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=10, blank=True)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, blank=True)
    photo = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = "people"

    def __str__(self):
        return self.name
