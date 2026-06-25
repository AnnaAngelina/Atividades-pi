from django.shortcuts import render

def livrosreturn():
    livros = [{'id': 1, 'titulo': 'A cabeça do santo', 'autor': 'Socorro Acioli', 'ano': 2014, 'prioridade_leitura': 2, 'sinopse': 'Samuel encontra abrigo dentro da cabeça de uma enorme estátua de santo e sua vida passa por transformações inesperadas.'},
              {'id': 2, 'titulo': 'A hora da estrela', 'autor': 'Clarice Lispector', 'ano': 1977, 'prioridade_leitura': 1, 'sinopse': 'A história de Macabéa, uma jovem nordestina que vive à margem da sociedade no Rio de Janeiro.'},
              {'id': 3, 'titulo': 'Vidas Secas', 'autor': 'Graciliano Ramos', 'ano': 1938, 'prioridade_leitura': 1, 'sinopse': 'Uma família sertaneja enfrenta a seca e a miséria no interior do Nordeste brasileiro.'},
              {'id': 4, 'titulo': 'Uma pequena coreografia do Adeus', 'autor': 'Aline Bei', 'ano': 2021, 'prioridade_leitura': 3, 'sinopse': 'Um romance poético sobre afetos, perdas e reconstrução emocional de uma garota chamada Júlia'}]
    return livros

# Create your views here.
def listLivros(request):
    context = {'livros': livrosreturn()}
    return render(request, 'biblioteca/list-livros.html', context)

def livroDetalhe(request, id):
    for livro in livrosreturn():
        if livro['id'] == id:
            livroselecionado = livro
    context = {'livro_selecionado': livroselecionado}
    return render(request, 'biblioteca/detalhes.html', context)


