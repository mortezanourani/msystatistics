from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class PropertyOwnership(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
