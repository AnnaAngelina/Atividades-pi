from django.shortcuts import render

# Create your views here.
def listDisciplinas(request):
    disciplinas = ["Django", "Python", "HTML"]
    context = {'disciplinas': disciplinas, 'autorizado': True}
    return render(request, 'disciplinas/list-disciplinas.html', context)