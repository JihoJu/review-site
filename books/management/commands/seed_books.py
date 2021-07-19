import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person
from categories.models import Category
from books.models import Book

NAME = "books"

help = f"This command creates {NAME}"


class Command(BaseCommand):

    """Books Command Definition"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        total = options["total"]

        # category book objects
        all_categories_books = Category.objects.exclude(kind="movie")
        # person writer objects
        all_people = Person.objects.filter(kind="writer")
        seeder = Seed.seeder()
        seeder.add_entity(
            Book,
            total,
            {
                "year": lambda x: random.randint(1980, 2021),
                "category": lambda x: random.choice(all_categories_books),
                "rating": lambda x: random.randint(0, 5),
                "writer": lambda x: random.choice(all_people),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!!"))
