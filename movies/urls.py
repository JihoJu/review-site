from django.urls import path
from .views import resolve_movies

app_name = "movies"

urlpatterns = [
    path("", resolve_movies, name="movies"),
]
