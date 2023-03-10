from django import forms
from django.contrib.auth.models import User
from utils.django_form import add_attr
from django.core.exceptions import ValidationError
from persons.models import Person


class RegisterUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = ['first_name', 'last_name', 'CPF', 'data_nasc', 'email', 'password', 'password2']
        for field in fields:
            add_attr(self.fields.get(field, ''), 'class', 'form-control')

    first_name = forms.CharField(
        label='Nome',
        error_messages={
            'required': 'Escreva seu Nome'
        }
    )
    last_name = forms.CharField(
        label='Sobrenome',
        error_messages={
            'required': 'Escreva seu Sobrenome'
        }
    )
    CPF = forms.CharField(
        label="CPF",
        error_messages={
            'required': 'Escreava seu CPF'
        },
        max_length=11,
    )
    data_nasc = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(
            attrs={
                'type': 'date'
                }
            ),
    )
    email = forms.CharField(
        label='E-mail',
        error_messages={
            'required': 'Escreva seu e-mail'
        },
        help_text="Escreva um e-mail valido"
    )
    password = forms.CharField(
        label='Senha',
        error_messages={
            'required': 'Escreva sua senha'
        },
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        error_messages={
            'required': 'Escreva sua senha'
        },
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'CPF',
            'data_nasc',
            'email',
            'password',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exist = User.objects.filter(email=email)
        if exist:
            raise ValidationError(
                'E-mail já cadastrado'
            )
        
        return email
    
    def clean_CPF(self):
        cpf = self.cleaned_data.get('CPF', '')
        exist = Person.objects.filter(
            cpf=cpf
        )
        if exist:
            raise ValidationError(
                'CPF já cadastrado'
            )
        
        return cpf

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise ValidationError({
                'password': 'As senhas precisam estar iguais',
                'password2': 'As senhas precisam estar iguais'
            })
    
    def save(self, commit=True):
        user = super().save(commit)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            person = Person.objects.filter(
                author=user
            )
            person.update(
                CPF=self.cleaned_data['CPF'],
                data_nasc=self.cleaned_data['data_nasc']
            )
        return user