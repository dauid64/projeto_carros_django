from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'registrar/',
        views.RegisterCarView.as_view(),
        name='register'
    )
]