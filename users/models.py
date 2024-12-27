from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """Переопределение модели User."""

    username = None
    country = models.CharField(
        max_length=20, verbose_name="Страна", blank=True, null=True, help_text="Укажите вашу страну"
    )
    phone_number = models.CharField(
        max_length=20, verbose_name="Номер телефона", blank=True, null=True, help_text="Укажите ваш номер телефона"
    )
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True, verbose_name="Аватар")
    email = models.EmailField(verbose_name="Электронная почта", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
