from django.contrib import admin
from .models import FavList


@admin.register(FavList)
class FavListAdminModel(admin.ModelAdmin):

    """FavList Admin Definition"""

    fieldsets = (
        (
            "FavList Info",
            {
                "fields": (
                    "created_by",
                    "books",
                    "movies",
                )
            },
        ),
    )

    list_filter = (
        "created_by",
        "books",
        "movies",
    )

    list_display = (
        "created_by",
        "books_count",
        "movies_count",
    )
