from django.db import models
from accounts.models import Driver
# Create your models here.


class Vehicle(models.Model):
    TYPE_CLASS = (
        ('A', 'Luxury'),
        ('B', 'Standard'),
    )
    capacity = models.PositiveIntegerField()
    number_plate = models.CharField(
        max_length=15,
        verbose_name="Number plate",
        primary_key=True)
    driver = models.OneToOneField(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Driver")
    vehicle_type = models.CharField(
        max_length=2,
        choices=TYPE_CLASS,
        null=False,
        blank=False)
    
