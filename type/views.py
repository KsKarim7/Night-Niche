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
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {
            'message': 'Hotel Type created successfully!',
            'name': '',
            'slug': ''
        }
        return response


class TypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HotelType.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'id'
