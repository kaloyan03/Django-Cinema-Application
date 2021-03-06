# Generated by Django 4.0.3 on 2022-03-06 21:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(0)]),
        ),
    ]
