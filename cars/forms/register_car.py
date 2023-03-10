from django import forms
from cars.models import Car
from persons.models import Person
from utils.django_form import add_attr
from django.core.exceptions import ValidationError


class RegisterCar(forms.ModelForm):
    def __init__(self, *args, **Kwargs):
        self.user = Kwargs.pop('user')
        super().__init__(*args, **Kwargs)
        model = self.fields.get('model', '')
        color = self.fields.get('color', '')
        add_attr(model, 'class', 'form-control')
        add_attr(color, 'class', 'form-control')

    class Meta:
        model = Car
        fields = 'model', 'color'

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        person = Person.objects.filter(
            author=self.user
        ).first()
        if person.is_sales_opportunity is False:
            count_cars = Car.objects.filter(
                    owner=person
                ).count()
            if count_cars == 3:
                raise ValidationError(
                    'Não é possível registrar mais de 3 carros por pessoa'
                )


    def save(self, commit=False):
        car = super().save(commit)
        if commit:
            car.save()
        user = self.user
        person = Person.objects.filter(
            author=user
        ).first()
        car.owner = person
        if person.is_sales_opportunity is True:
            person.is_sales_opportunity = False
            person.save()
        return car