from django.urls import path
from . import views

urlpatterns = [
    path('listaServicos/', views.listaServicos, name='listaServicos'),
    path('detalheServico/<int:id>', views.detalheServico, name='detalheServico'),
]
