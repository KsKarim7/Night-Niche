from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from type.models import HotelType
 

class Hotel(models.Model):
  name = models.CharField(max_length=255)
  type = models.ManyToManyField(HotelType) 
  rating = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
  address = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=11, blank=True, null=True)
  email_address = models.EmailField(blank=True, null=True)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to='posts/media/uploads/',blank = True, null = True)
 

  def __str__(self):
    return self.name
 
class RoomType(models.Model):
  name = models.CharField(max_length=100)  
  size = models.IntegerField(blank=True, null=True) 
  bed_options = models.CharField(max_length=255, blank=True, null=True)
  hotel = models.ForeignKey(Hotel, related_name='room_types', on_delete=models.CASCADE)
 

  def __str__(self):
    return f"{self.name} at {self.hotel.name}"
 

class Room(models.Model):
  room_type = models.ForeignKey(RoomType, related_name='rooms', on_delete=models.CASCADE)
  number = models.CharField(max_length=50)
  price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
  is_available = models.BooleanField(default=True)
 

  def __str__(self):
    return f"{self.room_type} - Room {self.number}"