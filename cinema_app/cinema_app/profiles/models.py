from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from cloudinary import models as cloudinary_models

# Create your models here.
from cinema_app.cinema_auth.models import CinemaUser
from cinema_app.validators import validate_start_with_capital_letter


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 0
    AGE_MAX_VALUE = 100

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_start_with_capital_letter,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_start_with_capital_letter,
        )
    )

    profile_picture = cloudinary_models.CloudinaryField('image')

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
            MaxValueValidator(AGE_MAX_VALUE),
        )
    )

    user = models.OneToOneField(
        CinemaUser,
        on_delete=models.CASCADE,
    )