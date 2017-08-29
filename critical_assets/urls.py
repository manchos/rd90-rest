from django.conf.urls import url
from rest_framework import routers
from .views import CriticalAssetViewSet, CriticalAssetTypeViewSet

router = routers.DefaultRouter()
router.register(r'criticalassets', CriticalAssetViewSet)
router.register(r'criticalassettypes', CriticalAssetTypeViewSet)

urlpatterns = router.urls