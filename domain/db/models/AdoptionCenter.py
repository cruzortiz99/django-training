from django.db import models
from domain.db.models.BaseModel import BaseModel


class AdoptionCenter(BaseModel):
    class Meta:
        db_table = "\"adoption_center\""

    name = models.CharField(unique=True, max_length=200,
                            blank=False, null=False)
    country = models.CharField(null=False, blank=False, max_length=200)
    province = models.CharField(null=False, blank=False, max_length=200)
    city = models.CharField(null=False, blank=False, max_length=200)
