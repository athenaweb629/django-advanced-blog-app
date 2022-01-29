from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class BlangoUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # Implementing Email Log in
    # Remove Username instances and replace with email
    username = None
    # Require unique email addresses
    email = models.EmailField(
        _("email address"), 
        unique=True,
    )
    # set to a new instance of the user manager
    objects = BlangoUserManager()
    # Since username is required, replace with email.
    USERNAME_FIELD = "email"
    # Remove Username instances and replace with email
    # Django will assume REQUIRED_FIELDS=username
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email