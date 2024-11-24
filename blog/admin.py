from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at", "updated_at", "published", "count_views")
    list_filter = ("published", "title")
    search_fields = ("title", "content")


# Register your models here.
