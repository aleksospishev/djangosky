from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangosky.settings import EMAIL_HOST_USER

from .forms import UserRegisterForm
from .models import User


class UserRegisterView(CreateView):
    """Регистрация нового пользователя."""

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Сохраняет нового пользователя и отправляет письмо с информацией о регистрации."""
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """Отправляет письмо с приветствием и информацией о регистрации."""
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
