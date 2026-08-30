from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarAutores, name='listar_autores'),
    path('detalhes_autor/<int:id>/', views.detalhesAutor, name='detalhesAutor')
]