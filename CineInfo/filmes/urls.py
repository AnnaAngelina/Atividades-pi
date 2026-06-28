from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.listaFilmes, name='lista_filmes'),
]
