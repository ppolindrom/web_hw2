import random
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetDoneView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import login
from users.test import send_mail

class LoginView(BaseLoginView):
    """ Вход на сайт """
    template_name = "users/login.html"
    title = "Login"


class LogoutView(BaseLogoutView):
    """ Выход с сайта """
    template_name = "users/login.html"


class RegisterView(CreateView):
    """ Регистрация нового пользователя и отправка подтверждения на email пользователя """
    form_class = UserRegisterForm
    template_name = "users/registration/registration_form.html"
    success_url = reverse_lazy('users:registration_reset')
    title = "Регистрация нового пользователя"

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        token = default_token_generator.make_token(user)
        print('создал токен')
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print('скоро создам активейд урл')
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        print('скоро создам кьюрент файл')
        current_site = '127.0.0.1:8000'
        print(user.email)
        send_mail(
            to= user.email,
            theme="Регистрация на сайте!",
            message = f"Подтвердите свой адрес электронной почты. Перейдите по ссылке: http://{current_site}{activation_url}"
        )
        print('письмо отправлено')
        return redirect('users:email_confirmation_sent')


class UserConfirmationSentView(PasswordResetDoneView):
    """Успешный первый этап регистрации"""
    template_name = "users/registration/registration_sent_done.html"


class UserConfirmEmailView(View):
    """Пользователь подтверждает свою регистрацию"""
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')


class UserConfirmedView(TemplateView):
    """Регистрация пользователя завершена, вывод информации об этом"""
    template_name = 'users/registration/registration_confirmed.html'
    title = "Your email is activated."


class UserUpdateView(UpdateView):
    """Профиль пользователя """
    model = User
    success_url = reverse_lazy("users:profile")
    form_class = UserProfileForm
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    """Сгенерировать новый пароль для пользователя по желанию"""
    print('я запустилась')
    new_password = "".join([str(random.randint(0, 9)) for _ in range(12)])
    print('я сгенирировала пароль')
    send_mail(request.user.email, "Changed password on site", new_password)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse("index"))

def password_reset(request):
    """Сгенерировать новый пароль для пользователя если пароль забыли"""
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = "".join([str(random.randint(0, 9)) for _ in range(12)])
            user.set_password(new_password)
            user.save()

            subject = "Changed password on site"
            message = f"Your new password: {new_password}"
            send_mail(user.email, subject, message)

            return redirect(reverse("users:login"))  # Перенаправление на страницу входа
        except User.DoesNotExist:
            return render(request, 'users/registration/password_reset_form.html', {'error_message': 'User not found'})  # Отображение формы с сообщением об ошибке
    return render(request, 'users/registration/password_reset_form.html')  # Вывод формы для ввода email
