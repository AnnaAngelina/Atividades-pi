from django.shortcuts import render
from extensao import models

# Create your views here.
def home(request):
    qtd_projetos = models.Projeto.objects.all().count()
    qtd_alunos = models.Aluno.objects.all().count()

    return render(request, 'core/home.html', {'qtd_projetos': qtd_projetos, 'qtd_alunos': qtd_alunos})