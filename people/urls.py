from django.urls import path
from .views import HomePeopleView, PeopleDetailView

app_name = "people"

urlpatterns = [
    path("", HomePeopleView.as_view(), name="people"),
    path("<int:pk>/", PeopleDetailView.as_view(), name="detail"),
]
