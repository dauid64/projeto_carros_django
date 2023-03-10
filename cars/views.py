from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from cars.models import Car
from cars.forms.register_car import RegisterCar
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        user = request.user
        cars = Car.objects.filter(
            owner__author=user.id
        )
        return render(
            request,
            'cars/pages/home.html',
            context={
            'cars': cars
            }
        )

class RegisterCarView(View):
    def get(self, request):
        form = RegisterCar(user=request.user)
        return render(
            request,
            'cars/pages/register.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        POST = request.POST
        form = RegisterCar(
            POST,
            user=request.user
        )
        if form.is_valid():
            form.save()
            form.save(commit=True)
            messages.success(request, 'Carro registrado com sucesso!')
            return redirect(
                reverse('cars:home')
            )
        else:
            return render(
                request,
                'cars/pages/register.html',
                context={
                    'form': form
                }
            )
