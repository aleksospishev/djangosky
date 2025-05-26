from django.db import models

from users.models import User


class Category(models.Model):
    """Класс для категорий товаров."""

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """Возвращает имя категории."""
        return self.name

    class Meta:
        """Определение настроек модели категории."""

        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """Класс для товаров с указанием категории и цены."""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="products/image", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(
        verbose_name="Категория", to=Category, on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Дата изменения")
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(User, verbose_name="владелец", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """Возвращает имя товара, категорию и цену."""
        return f"{self.name} {self.category} {self.price}.руб."

    class Meta:
        """Определение настроек модели продукта."""

        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at", "name", "category", "price"]
        permissions = (("can_unpublish_product", "Can unpublish product"),)
