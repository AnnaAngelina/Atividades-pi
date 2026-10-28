from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import *
from django.db.models.deletion import ProtectedError

# Create your views here.
def projetos_lista(request):
    projetos = Projeto.objects.all()

    return render(request, 'extensao/lista_projetos.html', {'projetos': projetos})

def detalhes_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    return render(request, 'extensao/detalhes_projeto.html', {'projeto': projeto})

def alunos_lista(request):
    alunos = Aluno.objects.all()

    return render(request, 'extensao/lista_alunos.html', {'alunos': alunos})

def aluno_detalhes(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    return render(request, 'extensao/aluno_detalhes.html', {'aluno': aluno})

def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'extensao/listar_categorias.html', {'categorias': categorias})

def criar_categoria(request):

    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            Categoria.objects.create(nome=nome)

            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect('listar_categorias')

    else:
        form = CategoriaForm()

    return render(request, 'extensao/criar_categoria.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect('listar_categorias')
    else:
       form = CategoriaForm(instance=categoria)
    return render(request, 'extensao/editar_categoria.html', {'form': form})

def excluir_categoria(request, id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":

        try:
            categoria.delete()
            messages.error(request, "Categoria deletada com sucesso!")
        except ProtectedError:
            messages.error(request, "Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.")

        return redirect("listar_categorias")

    categoria.delete()
    return render(request, 'extensao/listar_categorias.html', {'categorias': categorias})