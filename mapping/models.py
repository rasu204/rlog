from django.db import models, migrations
from django.contrib.postgres.fields import HStoreField


# Create your models here.
class Mapping(models.Model):
    # MappingID = models.IntegerField(primary_key = True)
    #UserID = models.ForeignKey('user.User', on_delete=models.RESTRICT)
    MappingFor = models.TextField(null=True)
    #CreatedOn = models.DateField(auto_now_add=True, null=True)
    Mappings = HStoreField(null=True)
