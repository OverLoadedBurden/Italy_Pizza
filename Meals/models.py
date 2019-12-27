from django.db import models
from django.conf import settings


# Create your models here.
class Types(models.Model):
    name = models.CharField(max_length=80)
    image = models.BinaryField()

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=80)
    image = models.BinaryField()
    ingredient = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.name


class Rate(models.Model):
    rate = models.FloatField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
