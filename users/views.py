from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from .forms import LoginForm


class LoginView(View):

    """Login View Definition"""

    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(self.request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):

    """Logout Func Definition"""

    logout(request)
    return redirect("core:home")
