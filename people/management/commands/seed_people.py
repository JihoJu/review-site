from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person

NAME = "people"

help = f"This command creates {NAME}"


class Command(BaseCommand):

    """People Command Definition"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        total = options["total"]
        seeder = Seed.seeder()
        seeder.add_entity(
            Person,
            total,
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!!"))
