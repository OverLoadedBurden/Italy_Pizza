from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    image = models.BinaryField()

    def __str__(self):
        return self.name
