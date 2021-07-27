from django.urls import path
from .views import BookHomeView, BookDetailView

app_name = "books"

urlpatterns = [
    path("", BookHomeView.as_view(), name="books"),
    path("<int:pk>/", BookDetailView.as_view(), name="detail"),
]
