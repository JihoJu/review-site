from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdminModel(admin.ModelAdmin):

    """Book Admin Definition"""

    fieldsets = (
        (
            "Book Info",
            {
                "fields": (
                    "title",
                    "year",
                    "category",
                    "cover_image",
                    "rating",
                    "writer",
                )
            },
        ),
    )

    list_filter = (
        "title",
        "year",
        "category",
        "cover_image",
        "rating",
        "writer",
    )

    list_display = (
        "title",
        "year",
        "category",
        "cover_image",
        "rating",
        "writer",
    )
