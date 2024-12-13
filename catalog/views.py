from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    """ Список всех продуктов.  """
    model = Product


class ProductCreateView(CreateView):
    """ Создание нового продукта. """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    """ Редактирование продукта. """
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        """ Перенаправляет на страницу просмотра продукта после редактирования."""
        return reverse_lazy("catalog:product_detail", args=[self.object.id])


class ProductDeleteView(DeleteView):
    """ Удаление продукта.  """
    model = Product
    success_url = reverse_lazy("catalog:home")


class ProductDetailView(DetailView):
    """ Детальный просмотр продукта.  """
    model = Product
    form_class = ProductForm


class ContactView(TemplateView):
    """ Страница контактов.  """
    template_name = "catalog/contact.html"
    extra_context = {"title": "Контакты"}

    def get_context_data(self, **kwargs):
        """ Добавляет контекст с данными для отображения в шаблоне.  """
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        """ Отправляет сообщение сб обратной связи.  """
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"You have new message from {name}({email}): {message}")
        return super().get(request, *args, **kwargs)
