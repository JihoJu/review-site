from django import forms
from django.forms.widgets import EmailInput, PasswordInput
from .models import User


class LoginForm(forms.Form):

    """Login Form Definition"""

    email = forms.EmailField(widget=EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        )
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
