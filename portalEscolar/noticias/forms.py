from django import forms
from django.shortcuts import redirect
from .models import Categoria, Noticia, Tag

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['manchete', 'categoria', 'descricao', 'tags']
        labels = {
            'manchete': 'Manchete', 'categoria': 'Categoria', 'descricao': 'Descrição', 'tags': 'Tags'
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['titulo']
        labels = {
            'titulo': 'Titulo da manchete'
        }
