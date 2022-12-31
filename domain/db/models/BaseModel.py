from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.fields.DateField(auto_now_add=True)
    updated_at = models.fields.DateField(auto_now=True)
    deleted_at = models.fields.DateField(auto_now=False,
                                         auto_created=False,
                                         auto_now_add=False,
                                         null=True)
