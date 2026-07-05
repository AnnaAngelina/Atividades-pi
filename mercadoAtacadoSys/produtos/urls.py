from django.urls import path
from . import views

urlpatterns = [
    path('listarProdutos/', views.listaProdutos, name='listaProdutos'),
    path('detralhesProduto/<int:id>', views.detalhesProduto, name='detalhesProduto'),
]
