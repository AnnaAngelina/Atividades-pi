from django.urls import path, include
from .views import *

urlpatterns = [
    path('projetos_lista/', projetos_lista, name='projetos_lista'),
    path('detalhes_projeto/<int:id>', detalhes_projeto, name='detalhes_projeto'),
    path('aluno_detalhes/<int:id>', aluno_detalhes, name='aluno_detalhes'),
    path('alunos_lista/', alunos_lista, name='alunos_lista'),
]
