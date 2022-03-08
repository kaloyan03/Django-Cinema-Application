from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
from cinema_app.movies.models import Movie


class Actor(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 0
    AGE_MAX_VALUE = 100
    COUNTRY_MAX_LENGTH = 20
    COUNTRY_MIN_LENGTH = 2


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        )
    )

    image = models.ImageField(
        upload_to='actor_images/',
        default='unknown.jpg',
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )

    country = models.CharField(
        max_length=COUNTRY_MAX_LENGTH,
        validators=(
            MinLengthValidator(COUNTRY_MIN_LENGTH),
        )
    )

    movies = models.ManyToManyField(
        Movie,
    )

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
