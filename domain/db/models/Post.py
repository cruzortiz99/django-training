from django.db import models
from domain.db.models.User import User


class Post(models.Model):
    class Meta:
        db_table = "post"
    created_by = models.ForeignKey(to=User, on_delete=models.deletion.CASCADE,
                                   null=False)
    description = models.TextField(max_length=500, null=True, blank=True)
