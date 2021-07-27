from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):

    """Create BookForm Definition"""

    class Meta:
        model = Book
        fields = (
            "title",
            "year",
            "category",
            "cover_image",
            "writer",
        )
