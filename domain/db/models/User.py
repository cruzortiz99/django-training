from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    second_name = models.CharField(max_length=200, null=False, blank=True)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False,
                              unique=True)
    birth_date = models.DateField(null=False)
    confirmed = models.BooleanField(null=False, default=False)
