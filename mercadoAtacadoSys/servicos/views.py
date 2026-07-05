from django.shortcuts import render

def returnServico():
    servicos = [
        {
            "id": 1,
            "nome_servico": "Delivery",
            "responsavel": "Equipe de Logística",
            "tempo_estimado": "2 horas",
            "requisitos": [
                "O cliente deve possuir um endereço de entrega válido dentro da área de cobertura do mercado. ",
                "O pedido deve ser finalizado e o pagamento confirmado para que a entrega seja iniciada. ",
                "O horário de entrega está sujeito à disponibilidade da equipe de logística e às condições de trânsito. ",
                "O cliente deve permanecer disponível para receber os produtos no endereço informado."
            ]
        },{
            "id": 2,
            "nome_servico": "Produtos Frescos",
            "responsavel": "Setor de Hortifruti",
            "tempo_estimado": "Disponível diariamente",
            "requisitos": [
                "Os produtos são selecionados diariamente por colaboradores especializados para garantir qualidade, frescor e boas condições de consumo. ",
                "A disponibilidade pode variar conforme a sazonalidade, o fornecedor e o estoque do mercado. ",
                "Alguns itens podem possuir limite de compra em períodos de alta demanda."
            ]
        },{
            "id": 3,
            "nome_servico": "Pagamento Seguro",
            "responsavel": "Setor Financeiro",
            "tempo_estimado": "Confirmação em até 5 minutos",
            "requisitos": [
                "São aceitos cartões de crédito, cartões de débito, PIX e dinheiro, conforme disponibilidade da unidade. ",
                "Todas as transações eletrônicas são processadas em ambiente seguro, utilizando protocolos de criptografia para proteção das informações financeiras dos clientes. ",
                "O pagamento deve ser aprovado para que o pedido seja liberado."
            ]
        },{
            "id": 4,
            "nome_servico": "Atendimento",
            "responsavel": "Central de Atendimento ao Cliente",
            "tempo_estimado": "Até 30 minutos",
            "requisitos": [
                "O cliente poderá solicitar atendimento para esclarecimento de dúvidas, reclamações, sugestões ou informações sobre produtos e serviços. ",
                "Para agilizar o atendimento, recomenda-se informar o número do pedido, quando houver, além de uma descrição detalhada da solicitação. ",
                "O suporte é realizado durante o horário de funcionamento do mercado."
            ]
        }
    ]
    return servicos

# Create your views here.
def listaServicos(request):
    context = {'servicos': returnServico()}
    return render(request, 'servicos/listaservicos.html', context)

def detalheServico(request, id):
    for s in returnServico():
        if s['id'] == id:
            context = {'servico': s}
    return render(request, 'servicos/detalheservico.html', context)