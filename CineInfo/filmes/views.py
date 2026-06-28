from django.shortcuts import render
from .models import Filme

# Create your views here.
def listaFilmes(request):
    filmes = Filme.objects.all()
    context = {'filmes': filmes}
    return render(request, 'filmes/lista-filmes.html', context)