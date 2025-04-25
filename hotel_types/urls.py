# from django.urls import path
# from . import views

# urlpatterns = [
#     path('types/', views.TypeListCreateAPIView.as_view(), name='Type_list_create'),
#     path('types/<int:id>/', views.TypeRetrieveUpdateDestroyAPIView.as_view(), name='Type_detail'),
# ]


# from rest_framework.routers import DefaultRouter
# from .views import TypeViewSet
# from django.urls import path, include

# router = DefaultRouter()
# router.register('', TypeViewSet)

# urlpatterns = [
#     path('',include(router.urls)),
# ]  

from rest_framework.routers import DefaultRouter
from .views import TypeViewSet 

router = DefaultRouter()
router.register(r'', TypeViewSet, basename='hotel_types') 

urlpatterns = router.urls

