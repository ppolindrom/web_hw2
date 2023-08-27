from django.urls import path
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_password, \
    UserConfirmEmailView, \
    UserConfirmedView, password_reset, UserConfirmationSentView

app_name = "users"


urlpatterns = [

    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegisterView.as_view(), name="registration"),
    path('email_confirmation_sent/', UserConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email_confirmed/', UserConfirmedView.as_view(), name='email_confirmed'),
    path("profile/", UserUpdateView.as_view(), name="profile"),
    path("profile/generate_password", generate_password, name="generate_password"),
    path('password_reset/', password_reset, name='password_reset'),
]