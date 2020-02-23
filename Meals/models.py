from django.db import models
from django.conf import settings


# Create your models here.
class Types(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    image = models.BinaryField()

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    image = models.BinaryField()
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    cost = models.FloatField()
    ingredient = models.TextField(default='[]')
    additional_meals = models.TextField(default='[]')
    additional_drinks = models.TextField(default='[]')
    additional_deserts = models.TextField(default='[]')

    def __str__(self):
        return self.name
