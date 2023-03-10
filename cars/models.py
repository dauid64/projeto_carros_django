from django.db import models
from persons.models import Person

class Color(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)



