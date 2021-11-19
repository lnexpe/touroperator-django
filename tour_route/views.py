from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, DeleteView
from .models import *
from .forms import HotelListForm, CountryListForm, RouteDateForm, AdditionalInfoForm
import csv
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


def export_hotels_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hotels.csv"'
    writer = csv.writer(response)
    writer.writerow(['Hotel name', 'Price'])
    hotels = Hotel.objects.all().values_list('name', 'price')
    for hotel in hotels:
        writer.writerow(hotel)
    return response


def index(request):
    return render(request, 'tour_route/index.html')


class HotelView(DetailView):
    model = Hotel
    template_name = 'tour_route/hotel.html'
    context_object_name = 'hotel'


class HotelList(ListView):
    model = Hotel
    template_name = 'tour_route/hotels.html'
    context_object_name = 'hotels'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        self.form = HotelListForm(request.GET)
        self.form.is_valid()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = Hotel.objects.all()
        if self.form.cleaned_data.get('city_field'):
            qs = qs.filter(city=self.form.cleaned_data.get('city_field'))
        if self.form.cleaned_data.get('search'):
            qs = qs.filter(name__icontains=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            qs = qs.order_by(self.form.cleaned_data['sort_field'])
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        return context


class CityView(DetailView):
    model = City
    template_name = 'tour_route/city.html'
    context_object_name = 'city'

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['hotels'] = self.object.hotel_set.all()[:3]
        context['places'] = self.object.place_set.all()[:3]
        return context


class PlaceView(DetailView):
    model = Place
    template_name = 'tour_route/place.html'
    context_object_name = 'place'


class CountryView(DetailView):
    model = Country
    template_name = 'tour_route/country.html'
    context_object_name = 'country'


class CountryList(ListView):
    model = Country
    template_name = 'tour_route/countries.html'
    context_object_name = 'countries'

    def dispatch(self, request, *args, **kwargs):
        self.form = CountryListForm(request.GET)
        self.form.is_valid()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = Country.objects.all()
        if self.form.cleaned_data.get('search'):
            qs = qs.filter(name__icontains=self.form.cleaned_data['search'])
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        return context


@login_required
def add_city(request, step):
    cities = City.objects.all()
    return render(request, 'tour_route/add_city.html', context={'cities': cities, 'step': step})


@login_required
def add_hotel(request, step, city):
    hotels = Hotel.objects.filter(city=city)
    return render(request, 'tour_route/add_hotel.html', context={'hotels': hotels, 'step': step})


@login_required
def add_places(request, step, city, hotel):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        hotel = Hotel.objects.get(pk=hotel)
        dates = RouteDateForm(request.POST)
        if dates.is_valid():
            if step == 1:
                info = AdditionalInfoForm(request.POST)
                if info.is_valid():
                    people = info.cleaned_data.get('people')
                    name = info.cleaned_data.get('name')
                    start_city = info.cleaned_data.get('start_city')
                    description = info.cleaned_data.get('description')
                    last_trip = Trip.objects.last()
                    if not last_trip:
                        last_id = 1
                        trip = Trip(id=last_id, author=user, people=people,
                                    name=name, description=description, start_city=start_city)
                        trip.save()
                    else:
                        last_id = last_trip.id + 1
                        trip = Trip(id=last_id, author=user, people=people,
                                    name=name, description=description, start_city=start_city)
                        trip.save()
            else:
                trip = Trip.objects.filter(author=user).last()

            route = Route(trip=trip, step=step, hotel=hotel, start_date=dates.cleaned_data.get('start'),
                          end_date=dates.cleaned_data.get('end'))
            route.save()
            for place in request.POST.getlist('chosen'):
                chosen_place = Place.objects.get(pk=place)
                place_qs = TripPlaces(route=route, place=chosen_place)
                place_qs.save()
            step += 1
            return render(request, 'tour_route/route_continue.html', context={'step': step})

    form_dates = RouteDateForm()
    form_info = AdditionalInfoForm()
    places = Place.objects.filter(city=city)
    return render(request, 'tour_route/add_places.html', context={'places': places, 'step': step,
                                                                  'form_dates': form_dates,
                                                                  'form_info': form_info})


@method_decorator(login_required, name='dispatch')
class TripList(ListView):
    model = Trip
    template_name = 'tour_route/trips.html'
    context_object_name = 'trips'

    def get_queryset(self):
        qs = Trip.objects.filter(author=self.request.user)
        return qs


@method_decorator(login_required, name='dispatch')
class TripView(DetailView):
    model = Trip
    template_name = 'tour_route/trip.html'
    context_object_name = 'trip'


@method_decorator(login_required, name='dispatch')
class TripDelete(DeleteView):
    model = Trip

    def get_success_url(self):
        return reverse('trips')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminTripList(ListView):
    model = Trip
    template_name = 'tour_route/admin_trips.html'
    context_object_name = 'trips'


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminTripDelete(DeleteView):
    model = Trip

    def get_success_url(self):
        return reverse('admin_trips')
