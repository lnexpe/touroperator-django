# Generated by Django 3.0.4 on 2020-05-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_route', '0007_remove_tripplaces_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='people',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
