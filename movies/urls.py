from django.urls import path
from .views import MovieHomeView

app_name = "movies"

urlpatterns = [
    path("", MovieHomeView.as_view(), name="movies"),
]
