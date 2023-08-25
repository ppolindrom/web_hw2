from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


class RegisterView(CreateView):
    """ Register new user and send verification mail on user email."""
    form_class = UserCreationForm
    template_name = "users/registration/registration_form.html"
    # success_url = reverse_lazy('users:registration_reset')
    # title = "Registration New User"
    #
    # def form_valid(self, form):
    #     user = form.save()
    #     user.is_active = False
    #     user.save()
    #     token = default_token_generator.make_token(user)
    #     uid = urlsafe_base64_encode(force_bytes(user.pk))
    #     activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
    #     current_site = config.settings.SITE_NAME
    #     sendmail(
    #         user.email,
    #         "Registration on Site!",
    #         f"Accept your email address. Go on: http://{current_site}{activation_url}"
    #     )
    #     return redirect('users:email_confirmation_sent')