from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/<int:pk>/', views.HotelView.as_view(), name='hotel_description'),
    path('city/<int:pk>/', views.CityView.as_view(), name='city_description'),
    path('place/<int:pk>/', views.PlaceView.as_view(), name='place_description'),
    path('country/<int:pk>/', views.CountryView.as_view(), name='country_description'),
    path('hotels/', views.HotelList.as_view(), name='all_hotels'),
    path('countries/', views.CountryList.as_view(), name='all_countries'),
    path('route/<int:step>/', views.add_city, name='add_city'),
    path('route/<int:step>/<int:city>/', views.add_hotel, name='add_hotel'),
    path('route/<int:step>/<int:city>/<int:hotel>/', views.add_places, name='add_places'),
    path('trips/', views.TripList.as_view(), name='trips'),
    path('admin_trips/', views.AdminTripList.as_view(), name='admin_trips'),
    path('trip/<int:pk>/', views.TripView.as_view(), name='trip_description'),
    path('trips/delete/<int:pk>', views.TripDelete.as_view(), name='delete_trip'),
    path('trips/admin_delete/<int:pk>', views.AdminTripDelete.as_view(), name='admin_delete_trip'),
    path('export_hotel/', views.export_hotels_csv, name='hotel_export'),
]
