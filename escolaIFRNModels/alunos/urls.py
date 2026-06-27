from django.urls import path
from . import views

urlpatterns = [
    path('', views.listAlunos, name='list_alunos'),
    path('detalhes/<int:id>', views.detalhesAluno, name='detalhe_aluno'),
]