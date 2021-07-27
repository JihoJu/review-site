from django import forms
from .models import Movie


class CreateMovieForm(forms.ModelForm):

    """Create MovieForm Definition"""

    class Meta:
        model = Movie
        fields = (
            "title",
            "year",
            "category",
            "cover_image",
            "director",
            "cast",
        )
