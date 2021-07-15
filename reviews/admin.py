from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdminModel(admin.ModelAdmin):

    """Review Admin Model"""

    fieldsets = (
        (
            "Review Info",
            {
                "fields": (
                    "created_by",
                    "text",
                    "book",
                    "movie",
                    "rating",
                )
            },
        ),
    )

    list_filter = (
        "created_by",
        "text",
        "book",
        "movie",
        "rating",
    )

    list_display = (
        "created_by",
        "text",
        "book",
        "movie",
        "rating",
    )
