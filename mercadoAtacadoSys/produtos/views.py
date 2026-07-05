from django.shortcuts import render

# Create your views here.
def returnProdutos():
    produtos = [{
            "id": 1,
            "nome": "Maçã Gala",
            "categoria": "Frutas",
            "preco": 9.90,
            "descricao": (
                "A Maçã Gala é uma das frutas mais apreciadas pelos brasileiros devido ao seu sabor doce, textura crocante e suculenta. Rica em fibras, vitaminas e antioxidantes, é ideal para consumo in natura, preparo de sobremesas, sucos e saladas de frutas. Produto selecionado, fresco e de alta qualidade, vendido em embalagem de aproximadamente 1 kg."
            )},
        {
            "id": 2,
            "nome": "Leite Integral",
            "categoria": "Laticínios",
            "preco": 5.49,
            "descricao": (
                "Leite integral de excelente qualidade, rico em cálcio, proteínas e vitaminas essenciais para uma alimentação equilibrada. Possui sabor suave e textura cremosa, sendo ideal para consumo puro, preparo de cafés, vitaminas, sobremesas e diversas receitas culinárias. Embalagem longa vida com 1 litro."
            )},
        {
            "id": 3,
            "nome": "Pão Francês",
            "categoria": "Padaria",
            "preco": 7.99,
            "descricao": (
                "Pão francês produzido diariamente com ingredientes selecionados, apresentando casca crocante e miolo macio. Ideal para o café da manhã ou lanche da tarde, podendo ser acompanhado de manteiga, frios, geleias ou outros recheios. Produto vendido em embalagem com aproximadamente 500 gramas."
            )},
        {
            "id": 4,
            "nome": "Carne Bovina",
            "categoria": "Carnes",
            "preco": 39.90,
            "descricao": (
                "Carne bovina fresca, cuidadosamente selecionada para garantir maciez, sabor e qualidade. Indicada para grelhados, assados, cozidos e churrascos. Armazenada sob rigorosos padrões de higiene e conservação, oferecendo um produto seguro e de excelente procedência. Venda por quilograma."
            )}
        ]
    return produtos
    

def listaProdutos(request):
    context = {'produtos': returnProdutos()}
    return render(request, 'produtos/listaprodutos.html', context)


def detalhesProduto(request, id):
    for i in returnProdutos():
        if i['id'] == id:
            context = {'produto': i}
    return render(request, 'produtos/detalhes.html', context)