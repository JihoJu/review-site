from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from movies.models import Movie
from books.models import Book
from people.models import Person


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
            "page_title": "Home",
            "latest_movies": latest_movies,
            "latest_books": latest_books,
            "latest_people": latest_people,
        },
    )


def resolve_search(request):
    return render(request, "search.html")
