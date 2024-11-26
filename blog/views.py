from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Create your views here.
from .models import Post


class PostListView(ListView):
    """Список публичных постов."""
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    """Детальный просмотр поста."""
    model = Post

    def get_object(self):
        """Увеличивает счетчик просмотров поста."""
        obj = super().get_object()
        obj.count_views += 1
        obj.save()
        return obj


class PostCreateView(CreateView):
    """Создание нового поста."""
    model = Post
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:blog")


class PostUpdateView(UpdateView):
    """Редактирование поста."""
    model = Post
    fields = ("title", "content", "preview")

    def get_success_url(self):
        """Перенаправляет на страницу просмотра поста после редактирования."""
        return reverse_lazy("blog:post_detail", args=[self.object.id])


class PostDeleteView(DeleteView):
    """Удаление поста."""
    model = Post
    success_url = reverse_lazy("blog:blog")
