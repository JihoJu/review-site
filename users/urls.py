from django.urls import path
from .views import LoginView, log_out, SignUpView, ProfileView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", log_out, name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
]
