# Generated by Django 4.0.3 on 2022-04-10 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_remove_projections_day_of_the_week'),
        ('tickets_cart', '0011_remove_cart_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='projection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.projections'),
        ),
    ]
