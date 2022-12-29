from django.db import models


class PetStore(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=False, blank=False)
    province = models.CharField(null=False, blank=False, max_length=200)
    city = models.CharField(null=False, blank=False, max_length=200)
    email = models.EmailField(null=False, blank=False,
                              unique=False, max_length=200)
    confirmed = models.BooleanField(null=False, default=False)
