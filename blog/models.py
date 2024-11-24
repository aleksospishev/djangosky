from django.db import models


class Post(models.Model):
    """Класс для постов в блоге."""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to="posts/image", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    count_views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        """Возвращает заголовок поста."""
        return f"{self.title}."

    class Meta:
        """Определение настроек модели поста."""
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at", "title"]
