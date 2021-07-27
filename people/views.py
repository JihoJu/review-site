from django.views.generic import ListView
from .models import Person


class HomePeopleView(ListView):

    """HomePeopleView Definition"""

    model = Person
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created"
    template_name = "people_list.html"
    context_object_name = "people"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All People"
        return context
