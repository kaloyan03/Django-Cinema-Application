from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


# Create your models here.


class CinemaUserManager(BaseUserManager):
    """
    Manager for the CinemaUser.
    """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CinemaUser(AbstractBaseUser, PermissionsMixin):
    """
    Extended User model with email than username.
    """
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    # solution for the reset password functionality
    is_active = models.BooleanField(
        default=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    has_completed_profile = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = CinemaUserManager()
