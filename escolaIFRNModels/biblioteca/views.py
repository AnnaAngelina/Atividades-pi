from django.shortcuts import render
from .models import Livro

# Create your views here.
def listLivros(request):
    livros = Livro.objects.all()
    context = {'livros': livros}
    return render(request, 'biblioteca/list-livros.html', context)

def livroDetalhe(request, id):
    livroselecionado = Livro.objects.filter(id=id).first()
    context = {'livro_selecionado': livroselecionado}
    return render(request, 'biblioteca/detalhes.html', context)


