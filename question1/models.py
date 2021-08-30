from django.db import models

# Create your models here.

class Vehicle(models.Model):
    plate = models.CharField(max_length=10)

class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()