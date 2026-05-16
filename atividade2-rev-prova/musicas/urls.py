from django.urls import path, include
from . import views

app_name = 'musicas'

urlpatterns = [
    path('lista', views.lista, name='lista-musicas'),
    path('detalhe', views.detalhe, name='detalhe-musicas'),
]
