# Generated by Django 4.0.3 on 2022-04-09 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_movietime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_the_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9, validators=[django.core.validators.MinLengthValidator(6)])),
                ('time', models.TimeField()),
                ('movie', models.ManyToManyField(to='movies.movie')),
            ],
        ),
        migrations.DeleteModel(
            name='MovieTime',
        ),
    ]
