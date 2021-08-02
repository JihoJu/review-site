from django import forms


class SearchForm(forms.Form):

    """Search Form Definition"""

    key_word = forms.CharField(required=True)
