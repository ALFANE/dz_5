from django.core.management.base import BaseCommand
from faker import Faker

from home.models import Student

class Command(BaseCommand):

    help = 'Add new students to the system'

    def add_arguments(self, parser):

        parser.add_argument('-l', '--len', type = int, default =10 )

    def handle(self, *args, **options):

        faker = Faker()
        self.stdout.write('Start inserting Students')
        for _ in range(options['len']):
            self.stdout.write('Start inserting Student')
            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.pyint(min_value=0, max_value=70, step=1)
            student.sex = faker.simple_profile()['sex']
            student.address = faker.address()
            student.description = faker.text()
            student.birthday = faker.date_between(start_date='-50y', end_date='-18y')
            student.email = faker.email()
            student.save()
            self.stdout.write('Student inserted')
        self.stdout.write('End inserting Students')
