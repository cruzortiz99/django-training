from django.db import models
from domain.db.models.PetStore import PetStore
from domain.db.models.Account import Account

from domain.db.models.BaseModel import BaseModel


class PetStorePurchaseOrder(BaseModel):
    class Meta:
        db_table = "\"pet_store_purchase_order\""
    pet_store = models.ForeignKey(to=PetStore, null=False,
                                  on_delete=models.deletion.CASCADE)
    buyer = models.ForeignKey(to=Account, null=False,
                              on_delete=models.deletion.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=500, blank=True, null=True)
