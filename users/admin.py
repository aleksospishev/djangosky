# Register your models here.
from django.contrib import admin

from .models import User


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ("email", "username", "avatar", "country", "phone_number")
    list_filter = ("email", "country")
    search_fields = ("email", "phone_number")


# Register your models here.
