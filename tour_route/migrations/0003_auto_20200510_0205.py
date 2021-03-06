# Generated by Django 3.0.4 on 2020-05-09 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour_route', '0002_auto_20200509_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='name',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='total',
        ),
        migrations.AddField(
            model_name='trip',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TripPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_route.City')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_route.Place')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_route.Trip')),
            ],
        ),
    ]
