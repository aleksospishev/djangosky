from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView

from .models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'
    extra_context = {
        'title': 'Контакты'
    }

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
        return super().get(request, *args, **kwargs)