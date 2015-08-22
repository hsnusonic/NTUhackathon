from django.db import models

# Create your models here.
class Status(models.Model):
    update_date = models.DateField('update date')
    update_time = models.TimeField()
    qua_id    = models.CharField(max_length=20)
    name      = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    latitude  = models.DecimalField(max_digits=8, decimal_places=5)
    qua_cntu  = models.DecimalField(max_digits=4, decimal_places=2)
    qua_cl    = models.DecimalField(max_digits=4, decimal_places=2)
    qua_ph    = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
