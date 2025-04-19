from rest_framework import serializers
from .models import HotelType
from django.utils.text import slugify

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelType
        fields = '__all__'

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)