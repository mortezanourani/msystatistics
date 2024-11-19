from django.db import models
from msystatistics.models import City, PropertyOwnership

# Create your models here.
class Gym(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    author_phone = models.CharField(max_length=200)
    issuance_date = models.DateField("تاریخ صدور پروانه")
    expire_date = models.DateField("تاریخ انقضا پروانه")
    proprietorship = models.ForeignKey(PropertyOwnership, on_delete=models.CASCADE)
    area = models.IntegerField("مساحت")

    def __str__(self):
        return "{} [{}]".format(self.name, self.author_name)
