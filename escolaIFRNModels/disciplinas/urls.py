from django.urls import path
from . import views

urlpatterns = [
    path('', views.listDisciplinas, name='lista_disciplinas'),
]