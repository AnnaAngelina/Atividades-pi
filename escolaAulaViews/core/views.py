from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def listEstudantes(request):
    alunos = ['Rogério', 'Agata', 'Maria', 'Lúcia', 'Ruan']
    notas = [9.5, 9, 10, 8, 9]
    lista = []
    for a in range(len(alunos)):
        lista.append({'aluno': alunos[a], 'nota': notas[a]})
    context = {
        'alunos': lista
    }
    return render(request, 'core/listalunos.html', context)

def sobreNos(request):
    context = {
       'nome': 'Escola Horizonte do Saber',
       'fundacao': 2005,
       'anos': [
           '9º ano', '8º ano', '7º ano', '6º ano'
       ]}
    return render(request, 'core/sobrenos.html', context)
