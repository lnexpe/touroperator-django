from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='Country is ....')
    image = models.ImageField(blank=True, null=True, upload_to='country_images')
    icon = models.ImageField(blank=True, null=True, upload_to='country_icon')
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='city_images')
    icon = models.ImageField(blank=True, null=True, upload_to='city_icon')
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='hotel_images')
    icon = models.ImageField(blank=True, null=True, upload_to='hotel_icon')
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.name


class Place(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='places_images')
    icon = models.ImageField(blank=True, null=True, upload_to='places_icon')

    def __str__(self):
        return self.name


class Trip(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    people = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_city = models.CharField(max_length=215)

    def route_set_sorted(self):
        return self.route_set.all().order_by('step')

    def __str__(self):
        return str(self.author.username) + "' trip " + str(self.created_at)


class Route(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    step = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class TripPlaces(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
