from django.urls import path
from persons import views

app_name = 'persons'

urlpatterns = [
    path(
        'registrar/',
        views.RegisterPerson.as_view(),
        name='register'
    )
]