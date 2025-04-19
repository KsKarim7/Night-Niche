from rest_framework import generics
from django.shortcuts import redirect
# from .serializers import TypeSerializer

# class TypeListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer

from rest_framework import viewsets
from .models import HotelType
from .serializers import TypeSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = HotelType.objects.all()
    serializer_class = TypeSerializer
    


class TypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HotelType.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'id'
