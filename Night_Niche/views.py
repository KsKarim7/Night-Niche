from django.shortcuts import render
from django.views.generic import TemplateView
from hotel.models import Hotel
from hotel_types.models import HotelType
# Create your views here.

def home(request,type_slug = None):
    hotel = Hotel.objects.all() 
    if type_slug is not None: 
        hotel_types = HotelType.objects.get(slug = type_slug) 
        hotel = Hotel.objects.filter(hotel_types  = hotel_types) 
    hotel_types = HotelType.objects.all() 
    return render(request, 'index.html', {'hotel' : hotel, 'hotel_types' : hotel_types})


    