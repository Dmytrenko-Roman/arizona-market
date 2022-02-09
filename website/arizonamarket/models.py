from django.db import models


class Player(models.Model):
    name = models.TextField(null=False)
    surname = models.TextField(null=False)
    server = models.TextField(null=False)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.TextField(null=False)
    twinturbo = models.BooleanField(default=False)
    mileage = models.IntegerField(null=False)
    price = models.IntegerField(null=True)
    
    owner = models.ForeignKey("Player", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.model

