from django.db import models

# Create your models here.

from django.db import models

class Horn(models.Model):
    horn_status = models.BooleanField()

class Gyro(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class SensorData(models.Model):
    horn = models.ForeignKey(Horn, on_delete=models.CASCADE)
    ru_id = models.CharField(max_length=100)
    gyro = models.ForeignKey(Gyro, on_delete=models.CASCADE)
    date = models.DateField()
    timestamp = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)





class VehicleData(models.Model):
    time = models.DateTimeField()
    horn = models.IntegerField()
    gyro = models.CharField(max_length=30)
    gps = models.CharField(max_length=30)