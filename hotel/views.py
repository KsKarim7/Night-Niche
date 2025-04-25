from django.shortcuts import render

# Create your views here.
# class AddHotelCreateView(CreateView):
#     model = models.Hotel
#     form_class = forms.HotelForm
#     template_name = 'add_hotel.html'
#     success_url = reverse_lazy('add_hotel')
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    
from rest_framework import viewsets
from .models import Hotel, RoomType,Room
from .serializers import HotelSerializer, RoomTypeSerializer, RoomSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
