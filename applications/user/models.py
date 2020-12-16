from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    full_name = models.CharField("Nombre Completo", max_length=50)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return str(self.id) + '-' + self.full_name