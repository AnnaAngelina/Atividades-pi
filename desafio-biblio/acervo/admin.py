from django.contrib import admin
from .models import Livro

# Register your models here.

class LivroVizualizer(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'nome_editora')

admin.site.register(Livro, LivroVizualizer)
