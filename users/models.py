from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=50, verbose_name="Номер телефона", null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name="Страна", null=True, blank=True)
    avatar = models.ImageField(upload_to="images", verbose_name="Аватар", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []