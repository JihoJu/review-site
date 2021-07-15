from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdminModel(admin.ModelAdmin):

    """Person Admin Definition"""

    fieldsets = (
        (
            "Person Info",
            {
                "fields": (
                    "name",
                    "kind",
                    "photo",
                )
            },
        ),
    )

    list_filter = (
        "name",
        "kind",
        "photo",
    )

    list_display = (
        "name",
        "kind",
        "photo",
    )
