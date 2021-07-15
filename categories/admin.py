from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):

    """Category Admin Definition"""

    fieldsets = (
        (
            "Category Info",
            {
                "fields": (
                    "name",
                    "kind",
                )
            },
        ),
    )

    list_filter = (
        "name",
        "kind",
    )

    list_display = (
        "name",
        "kind",
    )
