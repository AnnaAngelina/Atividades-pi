from django.urls import path, include
from .views import *

urlpatterns = [
    #categorias
    path('listar_categorias/', listar_categorias, name='listar_categorias'),
    path('criar_categoria/', criar_categoria, name='criar_categoria'),
    path('editar_categoria/<int:id>/', editar_categoria, name='editar_categoria'),
    path('listar_categorias/', listar_categorias, name='listar_categorias'),
    path('excluir_categoria/<int:id>/', excluir_categoria, name='excluir_categoria'),
    #noticias
    path('listar_noticias/', listar_noticias, name='listar_noticias'),
    path('detalhes_noticia/<int:id>', detalhes_noticia, name='detalhes_noticia'),
    path('adicionar_noticia/', adicionar_noticia, name='adicionar_noticia'),
    path('editar_noticia/<int:id>/', editar_noticia, name='editar_noticia'),
    path('excluir_noticia/<int:id>/', excluir_noticia, name='excluir_noticia'),
    #tags
    path('listar_tags/', listar_tags, name='listar_tags'),
    path('criar_tag/', criar_tag, name='criar_tag'),
    path('excluir_tag/<int:id>/', excluir_tag, name='excluir_tag'),
    path('editar_tag/<int:id>/', editar_tag, name='editar_tag'),
    path('detalhes_tag/<int:id>/', detalhes_tag, name='detalhes_tag'),
]