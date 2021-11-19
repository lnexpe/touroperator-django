# Generated by Django 3.0.4 on 2020-05-09 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour_route', '0003_auto_20200510_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='places',
        ),
        migrations.RemoveField(
            model_name='tripplaces',
            name='trip',
        ),
        migrations.AddField(
            model_name='tripplaces',
            name='route',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tour_route.Route'),
            preserve_default=False,
        ),
    ]