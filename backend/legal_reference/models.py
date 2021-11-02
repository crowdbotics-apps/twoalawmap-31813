from django.conf import settings
from django.db import models


class Local_data(models.Model):
    "Generated Model"
    county = models.TextField()
    state = models.TextField(
        null=True,
        blank=True,
    )
    risk = models.IntegerField(
        null=True,
        blank=True,
    )


# Create your models here.
