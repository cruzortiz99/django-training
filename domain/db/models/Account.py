from django.db import models

from domain.db.models.BaseModel import BaseModel
from domain.db.models.AdoptionCenter import AdoptionCenter
from domain.db.models.PetStore import PetStore


class Account(BaseModel):
    class Meta:
        db_table = "account"

    first_name = models.CharField(max_length=200, null=False, blank=False)
    second_name = models.CharField(max_length=200, null=False, blank=True)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    birth_date = models.DateField(null=False)
    email = models.fields.EmailField(max_length=200, unique=True,
                                     blank=False, null=False)
    password = models.fields.CharField(max_length=14, null=False,
                                       blank=False)
    confirmed = models.fields.BooleanField(default=False)
    in_adoption_center = models.ForeignKey(to=AdoptionCenter, null=True,
                                           on_delete=models.deletion.SET_NULL)
    in_pet_store = models.ForeignKey(to=PetStore, null=True,
                                     on_delete=models.deletion.SET_NULL)
