# Generated by Django 4.0.3 on 2022-04-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_remove_projections_day_of_the_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Projection',
                'verbose_name_plural': 'Projections',
            },
        ),
        migrations.RemoveField(
            model_name='projections',
            name='movie',
        ),
    ]