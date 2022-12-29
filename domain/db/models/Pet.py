from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    specie = models.CharField(max_length=200, blank=False, null=False)
    race = models.CharField(max_length=200, blank=False, null=False)
