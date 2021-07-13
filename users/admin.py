from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """User Admin Definition"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "favorite_book_genre",
                    "favorite_movie_genre",
                )
            },
        ),
    )

    # Admin Field Filter

    list_filter = (
        "language",
        "preference",
        "favorite_book_genre",
        "favorite_movie_genre",
    )
