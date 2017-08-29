from django.db import models


class CriticalAssetType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Critical asset type"
        verbose_name_plural = "Critical asset types"

    def __unicode__(self):
        return self.name


class CriticalAsset(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    critical_asset_type = models.ForeignKey(CriticalAssetType)

    class Meta:
        verbose_name = "Critical asset"
        verbose_name_plural = "Critical assets"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
# Create your models here.
