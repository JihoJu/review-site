from django.urls import path
from .views import resolve_people

app_name = "people"

urlpatterns = [
    path("", resolve_people, name="people"),
]
