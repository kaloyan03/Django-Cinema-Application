# Generated by Django 4.0.3 on 2022-03-22 20:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0014_moviecomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieComment',
            new_name='Comment',
        ),
    ]
