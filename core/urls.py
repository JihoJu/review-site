from django.urls import path
from .views import resolve_home, SearchView

app_name = "core"

urlpatterns = [
    path("", resolve_home, name="home"),
    path("search/", SearchView.as_view(), name="search"),
]
