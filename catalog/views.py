from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Контроллер домашней страницы."""
    return render(request, "home.html")


def contacts(request):
    """Контроллер страницы контакты, с формой обратной связи."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'{name} c номером телефона {phone}, отправил сообщение {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contact.html")
