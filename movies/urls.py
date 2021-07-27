from django.urls import path
from .views import MovieHomeView, MovieDetailView, MovieCreateView

app_name = "movies"

urlpatterns = [
    path("", MovieHomeView.as_view(), name="movies"),
    path("<int:pk>/", MovieDetailView.as_view(), name="detail"),
    path("create/", MovieCreateView.as_view(), name="create"),
]
