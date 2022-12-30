from django.db import models
from domain.db.models.User import User

from domain.db.models.BaseModel import BaseModel


class Pet(BaseModel):
    class Meta:
        db_table = "pet"
    name = models.CharField(max_length=200, blank=False, null=False)
    specie = models.CharField(max_length=200, blank=False, null=False)
    race = models.CharField(max_length=200, blank=False, null=False)
    current_owner = models.ForeignKey(to=User, null=True,
                                      on_delete=models.deletion.DO_NOTHING)
