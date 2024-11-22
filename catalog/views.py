from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product


def home(request):
    """Контроллер домашней страницы."""
    context = {"products": Product.objects.all()}
    return render(request, "home.html", context)


def contacts(request):
    """Контроллер страницы контакты, с формой обратной связи."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} c номером телефона {phone}, отправил сообщение {message}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contact.html")


def product_detail(request, product_id):
    """Контроллер страницы детального продукта."""
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product}
    return render(request, "product.html", context)
