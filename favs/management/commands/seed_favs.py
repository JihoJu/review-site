import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from movies.models import Movie
from books.models import Book
from favs.models import FavList

NAME = "FavLists"

help = f"This command creates {NAME}"


class Command(BaseCommand):

    """FavLists Command Definition"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        total = options["total"]
        random_number = random.randint(1, 50)
        # User objects
        all_users = User.objects.all()[random_number : random_number + total]
        all_users = list(all_users)
        # Movie objects
        all_movies = Movie.objects.all()[random_number : random_number + total]
        # Book objects
        all_books = Book.objects.all()[random_number : random_number + total]

        seeder = Seed.seeder()
        seeder.add_entity(
            FavList,
            total,
            {
                "created_by": lambda x: all_users.pop(0),
            },
        )
        inserted_pk = seeder.execute()
        inserted_pk = flatten(list(inserted_pk.values()))

        for pk in inserted_pk:
            fav = FavList.objects.get(pk=pk)
            for i in range(random.randint(1, 5)):
                if all_books[i] is not None:
                    fav.books.add(all_books[i])
                if all_movies[i] is not None:
                    fav.movies.add(all_movies[i])
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!!"))
