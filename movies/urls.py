from django.urls import path
from .views import MovieHomeView, MovieDetailView, MovieCreateView, MovieUpdateView

app_name = "movies"

urlpatterns = [
    path("", MovieHomeView.as_view(), name="movies"),
    path("<int:pk>/", MovieDetailView.as_view(), name="detail"),
    path("create/", MovieCreateView.as_view(), name="create"),
    path("<int:pk>/update/", MovieUpdateView.as_view(), name="update"),
]
