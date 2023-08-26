import random
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse
import config.settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.services import sendmail
from django.shortcuts import redirect
from django.contrib.auth import login
from decouple import config


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
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = config.settings.SITE_NAME
        sendmail(
            user.email,
            "Регистрация на сайте!",
            f"Подтвердите свой адрес электронной почты. Перейдите по ссылке: http://{current_site}{activation_url}"
        )
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
    """Сгенерировать новый пароль для пользователя"""
    new_password = "".join([str(random.randint(0, 9)) for _ in range(12)])
    sendmail(request.user.email, "Changed password on site", new_password)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse("catalog:index_page"))


class UserResetView(PasswordResetView):
    """Первый шаг сброса пароля пользователя"""
    template_name = "users/registration/password_reset_form.html"
    email_template_name = "users/registration/password_reset_email.html"
    success_url = reverse_lazy('users:password_reset_done')


class UserResetDoneView(PasswordResetDoneView):
    """Второй шаг сброса пароля пользователя"""
    template_name = "users/registration/password_reset_done.html"


class UserResetConfirmView(PasswordResetConfirmView):
    """Подтверждение пользователя о сбросе и изменении пароля"""
    template_name = "users/registration/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class UserResetCompleteView(PasswordResetCompleteView):
    """Информация о завершении сброса пароля"""
    template_name = "users/registration/password_reset_complete.html"