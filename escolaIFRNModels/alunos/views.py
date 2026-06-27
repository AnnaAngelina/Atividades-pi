from django.shortcuts import render
from .models import Aluno

# Create your views here.
def listAlunos(request):
    aluno = Aluno.objects.all()
    context = {'alunos': aluno, 'autorizado': True, 'mostrar_alerta': True}
    return render(request, 'alunos/list-alunos.html', context)

def detalhesAluno(request, id):
    aluno = Aluno.objects.filter(id=id).first()
    context = {'aluno': aluno}
    return render(request, 'alunos/detalhes-aluno.html', context)

