from django.shortcuts import render

# Create your views here.
def index(request):
    nome_usuario = 'Estudante IFRN'
    context = {'usuario': nome_usuario}
    return render(request, 'core/index.html', context)