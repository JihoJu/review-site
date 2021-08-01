from django.urls import path
from .views import LoginView, log_out, SignUpView, ProfileView, ProfileUpdateView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", log_out, name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path(
        "profile/update/<int:pk>/", ProfileUpdateView.as_view(), name="profile-update"
    ),
]
