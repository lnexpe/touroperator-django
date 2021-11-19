from django import forms
from .models import City, Route


class HotelListForm(forms.Form):
    form_choices = (('name', 'Name'),
                    ('price', 'Price ASC'),
                    ('-price', 'Price DESC')
                    )
    search = forms.CharField(required=False, label='Search hotel by name')
    sort_field = forms.ChoiceField(choices=form_choices, required=False, label='Sort')
    city_field = forms.ModelChoiceField(queryset=City.objects.all(), required=False, label='City')


class CountryListForm(forms.Form):
    search = forms.CharField(required=False)


class RouteDateForm(forms.Form):
    start = forms.DateTimeField(required=True,
                                input_formats=['%d/%m/%Y'],
                                widget=forms.DateTimeInput(attrs={
                                    'class': 'form-control datetimepicker-input',
                                })
                                )
    end = forms.DateTimeField(required=True,
                              input_formats=['%d/%m/%Y'],
                              widget=forms.DateTimeInput(attrs={
                                  'class': 'form-control datetimepicker-input',
                              })
                              )


class AdditionalInfoForm(forms.Form):
    name = forms.CharField(max_length=255)
    people = forms.IntegerField(min_value=1, max_value=150)
    description = forms.CharField(widget=forms.Textarea)
    start_city = forms.CharField(max_length=100)
