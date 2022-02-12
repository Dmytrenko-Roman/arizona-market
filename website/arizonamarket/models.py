from django.db import models


class Car(models.Model):
    model = models.TextField(null=False)
    twinturbo = models.BooleanField(default=False)
    mileage = models.IntegerField(null=False)
    price = models.IntegerField(default=0)
    
    owner = models.ForeignKey("Player", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.model

