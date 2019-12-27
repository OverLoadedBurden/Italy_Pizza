from django.db import models


# Create your models here.
class Desert(models.Model):
    name = models.CharField(max_length=80)
    image = models.BinaryField()
    ingredient = models.TextField()
    cost = models.FloatField()
