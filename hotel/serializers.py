from rest_framework import serializers
from .models import Hotel, RoomType, Room
from hotel_types.models import HotelType

class HotelSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(many=True, queryset=HotelType.objects.all())

    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room_type = serializers.PrimaryKeyRelatedField(queryset=RoomType.objects.all())

    class Meta:
        model = Room
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())

    class Meta:
        model = RoomType
        fields = '__all__'
