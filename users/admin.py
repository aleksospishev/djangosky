# Register your models here.
from django.contrib import admin

from .models import User


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    """Модель администрирования пользователей."""
    list_display = ("email", "avatar", "country", "phone_number")
    list_filter = ("email", "country")
    search_fields = ("email", "phone_number")

