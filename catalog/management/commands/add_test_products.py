from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Класс для добавления тестовых продуктов в базу данных в ручном режиме и из фикстур."""

    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name="Мясо")

        products = [
            {"name": "Свиная рулька", "description": "рулька свиная класса А", "category": category, "price": "150"},
            {"name": "Лопатка говяжья", "description": "Говяжья лопатка", "category": category, "price": "850"},
            {"name": "Шея свиная", "description": "Шея свиная класса А", "category": category, "price": "860"},
            {"name": "Тушка Утки", "description": "утка домашняя", "category": category, "price": "1500"},
            {"name": "куриная голень", "description": "Голень курицы домашней", "category": category, "price": "500"},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"product already exists: {product.name}"))

        call_command("loaddata", "category_fixture.json")
        call_command("loaddata", "product_fixture.json")
