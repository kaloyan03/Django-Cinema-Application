# Generated by Django 4.0.3 on 2022-04-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_cart', '0010_alter_cart_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_created',
        ),
    ]