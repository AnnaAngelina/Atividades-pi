from django.urls import path
from . import views

urlpatterns = [
    path('', views.listAlunos, name='list_alunos'),
]