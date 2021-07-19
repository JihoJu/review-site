import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from movies.models import Movie
from books.models import Book
from reviews.models import Review

NAME = "reviews"

help = f"This command creates {NAME}"


class Command(BaseCommand):

    """Reviews Command Definition"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        total = options["total"]

        # User objects
        all_users = User.objects.all()
        # Movie objects
        all_movies = Movie.objects.all()
        # Book objects
        all_books = Book.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            total,
            {
                "rating": lambda x: random.randint(0, 5),
                "created_by": lambda x: random.choice(all_users),
                "book": lambda x: random.choice(all_books),
                "movie": lambda x: random.choice(all_movies),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!!"))
