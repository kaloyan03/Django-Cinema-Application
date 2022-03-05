from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.


class Movie(models.Model):
    NAME_MAX_LENGTH = 40
    NAME_MIN_LENGTH = 2
    GENRE_ACTION = 'Action'
    GENRE_COMEDY = 'Comedy'
    GENRE_CRIMINAL = 'Criminal'
    GENRE_THRILLER = 'Thriller'
    GENRE_HORROR = 'Action'
    GENRE_FANTASY = 'Fantasy'
    GENRE_DRAMA = 'Drama'
    GENRE_ADVENTURE = 'Adventure'
    GENRE_HISTORICAL = 'Historical'
    GENRE_DOCUMENTARY = 'Documentary'
    GENRE_CHOICES = [(x, x) for x in (GENRE_ACTION, GENRE_COMEDY, GENRE_CRIMINAL, GENRE_THRILLER, GENRE_HORROR, GENRE_FANTASY, GENRE_DRAMA, GENRE_ADVENTURE, GENRE_HISTORICAL, GENRE_DOCUMENTARY)]
    GENRE_MAX_LENGTH = max(len(x) for x, _ in GENRE_CHOICES)
    GENRE_MIN_LENGTH = min(len(x) for x, _ in GENRE_CHOICES)
    YEAR_MIN_VALUE = 0
    DURATION_MIN_VALUE = 0
    CATEGORY_B = 'B'
    CATEGORY_C = 'C'
    CATEGORY_D = 'D'
    CATEGORY_CHOICES = [(x, x) for x in (CATEGORY_B, CATEGORY_C, CATEGORY_D)]
    CATEGORY_MAX_LENGTH = max(len(x) for x, _ in CATEGORY_CHOICES)
    CATEGORY_MIN_LENGTH = min(len(x) for x, _ in CATEGORY_CHOICES)

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        )
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRE_CHOICES,
        validators=(
            MinLengthValidator(GENRE_MIN_LENGTH),
        )
    )

    year = models.IntegerField(
        validators=(
            MinValueValidator(YEAR_MIN_VALUE),
        )
    )

    description = models.TextField(

    )

    duration = models.FloatField(
        validators=(
            MinValueValidator(DURATION_MIN_VALUE),
        )
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        choices=CATEGORY_CHOICES,
        validators=(
            MinValueValidator(CATEGORY_MIN_LENGTH),
        )
    )

