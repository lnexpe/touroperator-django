# Generated by Django 3.0.4 on 2020-05-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_route', '0005_remove_route_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
