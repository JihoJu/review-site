import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person
from categories.models import Category
from movies.models import Movie

NAME = "movies"

help = f"This command creates {NAME}"


class Command(BaseCommand):

    """Movies Command Definition"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        total = options["total"]

        # category movie objects
        all_categories_movies = Category.objects.exclude(kind="book")
        # person writer objects
        all_director = Person.objects.filter(kind="director")
        all_actor = Person.objects.filter(kind="actor")
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie,
            total,
            {
                "year": lambda x: random.randint(1980, 2021),
                "category": lambda x: random.choice(all_categories_movies),
                "rating": lambda x: random.randint(0, 5),
                "director": lambda x: random.choice(all_director),
                "cast": lambda x: random.choice(all_actor),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!!"))
