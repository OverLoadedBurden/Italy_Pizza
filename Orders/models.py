from django.db import models
from django.utils.timezone import now


# Create your models here.
class Order(models.Model):
    loc = models.TextField()
    orders = models.TextField()
    date = models.DateTimeField(default=now)
