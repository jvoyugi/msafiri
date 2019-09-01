from django.db import models
from django.contrib.auth.models import AbstractUser
from sacco.models import Sacco
# Create your models here.


class Employee(AbstractUser):
    employee_id = models.CharField(
        max_length=100, verbose_name="Employee number", primary_key=True)
    sacco = models.ForeignKey(
        Sacco, on_delete=models.CASCADE, verbose_name="Sacco")

class Driver(Employee):
    is_driver=models.BooleanField(default=True)