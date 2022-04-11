# Generated by Django 4.0.3 on 2022-04-11 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0026_remove_projection_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_the_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=9, validators=[django.core.validators.MinLengthValidator(6)])),
                ('time', models.TimeField()),
                ('movie', models.ManyToManyField(to='movies.movie')),
            ],
            options={
                'verbose_name': 'Projection',
                'verbose_name_plural': 'Projections',
            },
        ),
    ]
