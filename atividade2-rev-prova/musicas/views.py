from django.shortcuts import render

# Create your views here.
def lista(request):
    return render(request, 'musicas/lista.html')

def detalhe(request):
    return render(request, 'musicas/detalhe.html')