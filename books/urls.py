from django.urls import path
from .views import BookHomeView, BookDetailView, BookCreateView

app_name = "books"

urlpatterns = [
    path("", BookHomeView.as_view(), name="books"),
    path("<int:pk>/", BookDetailView.as_view(), name="detail"),
    path("create/", BookCreateView.as_view(), name="create"),
]
