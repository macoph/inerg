from django.db import models

# Create your models here.

class Production(models.Model):
    api_well_number = models.BigIntegerField(primary_key=True)
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()

    def __int__(self):
        return self.api_well_number