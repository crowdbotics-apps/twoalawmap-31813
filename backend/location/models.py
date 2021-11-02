from django.conf import settings
from django.db import models


class User_location(models.Model):
    "Generated Model"
    lat = models.IntegerField()
    long = models.IntegerField(
        null=True,
        blank=True,
    )
    user_ip = models.IntegerField(
        null=True,
        blank=True,
    )
    timestamp = models.DateTimeField(
        null=True,
        blank=True,
    )


# Create your models here.
