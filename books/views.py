from django.views.generic import ListView, DetailView, CreateView
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


class BookCreateView(CreateView):

    """Book CreateView Definition"""

    form_class = CreateBookForm
    template_name = "books/book_create.html"
