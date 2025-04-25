from django.contrib import admin
from .models import Hotel, RoomType, Room

# Register your models here.
admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Room)