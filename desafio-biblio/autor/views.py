from django.shortcuts import render, get_object_or_404
from . import models
from acervo import models as m

# Create your views here.
def listarAutores(request):
    autores = models.Autor.objects.all()

    return render(request, 'autor/listarAutores.html', {'autores': autores})

def detalhesAutor(request, id):
    autor = get_object_or_404(models.Autor, id=id)
    livros = m.Livro.objects.filter(autor=autor)

    return render(request, 'autor/detalhesAutor.html', {'autor': autor, 'livros': livros})