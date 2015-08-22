from django.db import models
import datetime

# Create your models here.
class Status(models.Model):
    index     = models.IntegerField()
    #update_date = models.DateField("Date", blank=True, null=True)
    #update_time = models.TimeField("Time", blank=True, null=True)
    update_date = models.CharField(max_length=20, blank=True, null=True)
    update_time = models.CharField(max_length=20, blank=True, null=True)
    qua_id    = models.CharField(max_length=20, blank=True, null=True)
    name      = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    latitude  = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    qua_cntu  = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    qua_cl    = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    qua_ph    = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    normal    = models.BooleanField(default=True)

    def __str__(self):
        return self.name
