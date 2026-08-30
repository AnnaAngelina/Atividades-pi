from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarLivros, name='listar_livros'),
    path('detalhes/<int:id>/', views.detalheslivro, name='detalhesLivro'),
]