# Generated by Django 4.0.3 on 2022-03-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_auth', '0004_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemauser',
            name='has_completed_profile',
            field=models.BooleanField(default=False),
        ),
    ]
