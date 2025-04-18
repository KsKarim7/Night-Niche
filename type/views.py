from rest_framework import generics
# from .serializers import TypeSerializer

# class TypeListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer

from rest_framework import viewsets
from .models import Type
from .serializers import TypeSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer



class TypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'id'
