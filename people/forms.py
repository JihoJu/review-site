from django import forms
from .models import Person


class CreatePeopleForm(forms.ModelForm):

    """Create PeopleForm Definition"""

    class Meta:
        model = Person
        fields = (
            "name",
            "kind",
            "photo",
        )
