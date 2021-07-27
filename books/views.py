from django.views.generic import ListView
from .models import Book


class BookHomeView(ListView):

    """BookHomeView Definition"""

    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created"
    template_name = "book_list.html"
    context_object_name = "books"
