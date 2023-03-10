from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from persons.forms.register_user import RegisterUserForm
from django.contrib import messages

# Create your views here.
class RegisterPerson(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(
            request,
            'persons/pages/register.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        POST = request.POST
        form = RegisterUserForm(POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado com sucesso!')
            return redirect(
                reverse('persons:register')
            )
        return render(
            request,
            'persons/pages/register.html',
            context={
                'form': form
            }
        )
            