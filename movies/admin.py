from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdminModel(admin.ModelAdmin):

    """Movie Admin Definition"""

    fieldsets = (
        (
            "Movie Info",
            {
                "fields": (
                    "title",
                    "year",
                    "cover_image",
                    "rating",
                    "category",
                    "director",
                    "cast",
                )
            },
        ),
    )

    list_filter = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )

    list_display = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )
