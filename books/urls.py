from django.urls import path
from .views import BookHomeView

app_name = "books"

urlpatterns = [
    path("", BookHomeView.as_view(), name="books"),
]
