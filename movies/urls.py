from django.urls import path
from .views import MovieHomeView, MovieDetailView

app_name = "movies"

urlpatterns = [
    path("", MovieHomeView.as_view(), name="movies"),
    path("<int:pk>/", MovieDetailView.as_view(), name="detail"),
]
