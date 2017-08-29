from rest_framework import viewsets
from .models import CriticalAssetType, CriticalAsset
from .serializers import CriticalAssetTypeSerializer, CriticalAssetSerializer

class CriticalAssetViewSet(viewsets.ModelViewSet):
    queryset = CriticalAsset.objects.all()
    serializer_class = CriticalAssetSerializer

class CriticalAssetTypeViewSet(viewsets.ModelViewSet):
    queryset = CriticalAssetType.objects.all()
    serializer_class = CriticalAssetTypeSerializer

# Create your views here.
