from django.core.management.base import BaseCommand
from django_seed import Seed
from categories.models import Category

NAME = "categories"


class Command(BaseCommand):

    """Categories Command Definition"""

    help = f"This is command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        # total = options.get("total")
        number = options["number"]
        seeder = Seed.seeder()
        seeder.add_entity(Category, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!!!"))
