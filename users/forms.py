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


class SignUpForm(forms.ModelForm):

    """SignUp Form Definition"""

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )

    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user = User.objects.get(email=email)
            self.add_error("email", forms.ValidationError("This Email is exist"))
        except User.DoesNotExist:
            return email

    def clean_password(self):
        pw = self.cleaned_data.get("password")
        confirm_pw = self.cleaned_data.get("confirm_password")

        if pw == confirm_pw:
            self.add_error(
                "password",
                forms.ValidationError("Password Confirmation does not match"),
            )
        else:
            return pw

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
