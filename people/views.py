from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Person
from .forms import CreatePeopleForm


class HomePeopleView(ListView):

    """HomePeopleView Definition"""

    model = Person
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created"
    template_name = "people/people_list.html"
    context_object_name = "people"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All People"
        return context


class PeopleDetailView(DetailView):

    """People DetailView Definition"""

    model = Person
    template_name = "people/people_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"[Person] {context['object']}"
        return context


class PeopleCreateView(CreateView):

    """People CreateView Definition"""

    form_class = CreatePeopleForm
    template_name = "people/people_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Person"
        return context


class PeopleUpdateView(UpdateView):

    """People UpdateView Definition"""

    model = Person
    template_name = "people/people_update.html"
    fields = (
        "name",
        "kind",
        "photo",
    )
