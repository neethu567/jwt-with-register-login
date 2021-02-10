# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    country_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.country_name


class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    c_password = models.CharField(max_length=50,null=True,blank=True)
    country = models.ManyToManyField(Country, related_name="travel_country")
    phone = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=500, null=True)
    token = models.CharField(max_length=500,null=True,default="")

    def __str__(self):
        return str(self.id)
