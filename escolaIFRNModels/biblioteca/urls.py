from django.urls import path
from . import views

urlpatterns = [
    path('', views.listLivros, name='list_livros'),
    path('livro/<int:id>/', views.livroDetalhe, name='livro-detalhe'),
]