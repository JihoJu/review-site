from django.core.paginator import Paginator
from django.shortcuts import render
from movies.models import Movie
from books.models import Book
from people.models import Person


def resolve_home(request):
    movies_page = request.GET.get("movies_page")
    books_page = request.GET.get("books_page")
    people_page = request.GET.get("people_page")

    latest_movies_list = Movie.objects.all().order_by("-created")
    latest_books_list = Book.objects.all().order_by("-created")
    latest_people_list = Person.objects.all().order_by("-created")

    paginator_movies = Paginator(latest_movies_list, 5, orphans=3)
    paginator_books = Paginator(latest_books_list, 5, orphans=3)
    paginator_people = Paginator(latest_people_list, 5, orphans=3)

    latest_movies = paginator_movies.get_page(movies_page)
    latest_books = paginator_books.get_page(books_page)
    latest_people = paginator_people.get_page(people_page)

    return render(
        request,
        "home.html",
        context={
            "latest_movies": latest_movies,
            "latest_books": latest_books,
            "latest_people": latest_people,
        },
    )


def resolve_search(request):
    return render(request, "search.html")
