from django.contrib import admin
from cars.models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    ...


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    ...


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    ...