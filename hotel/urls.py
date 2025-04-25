from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomTypeViewSet, RoomViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet, basename='hotels')
router.register(r'roomtypes', RoomTypeViewSet, basename='roomtypes')
router.register(r'rooms', RoomViewSet, basename='rooms')

urlpatterns = router.urls
