# Generated by Django 4.0.3 on 2022-04-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_auth', '0005_cinemauser_has_completed_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemauser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]