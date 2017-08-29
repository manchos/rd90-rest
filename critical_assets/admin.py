from django.contrib import admin
from .models import CriticalAssetType, CriticalAsset

admin.site.register(CriticalAssetType)
admin.site.register(CriticalAsset)
# Register your models here.
