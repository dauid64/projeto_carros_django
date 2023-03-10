from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    CPF = models.CharField(max_length=11, blank=True)
    data_nasc = models.DateField(null=True, blank=True)
    is_sales_opportunity = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.CPF