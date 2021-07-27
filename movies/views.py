from django.views.generic import ListView
from .models import Movie


class MovieHomeView(ListView):

    """MovieHomeView Definition"""

    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created"
    template_name = "movie_list.html"
    context_object_name = "movies"
