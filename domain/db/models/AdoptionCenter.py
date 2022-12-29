from django.db import models


class AdoptionCenter(models.Model):
    name = models.CharField(unique=True, max_length=200,
                            blank=False, null=False)
    email = models.EmailField(unique=True, max_length=200,
                              blank=False, null=False)
    confirmed = models.BooleanField(null=False, default=False)
    country = models.CharField(null=False, blank=False, max_length=200)
    province = models.CharField(null=False, blank=False, max_length=200)
    city = models.CharField(null=False, blank=False, max_length=200)