from django.db import models

class ContractType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    seen_code = models.CharField(max_length=10)
    org_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    contract_start = models.DateField("تاریخ شروع قرارداد")
    contract_end = models.DateField("تاریخ اتمام قرارداد")
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)