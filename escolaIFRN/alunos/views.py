from django.shortcuts import render

# Create your views here.
def listAlunos(request):
    alunos = [
        {"matricula": "20231094010023", "nome": "Angelina Oliveira"},
        {"matricula": "20231094010024", "nome": "Guilherme Alves"},
        {"matricula": "20231094010025", "nome": "Luma Batista"},
        {"matricula": "20231094010026", "nome": "Eduarda Guedes"},
        {"matricula": "20231094010027", "nome": "Letícia Maria"}]
    context = {'alunos': alunos, 'autorizado': True, 'mostrar_alerta': True}
    return render(request, 'alunos/list-alunos.html', context)