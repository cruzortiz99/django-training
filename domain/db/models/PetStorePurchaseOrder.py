from django.db import models
from domain.db.models.PetStore import PetStore
from domain.db.models.User import User

from domain.db.models.BaseModel import BaseModel


class PetStorePurchaseOrder(BaseModel):
    class Meta:
        db_table = "\"pet_store_purchase_order\""
    pet_store = models.ForeignKey(to=PetStore, null=False,
                                  on_delete=models.deletion.CASCADE)
    buyer = models.ForeignKey(to=User, null=False,
                              on_delete=models.deletion.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
