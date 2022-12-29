from django.db import models


class User(models.Model):
    class Meta:
        db_table = "user"

    first_name = models.CharField(max_length=200, null=False, blank=False)
    second_name = models.CharField(max_length=200, null=False, blank=True)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False,
                              unique=True)
    password = models.CharField(max_length=14, null=False, blank=False)
    birth_date = models.DateField(null=False)
    confirmed = models.BooleanField(null=False, blank=False)
