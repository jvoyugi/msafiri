from django.db import models
from vehicle.models import Vehicle
# Create your models here.


class Seat(models.Model):
    seat_number = models.PositiveIntegerField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    is_taken = models.BooleanField(default=False)
