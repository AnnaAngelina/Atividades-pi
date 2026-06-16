from django.shortcuts import render

def menu_view(request):
    context = {
        'nome_loja': 'Greek Burger',
        'loja_aberta': False,
        'promocao_do_dia': {'nome': 'Bauru', 'descricao': 'rosbife fatiado, tomate em rodelas, pepino em conserva (picles) e uma mistura derretida de queijos, tudo servido dentro de um pão francês crocante', 'preco': 15},
        'lanches': [
            {'nome': 'Cheeseburger', 'preco': 10},
            {'nome': 'Bacon Duplo', 'preco': 12},
            {'nome': 'Vegano', 'preco': 15},
            {'nome': 'Batata Rústica', 'preco': 10},
            {'nome': 'Bauru', 'preco': 17},
            {'nome': 'X-tudo', 'preco': 15},
        ]
    }
    return render(request, 'core/cardapio.html', context)