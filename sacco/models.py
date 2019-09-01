from django.db import models
# Create your models here.


class Sacco(models.Model):
    name = models.CharField(
        verbose_name="Sacco name",
        max_length=100,
        unique=True)
    sacco_id = models.CharField(
        verbose_name="Sacco ID",
        max_length=100,
        primary_key=True)
    manager = models.CharField(max_length=100,verbose_name="Store manager")
