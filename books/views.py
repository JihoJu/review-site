from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book
from .forms import CreateBookForm


class BookHomeView(ListView):

    """BookHomeView Definition"""

    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created"
    template_name = "books/book_list.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Books"
        return context


class BookDetailView(DetailView):

    """Book DetailView Definition"""

    model = Book
    template_name = "books/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"[Book] {context['object']}"
        return context


class BookCreateView(CreateView):

    """Book CreateView Definition"""

    form_class = CreateBookForm
    template_name = "books/book_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Book"
        return context


class BookUpdateView(UpdateView):

    """Book UpdateView Definition"""

    model = Book
    template_name = "books/book_update.html"
    fields = (
        "title",
        "year",
        "category",
        "cover_image",
        "writer",
    )
