from django.urls import path
from django.urls import include
from .import views

app_name = 'alunos'

urlpatterns = [
    path('lista/', views.lista_view, name='lista_alunos'),
    path('novo/', views.novo_view, name='novo_aluno'),
    path('detalhes/', views.detalhe_view, name='detalhes_aluno'),
]
