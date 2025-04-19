from rest_framework import serializers
from .models import Hotel, RoomType, Room
from type.serializers import TypeSerializer
from type.models import HotelType

class HotelSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(many=True, queryset=HotelType.objects.all())

    class Meta:
        model = Hotel
        fields = '__all__'

