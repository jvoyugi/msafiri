from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(verbose_name="Location", max_length=100)
    location_id = models.CharField(
        verbose_name="Location ID",
        max_length=100,
        primary_key=True)
