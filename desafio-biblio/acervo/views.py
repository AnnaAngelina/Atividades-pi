from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def listarLivros(request):
    livros = models.Livro.objects.all()

    return render(request, 'acervo/listarLivros.html', {'livros': livros})

def detalheslivro(request, id):
    livro = get_object_or_404(models.Livro, id=id)

    return render(request, 'acervo/detalhesLivro.html', {'livro': livro})