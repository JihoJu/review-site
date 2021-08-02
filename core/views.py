from django.core.paginator import EmptyPage, Paginator
from django.views.generic import View
from django.shortcuts import render
from movies.models import Movie
from books.models import Book
from people.models import Person
from .forms import SearchForm


def resolve_home(request):
    movies_page = request.GET.get("movies_page", 1)
    books_page = request.GET.get("books_page", 1)
    people_page = request.GET.get("people_page", 1)

    latest_movies_list = Movie.objects.all().order_by("-created")
    latest_books_list = Book.objects.all().order_by("-created")
    latest_people_list = Person.objects.all().order_by("-created")

    try:
        paginator_movies = Paginator(latest_movies_list, 10, orphans=5)
        latest_movies = paginator_movies.page(int(movies_page))
    except EmptyPage:
        latest_movies = None

    try:
        paginator_books = Paginator(latest_books_list, 10, orphans=5)
        latest_books = paginator_books.page(int(books_page))
    except EmptyPage:
        latest_books = None

    try:
        paginator_people = Paginator(latest_people_list, 10, orphans=5)
        latest_people = paginator_people.page(int(people_page))
    except EmptyPage:
        latest_people = None

    return render(
        request,
        "home.html",
        context={
            "latest_movies": latest_movies,
            "latest_books": latest_books,
            "latest_people": latest_people,
        },
    )


class SearchView(View):

    """Search View Definition"""

    def get(self, request):
        keyword = request.GET.get("key_word")

        if keyword is not None:
            # request.GET => 어떤 걸 검색했고 선택했는 지 기억한다.
            form = SearchForm(request.GET)

            # db에서 불러올 명령어
            filter_tag = dict()

            if form.is_valid():
                keyword = form.cleaned_data.get("key_word")

                if keyword:
                    filter_tag["title__contains"] = str(keyword)

                books = Book.objects.filter(**filter_tag)
                movies = Movie.objects.filter(**filter_tag)

                return render(
                    request,
                    "search.html",
                    {
                        "form": form,
                        "books": books,
                        "movies": movies,
                    },
                )

        else:
            form = SearchForm()

        return render(request, "search.html", {"form": form})
