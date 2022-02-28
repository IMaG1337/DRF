from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    first_name = models.CharField(verbose_name="Имя", max_length=64)
    last_name = models.CharField(verbose_name="Фамилия", max_length=64)
    birthday_year = models.PositiveIntegerField(blank=True)
    email = models.EmailField(verbose_name="email", unique=True)
