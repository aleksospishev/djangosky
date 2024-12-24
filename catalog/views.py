from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import ProductForm, ProductModeratorForm
from .models import Product


class ProductListView(ListView):
    """Список всех продуктов."""

    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание нового продукта."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование продукта."""

    model = Product
    form_class = ProductForm

    def get_success_url(self):
        """Перенаправляет на страницу просмотра продукта после редактирования."""
        return reverse_lazy("catalog:product_detail", args=[self.object.id])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        else:
            raise PermissionDenied("You don't have permission to edit this product.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта."""

    model = Product
    success_url = reverse_lazy("catalog:home")

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        user = self.request.user
        if user == self.product.owner or user.has_perm("catalog.can_delete_product"):
            product.delete()
            return redirect("catalog:home")
        else:
            return HttpResponseForbidden("У вас нет прав для исключения студента.")

    #
    # def get_object(self, queryset = None):
    #     user = self.request.user
    #     if user == self.object.owner or user.has_perm("catalog.can_delete_product"):
    #         object.delete()
    #     else:
    #         raise HttpResponseForbidden
    #
    #


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Детальный просмотр продукта."""

    model = Product
    form_class = ProductForm


class ContactView(TemplateView):
    """Страница контактов."""

    template_name = "catalog/contact.html"
    extra_context = {"title": "Контакты"}

    def get_context_data(self, **kwargs):
        """Добавляет контекст с данными для отображения в шаблоне."""
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        """Отправляет сообщение сб обратной связи."""
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"You have new message from {name}({email}): {message}")
        return super().get(request, *args, **kwargs)
