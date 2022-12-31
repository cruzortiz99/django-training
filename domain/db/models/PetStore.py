from django.db import models

from domain.db.models.BaseModel import BaseModel


class PetStore(BaseModel):
    class Meta:
        db_table = "\"pet_store\""
    name = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=False, blank=False)
    province = models.CharField(null=False, blank=False, max_length=200)
    city = models.CharField(null=False, blank=False, max_length=200)
