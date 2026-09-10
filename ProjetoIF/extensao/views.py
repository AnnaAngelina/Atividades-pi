from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

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
