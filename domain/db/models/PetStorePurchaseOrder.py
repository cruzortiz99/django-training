from django.db import models
from domain.db.models.PetStore import PetStore
from domain.db.models.User import User


class PetStorePurchaseOrder(models.Model):
    pet_store = models.ForeignKey(to=PetStore, null=False,
                                  on_delete=models.deletion.CASCADE)
    buyer = models.ForeignKey(to=User, null=False,
                              on_delete=models.deletion.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
