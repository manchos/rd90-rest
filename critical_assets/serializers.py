from rest_framework import serializers
from .models import CriticalAssetType, CriticalAsset

class CriticalAssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
    	model = CriticalAssetType
    	fields = '__all__'

class CriticalAssetSerializer(serializers.ModelSerializer):
	class Meta:
		model = CriticalAsset
		fields = '__all__'