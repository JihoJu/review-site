from django.urls import path
from .views import HomePeopleView

app_name = "people"

urlpatterns = [
    path("", HomePeopleView.as_view(), name="people"),
]
