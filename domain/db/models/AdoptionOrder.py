from django.db import models
import enum
from domain.db.models.AdoptionCenter import AdoptionCenter
from domain.db.models.User import User
from domain.db.models.Pet import Pet


class AdoptionOrderStatus(enum.Enum):
    SUCCESS = "success"
    PENDING = "pending"
    REJECTED = "rejected"
    REVERTED = "reverted"


class AdoptionOrder(models.Model):
    class Meta:
        db_table = "\"adoption_order\""
    adoption_center = models.ForeignKey(to=AdoptionCenter, null=False,
                                        on_delete=models.deletion.CASCADE)
    adopter = models.ForeignKey(to=User, null=False,
                                on_delete=models.deletion.CASCADE)
    pet = models.ForeignKey(to=Pet, null=False,
                            on_delete=models.deletion.CASCADE)
    current_status = models.CharField(max_length=50, choices=[
        (
            AdoptionOrderStatus.SUCCESS.value,
            AdoptionOrderStatus.SUCCESS.name
        ),
        (
            AdoptionOrderStatus.PENDING.value,
            AdoptionOrderStatus.PENDING.name
        ),
        (
            AdoptionOrderStatus.REJECTED.value,
            AdoptionOrderStatus.REJECTED.name
        ),
        (
            AdoptionOrderStatus.REVERTED.value,
            AdoptionOrderStatus.REVERTED.name
        )
    ], default=AdoptionOrderStatus.PENDING.value)
