from django.urls import path
from .views import HomePeopleView, PeopleDetailView, PeopleCreateView

app_name = "people"

urlpatterns = [
    path("", HomePeopleView.as_view(), name="people"),
    path("<int:pk>/", PeopleDetailView.as_view(), name="detail"),
    path("create/", PeopleCreateView.as_view(), name="create"),
]
