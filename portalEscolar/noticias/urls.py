from django.urls import path, include
from .views import *

urlpatterns = [
    path('listar_noticias/', listar_noticias, name='listar_noticias'),
    path('listar_categorias/', listar_categorias, name='listar_categorias'),
    path('detalhes_noticia/<int:id>', detalhes_noticia, name='detalhes_noticia'),
    path('listar_tags/', listar_tags, name='listar_tags'),
]