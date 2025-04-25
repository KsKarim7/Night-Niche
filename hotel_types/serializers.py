from rest_framework import serializers
from .models import HotelType
from django.utils.text import slugify

class HotelTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelType
        fields = '__all__'

    def create(self, validated_data):
        slug = validated_data.get('slug') or slugify(validated_data['name'])
        if HotelType.objects.filter(slug=slug).exists():
            raise serializers.ValidationError({'slug': 'Slug already exists.'})
        validated_data['slug'] = slug
        return super().create(validated_data)
