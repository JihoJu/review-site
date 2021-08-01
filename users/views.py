from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, DetailView, UpdateView
from django.views.generic.base import View
from .forms import LoginForm, SignUpForm
from .models import User


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


class SignUpView(FormView):

    """SignUp View Definition"""

    template_name = "users/signup.html"
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:home")


class ProfileView(DetailView):

    """Profile View Definition"""

    model = User
    fields = (
        "first_name",
        "last_name",
        "bio",
        "preference",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
    )
    template_name = "users/profile.html"
    context_object_name = "user"


class ProfileUpdateView(UpdateView):

    """Profile UpdateView Definition"""

    model = User
    fields = (
        "first_name",
        "last_name",
        "preference",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
        "bio",
    )
    template_name = "users/profile_update.html"

    def get_success_url(self):
        return reverse("users:profile", kwargs={"pk": self.request.user.pk})
