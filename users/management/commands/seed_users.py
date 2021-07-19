import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from categories.models import Category

NAME = "users"

help = f"This command creates {NAME}"


class Command(BaseCommand):

    """Users Command Definition"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        total = options["total"]
        all_categories_books = Category.objects.exclude(kind="movie")
        all_categories_movies = Category.objects.exclude(kind="book")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            total,
            {
                "favorite_book_genre": lambda x: random.choice(all_categories_books),
                "favorite_movie_genre": lambda x: random.choice(all_categories_movies),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!!"))
