from django.db import models


class Category(models.Model):
    """Класс для категорий товаров."""

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """Класс для товаров с указанием категории и цены"""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(
        verbose_name="Категория", to=Category, on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.name} {self.category} {self.price}.руб."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at", "name", "category", "price"]
