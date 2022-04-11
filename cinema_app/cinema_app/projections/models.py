from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from cinema_app.movies.models import Movie, Ticket


class Projection(models.Model):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    DAY_OF_THE_WEEK_CHOICES = [(x, x) for x in (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)]
    DAY_OF_THE_WEEK_MIN_LENGTH = min(len(x) for x, _ in DAY_OF_THE_WEEK_CHOICES)
    DAY_OF_THE_WEEK_MAX_LENGTH = max(len(x) for x, _ in DAY_OF_THE_WEEK_CHOICES)

    day_of_the_week = models.CharField(
        choices=DAY_OF_THE_WEEK_CHOICES,
        default=MONDAY,
        max_length=DAY_OF_THE_WEEK_MAX_LENGTH,
        validators=(
            MinLengthValidator(DAY_OF_THE_WEEK_MIN_LENGTH),
        )
    )

    time = models.TimeField(

    )

    ticket = models.ManyToManyField(
        Ticket,
    )

    def __str__(self):
        return f'{self.day_of_the_week} at {self.time}'

    class Meta:
        verbose_name = 'Projection'
        verbose_name_plural = 'Projections'