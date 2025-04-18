from rest_framework.routers import DefaultRouter
from .views import TypeViewSet

router = DefaultRouter()
router.register(r'types', TypeViewSet)

urlpatterns = router.urls
