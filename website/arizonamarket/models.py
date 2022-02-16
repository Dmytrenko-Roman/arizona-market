from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    server = models.TextField(null=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('market')


class Car(models.Model):
    model = models.TextField(null=False)
    twinturbo = models.BooleanField(default=False)
    mileage = models.IntegerField(null=False)
    price = models.IntegerField(default=0)

    owner = models.ForeignKey("CustomUser", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('market')
