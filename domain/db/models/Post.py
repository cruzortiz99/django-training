from django.db import models
from domain.db.models.Account import Account

from domain.db.models.BaseModel import BaseModel


class Post(BaseModel):
    class Meta:
        db_table = "post"
    created_by = models.ForeignKey(to=Account,
                                   on_delete=models.deletion.CASCADE,
                                   null=False)
    description = models.TextField(max_length=500, null=True, blank=True)
