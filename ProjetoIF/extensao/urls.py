from django.urls import path, include
from .views import *

urlpatterns = [
    path('projetos_lista/', projetos_lista, name='projetos_lista'),
    path('detalhes_projeto/<int:id>', detalhes_projeto, name='detalhes_projeto'),
    path('aluno_detalhes/<int:id>', aluno_detalhes, name='aluno_detalhes'),
    path('alunos_lista/', alunos_lista, name='alunos_lista'),
    path('criar_categoria/', criar_categoria, name='criar_categoria'),
    path('editar_categoria/<int:id>/', editar_categoria, name='editar_categoria'),
    path('listar_categorias/', listar_categorias, name='listar_categorias'),
    path('excluir_categoria/<int:id>/', excluir_categoria, name='excluir_categoria')
]
