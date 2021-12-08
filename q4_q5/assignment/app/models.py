from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=12)
    # default password field used

    objects = UserManager()
