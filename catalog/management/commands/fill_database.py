from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Fill the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing old data...')
        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write('Creating categories...')
        Category.objects.create(title='Category 1', text='Description for Category 1')
        Category.objects.create(title='Category 2', text='Description for Category 2')

        self.stdout.write('Creating products...')
        category1 = Category.objects.get(title='Category 1')
        Product.objects.create(title='Product 1', text='Description for Product 1',
                               category=category1, price=100)

        category2 = Category.objects.get(title='Category 2')
        Product.objects.create(title='Product 2', text='Description for Product 2',
                               category=category2, price=150)

        self.stdout.write(self.style.SUCCESS('Database successfully filled!'))
