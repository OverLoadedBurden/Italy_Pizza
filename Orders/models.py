from django.db import models
from django.utils.timezone import now


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=80)
    location = models.TextField()
    phone = models.CharField(max_length=14)
    meals = models.TextField()
    drinks = models.TextField()
    deserts = models.TextField()
    date = models.DateTimeField(default=now)
    done = models.BooleanField(default=False)
    deliver_date = models.DateTimeField(null=True)
    total = models.FloatField(default=0.0)

    def deliver(self):
        self.done = True
        self.deliver_date = now()
        self.save()
